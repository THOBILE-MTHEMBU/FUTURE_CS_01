# Screenshot Notes

The internship brief asked for screenshots where applicable. Because direct GUI capture was not available in this workspace, the repository includes recreated SVG evidence panels based on the passive findings already documented in the report and evidence files.

## Included Visual Evidence

### 1. `phpinfo_exposure.svg`

This panel summarizes the public `phpinfo()` exposure and highlights:

- publicly accessible diagnostic page
- obsolete `PHP 5.1.6`
- legacy Apache and OpenSSL components
- sensitive configuration detail exposure

### 2. `header_review.svg`

This panel summarizes the passive header review and highlights:

- exposed `server` and `x-powered-by` headers
- lack of modern browser security headers
- passive transport and hardening concerns

## Why Recreated Evidence Was Used

The assessment remained within a non-destructive, text-first shell environment. To keep the repository easy to review, these visuals were prepared as clean evidence summaries rather than raw browser screenshots.

They are not presented as live UI captures. They are reviewer-friendly visual summaries of the documented passive findings.
