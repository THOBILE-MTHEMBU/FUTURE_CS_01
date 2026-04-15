from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "report" / "Vulnerability_Assessment_Report.md"
TARGET = ROOT / "report" / "Vulnerability_Assessment_Report.pdf"

PAGE_WIDTH = 595
PAGE_HEIGHT = 842
LEFT_MARGIN = 50
TOP_MARGIN = 780
BOTTOM_MARGIN = 50
LINE_HEIGHT = 16
FONT_SIZE = 11
MAX_CHARS = 88


def escape_pdf_text(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def wrap_line(text: str, width: int = MAX_CHARS) -> list[str]:
    text = text.rstrip()
    if not text:
        return [""]

    words = text.split()
    lines = []
    current = words[0]

    for word in words[1:]:
        candidate = f"{current} {word}"
        if len(candidate) <= width:
            current = candidate
        else:
            lines.append(current)
            current = word

    lines.append(current)
    return lines


def normalize_markdown_line(line: str) -> str:
    stripped = line.rstrip()
    if stripped.startswith("# "):
        return stripped[2:].strip().upper()
    if stripped.startswith("## "):
        return stripped[3:].strip()
    if stripped.startswith("### "):
        return stripped[4:].strip()
    if stripped.startswith("- "):
        return f"* {stripped[2:].strip()}"
    return stripped


def markdown_to_lines(markdown_text: str) -> list[str]:
    output = []
    for raw_line in markdown_text.splitlines():
        normalized = normalize_markdown_line(raw_line)
        output.extend(wrap_line(normalized))
    return output


def build_page_stream(lines: list[str]) -> str:
    commands = ["BT", f"/F1 {FONT_SIZE} Tf"]
    y = TOP_MARGIN

    for line in lines:
        if y < BOTTOM_MARGIN:
            break
        commands.append(f"1 0 0 1 {LEFT_MARGIN} {y} Tm ({escape_pdf_text(line)}) Tj")
        y -= LINE_HEIGHT

    commands.append("ET")
    return "\n".join(commands)


def paginate(lines: list[str]) -> list[list[str]]:
    pages = []
    page = []
    lines_per_page = ((TOP_MARGIN - BOTTOM_MARGIN) // LINE_HEIGHT) + 1

    for line in lines:
        page.append(line)
        if len(page) >= lines_per_page:
            pages.append(page)
            page = []

    if page:
        pages.append(page)

    return pages


def build_pdf(page_streams: list[str]) -> bytes:
    objects = []
    objects.append("<< /Type /Catalog /Pages 2 0 R >>")
    kids = " ".join(f"{4 + index * 2} 0 R" for index in range(len(page_streams)))
    objects.append(f"<< /Type /Pages /Count {len(page_streams)} /Kids [{kids}] >>")
    objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")

    for index, stream in enumerate(page_streams):
        page_object = (
            "<< /Type /Page /Parent 2 0 R "
            f"/MediaBox [0 0 {PAGE_WIDTH} {PAGE_HEIGHT}] "
            "/Resources << /Font << /F1 3 0 R >> >> "
            f"/Contents {5 + index * 2} 0 R >>"
        )
        stream_bytes = stream.encode("latin-1", errors="replace")
        content_object = f"<< /Length {len(stream_bytes)} >>\nstream\n{stream}\nendstream"
        objects.append(page_object)
        objects.append(content_object)

    pdf = ["%PDF-1.4\n%\xE2\xE3\xCF\xD3\n"]
    offsets = [0]

    for number, obj in enumerate(objects, start=1):
        offsets.append(sum(len(part.encode("latin-1", errors="replace")) for part in pdf))
        pdf.append(f"{number} 0 obj\n{obj}\nendobj\n")

    xref_offset = sum(len(part.encode("latin-1", errors="replace")) for part in pdf)
    pdf.append(f"xref\n0 {len(objects) + 1}\n")
    pdf.append("0000000000 65535 f \n")

    for offset in offsets[1:]:
        pdf.append(f"{offset:010d} 00000 n \n")

    pdf.append(
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n"
    )

    return "".join(pdf).encode("latin-1", errors="replace")


def main() -> None:
    lines = markdown_to_lines(SOURCE.read_text(encoding="utf-8"))
    pages = paginate(lines)
    page_streams = [build_page_stream(page) for page in pages]
    TARGET.write_bytes(build_pdf(page_streams))
    print(f"Wrote {TARGET}")


if __name__ == "__main__":
    main()
