# Incident Response Plan

## 1. Detection
Incidents may be detected via GitHub Security Alerts, user reports, or automated integrity checks.

## 2. Containment
- Revoke compromised tokens.
- Mark affected releases as "unstable" or "compromised".
- Revert unauthorized commits.

## 3. Eradication & Recovery
- Patch the vulnerability.
- Rotate all secrets.
- Re-verify all data integrity using offline backups.

## 4. Post-Incident
- Publish a security advisory.
- Update the `THREAT_MODEL.md`.
