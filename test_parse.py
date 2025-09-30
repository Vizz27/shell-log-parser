# tests/test_parse.py
from src.parse_logs import parse_log_text

SAMPLE = '''
2025-09-01 12:00:00 INFO Starting service
2025-09-01 12:00:01 WARN Slow response
2025-09-01 12:00:02 ERROR Failed to connect
2025-09-01 12:00:03 INFO Health check OK
2025-09-01 12:00:04 ERROR Timeout while reading
'''

def test_counts_and_top_messages():
    counts, top = parse_log_text(SAMPLE)
    assert counts['INFO'] == 2
    assert counts['WARN'] == 1
    assert counts['ERROR'] == 2
    # verify top returns tuples (message, count)
    assert isinstance(top, list)
