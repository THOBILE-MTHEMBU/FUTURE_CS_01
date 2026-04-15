from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "report" / "Vulnerability_Assessment_Report.md"
TARGET = ROOT / "report" / "Vulnerability_Assessment_Report.docx"


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>
"""


RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
"""


APP_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
            xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Codex</Application>
</Properties>
"""


CORE_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
                   xmlns:dc="http://purl.org/dc/elements/1.1/"
                   xmlns:dcterms="http://purl.org/dc/terms/"
                   xmlns:dcmitype="http://purl.org/dc/dcmitype/"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>Vulnerability Assessment Report</dc:title>
  <dc:creator>Codex</dc:creator>
</cp:coreProperties>
"""


WORD_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>
"""


def paragraph(text: str, style: str | None = None) -> str:
    style_xml = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ""
    return (
        "<w:p>"
        f"{style_xml}"
        "<w:r><w:t xml:space=\"preserve\">"
        f"{escape(text)}"
        "</w:t></w:r>"
        "</w:p>"
    )


def markdown_to_document_xml(markdown_text: str) -> str:
    body = []
    for raw_line in markdown_text.splitlines():
        line = raw_line.rstrip()
        if not line:
            body.append(paragraph(""))
            continue
        if line.startswith("# "):
            body.append(paragraph(line[2:], "Heading1"))
        elif line.startswith("## "):
            body.append(paragraph(line[3:], "Heading2"))
        elif line.startswith("### "):
            body.append(paragraph(line[4:], "Heading3"))
        elif line.startswith("- "):
            body.append(paragraph(f"• {line[2:]}"))
        else:
            body.append(paragraph(line))

    body.append("<w:sectPr/>")
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<w:document xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\">"
        f"<w:body>{''.join(body)}</w:body>"
        "</w:document>"
    )


def main() -> None:
    markdown_text = SOURCE.read_text(encoding="utf-8")
    document_xml = markdown_to_document_xml(markdown_text)

    with ZipFile(TARGET, "w", compression=ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", CONTENT_TYPES)
        docx.writestr("_rels/.rels", RELS)
        docx.writestr("docProps/app.xml", APP_XML)
        docx.writestr("docProps/core.xml", CORE_XML)
        docx.writestr("word/document.xml", document_xml)
        docx.writestr("word/_rels/document.xml.rels", WORD_RELS)

    print(f"Wrote {TARGET}")


if __name__ == "__main__":
    main()
