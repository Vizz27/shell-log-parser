# shell-log-parser

[CI](https://github.com/<Vizz27>/shell-log-parser/actions/workflows/ci.yml/badge.svg)

**Short description:** Small toolset to parse service logs (Bash + Python), lightweight system monitor (psutil), pytest unit tests and Allure test reporting. Demonstrates test automation and CI for production-like observability pipelines.

## Tech stack
- Bash, Python 3.10+, pytest, allure-pytest
- GitHub Actions (CI), Allure test reporting

## Quickstart
1. Clone:
   git clone https://github.com/<username>/shell-log-parser.git
2. Run demo:
   cd shell-log-parser
   ./demo.sh

## What to look for
- `scripts/parse_logs.sh` — bash parser producing summary CSV.
- `src/parse_logs.py` — Python parser + reusable functions.
- `src/monitor.py` — psutil snapshotter.
- `tests/` — pytest unit tests.
- `.github/workflows/ci.yml` — CI that runs tests & uploads `allure-results`.


## License
MIT
