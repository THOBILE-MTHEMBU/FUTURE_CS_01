# FUTURE_CS_01

Cyber Security Task 1 (2026) for Future Interns.

This repository documents a read-only vulnerability assessment performed against a public demo website:

- Target website: `testphp.vulnweb.com`
- Assessment date: `2026-04-14`
- Track code: `CS`
- Task: `Vulnerability Assessment Report for a Live Website`

## Purpose

The goal of this task was to assess a live public website using passive, non-destructive techniques and present the results in a professional, business-friendly format. The focus was on:

- identifying common web security weaknesses
- classifying risks as Low, Medium, or High
- explaining business impact in plain language
- recommending practical remediation steps

## Scope

### In Scope

- Public-facing pages only
- Passive review of exposed services and HTTP behavior
- Publicly visible configuration and technology indicators
- Read-only inspection of forms, headers, and accessible pages

### Out of Scope

- Authentication bypass
- Brute forcing
- Exploitation
- Denial-of-Service
- Any action that could harm availability, integrity, or confidentiality

## Target Selection

`testphp.vulnweb.com` was selected because it is a well-known public training target used for security testing and learning. The site itself publicly states that it is intentionally vulnerable and intended for testing and education.

## Tools Used

- Passive web review
- Public HTTP/header exposure data
- Browser-accessible page review
- OWASP guidance for remediation mapping
- Markdown for report packaging
- Recreated screenshot evidence in SVG format

Note: `nmap`, OWASP ZAP, and direct GUI browser tooling were part of the original task brief, but they were not available in this local environment during preparation. To keep the submission ethical and evidence-based, the assessment used passive observations and publicly accessible scan evidence only. This limitation is documented transparently in the evidence files.

## Deliverables

- Formal report: [report/Vulnerability_Assessment_Report.md](report/Vulnerability_Assessment_Report.md)
- Word document: [report/Vulnerability_Assessment_Report.docx](report/Vulnerability_Assessment_Report.docx)
- PDF document: [report/Vulnerability_Assessment_Report.pdf](report/Vulnerability_Assessment_Report.pdf)
- Canva-designed report PDF: [report/Vulnerability_Assessment_Report_Canva.pdf](report/Vulnerability_Assessment_Report_Canva.pdf)
- Evidence log: [evidence/02_passive_scan_evidence.md](evidence/02_passive_scan_evidence.md)
- Findings matrix: [evidence/03_findings_matrix.md](evidence/03_findings_matrix.md)
- Screenshot notes: [evidence/04_screenshot_notes.md](evidence/04_screenshot_notes.md)
- Recreated screenshots:
  - [screenshots/phpinfo_exposure.svg](screenshots/phpinfo_exposure.svg)
  - [screenshots/header_review.svg](screenshots/header_review.svg)

## Executive Summary

The assessment found several meaningful weaknesses that would matter on a real business website:

- the site exposed a public `phpinfo()` page with detailed server configuration
- the exposed stack showed an obsolete PHP version
- the site did not present a valid TLS/SSL certificate in the passive snapshot
- key browser security headers were missing
- the server disclosed technology details through response headers

Overall risk rating: `High`

This rating is driven by the combination of insecure transport, sensitive configuration exposure, and obsolete server-side technology.

## Repository Structure

```text
FUTURE_CS_01/
|-- README.md
|-- screenshots/
|   |-- header_review.svg
|   `-- phpinfo_exposure.svg
|-- scripts/
|   |-- generate_docx.py
|   `-- generate_pdf.py
|-- report/
|   |-- Vulnerability_Assessment_Report_Canva.pdf
|   |-- Vulnerability_Assessment_Report.docx
|   |-- Vulnerability_Assessment_Report.md
|   `-- Vulnerability_Assessment_Report.pdf
`-- evidence/
    |-- 01_target_and_methodology.md
    |-- 02_passive_scan_evidence.md
    |-- 03_findings_matrix.md
    `-- 04_screenshot_notes.md
```

## Ethics Statement

This assessment was completed in a read-only manner. No exploitation, credential attacks, forced browsing, service disruption, or destructive activity was performed.

## Reviewer Notes

This repository is written so it can be reviewed by:

- a business owner
- a client-facing agency team
- a security consultant

The report intentionally avoids unnecessary jargon and ties each issue to practical business risk and remediation priority.

The repository now also includes the Canva-designed PDF version requested in the task brief for a more presentation-ready client deliverable.
