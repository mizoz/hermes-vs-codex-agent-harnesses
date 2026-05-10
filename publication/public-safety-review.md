# Public-Safety Review

Review date: 2026-05-10

## Addressed Before Draft Release

- Removed local absolute paths from public-facing Markdown and regenerated HTML.
- Removed placeholder repository URL from `CITATION.cff`.
- Reframed Hermes/Codex comparison as a case-study observation and benchmark
  hypothesis, not a proven superiority claim.
- Marked internal source inspection as non-public case-study evidence.
- Generalized private operational system names in the reusable master prompt.
- Added package validation for:
  - JSON syntax;
  - sample shape;
  - local absolute path leaks;
  - placeholder strings;
  - prohibited attribution strings.

## Remaining Before Public Release

- Ahmed must approve the exact repository name and visibility.
- Ahmed must approve whether `dist/whitepaper.pdf` should be committed or only
  attached to a release.
- A real paired benchmark must run before quantitative claims are added.
- Any internal implementation excerpts must be sanitized before publication.
- Source links should be spot-checked one more time before final release.

## Release Position

Current state: draft methodology and architecture package, suitable for private
review. Not yet a results paper.
