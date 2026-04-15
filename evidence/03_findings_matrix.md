# Findings Matrix

| ID | Finding | Risk | Business Impact | Recommended Priority |
| --- | --- | --- | --- | --- |
| F-01 | Publicly accessible `phpinfo()` page exposes configuration data | High | Makes targeted attacks easier and reveals internal environment details | Immediate |
| F-02 | Obsolete PHP and server components visible in public output | High | Increases likelihood of compromise through known vulnerabilities | Immediate |
| F-03 | No valid TLS/SSL certificate observed in passive scan | High | Risks interception of user-submitted data and damages trust | Immediate |
| F-04 | Modern browser security headers missing | Medium | Reduces browser-side protections against common web attacks | Short Term |
| F-05 | `server` and `x-powered-by` headers disclose technology stack | Low | Helps attackers fingerprint the environment more easily | Short Term |

## Priority Summary

The fastest risk reduction would come from:

1. removing public diagnostics
2. enforcing HTTPS with a valid certificate
3. upgrading unsupported server-side technology
