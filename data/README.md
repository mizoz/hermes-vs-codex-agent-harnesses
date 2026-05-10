# Data

Use synthetic or sanitized benchmark data only.

Do not store:

- live record-system rows;
- operational rows;
- message-system inbox or draft data;
- payment data;
- signature-workflow records;
- private-entity personal data;
- secrets or credentials.

`data/sample/` contains illustrative synthetic records. `data/raw/` should stay
empty until a public-safe benchmark fixture is approved.
