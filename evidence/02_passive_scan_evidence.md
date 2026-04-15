# Passive Scan Evidence

Assessment date: `2026-04-14`

## Evidence 1: Site States It Is Intentionally Vulnerable

Source:

- `https://testphp.vulnweb.com/login.php`

Observed in public search snippet:

> Warning: This is not a real shop. This is an example PHP application, which is intentionally vulnerable to web attacks.

Use in report:

- justified target selection for an ethical training assessment

## Evidence 2: Public `phpinfo()` Page

Source:

- `https://testphp.vulnweb.com/secured/phpinfo.php`

Observed publicly:

- `PHP Version 5.1.6`
- `Apache/2.2.3 (FreeBSD) DAV/2 PHP/5.1.6 mod_ssl/2.2.3 OpenSSL/0.9.7e-p1`
- filesystem paths, server variables, module inventory, request and response headers

Use in report:

- configuration disclosure
- obsolete technology exposure

## Evidence 3: Internet-Exposed Service

Source:

- `https://www.sitescan.com/report/testphp.vulnweb.com/port/list`

Observed publicly:

- open port `80/tcp`
- service: `http`

Use in report:

- confirms public HTTP exposure in the passive snapshot

## Evidence 4: Security Check Summary

Source:

- `https://www.sitescan.com/report/testphp.vulnweb.com/`

Observed publicly:

- `5 of 14 security checks passed`
- recommendations included:
  - `Use a valid SSL certificate`
  - `Use a content-security-policy HTTP header`
  - `Use a x-content-type-options HTTP header`
  - `Use a x-frame-options HTTP header`
  - `Use a referrer-policy HTTP header`
  - `Use a permissions-policy HTTP header`
  - `Send form submissions over HTTPS`
  - `Don't use obsolete technologies`
- certificate status shown as `None`

Use in report:

- transport security weakness
- missing security headers
- outdated technology signal

## Evidence 5: HTTP Header Snapshot

Source:

- `https://www.sitescan.com/report/testphp.vulnweb.com/header/list`

Observed publicly:

- header list contained:
  - `connection`
  - `content-type`
  - `date`
  - `location`
  - `server`
  - `transfer-encoding`
  - `x-powered-by`
- summary showed `Security 0`

Use in report:

- technology disclosure
- absence of common security headers

## Notes on Tooling

The original internship brief suggested `nmap`, OWASP ZAP Passive, Browser DevTools, and Canva. During preparation in this environment:

- `nmap` was not available locally
- OWASP ZAP was not available locally
- GUI browser tooling was not available through the workspace shell

To keep the work accurate and ethical, only passive, publicly visible evidence was documented. The report clearly separates observation from inference.
