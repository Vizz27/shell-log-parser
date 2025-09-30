# Shell Log Parser & System Monitor (Example)
Tools: bash, Python (psutil), pytest, Allure (allure-pytest), GitHub Actions

What this demonstrates:
- A simple bash log parser (scripts/parse_logs.sh)
- A Python parser (src/parse_logs.py) which is unit-tested with pytest
- A lightweight system monitor (src/monitor.py) using psutil
- CI workflow that runs tests and stores allure results as artifact

Quickstart:
1. Create a virtualenv and install dependencies:
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

2. Run tests and produce Allure results:
   pytest --alluredir=allure-results

3. Serve or view the Allure report locally (if you have allure installed):
   allure serve allure-results

Files:
- scripts/parse_logs.sh : Bash parser (quick summary)
- src/parse_logs.py     : Python parser with functions you can import & test
- src/monitor.py        : Simple system monitor using psutil
- tests/test_parse.py   : pytest tests for parse_logs.py
- .github/workflows/ci.yml : Example GitHub Actions to run tests and upload results
