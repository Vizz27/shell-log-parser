# src/parse_logs.py
import re
from collections import Counter
import json

LEVELS = ['INFO', 'WARN', 'ERROR']

def parse_log_text(text):
    '''
    Parse log text (string). Returns Counter of levels and top messages.
    '''
    level_pattern = re.compile(r'\b(INFO|WARN|ERROR)\b')
    messages = []
    counts = Counter()
    for line in text.splitlines():
        m = level_pattern.search(line)
        if m:
            lvl = m.group(1)
            counts[lvl] += 1
            # simple message extraction (everything after the level token)
            parts = line.split(lvl, 1)
            msg = parts[1].strip() if len(parts) > 1 else line.strip()
            messages.append(msg)
    top_messages = Counter(messages).most_common(10)
    return counts, top_messages

def parse_log_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    return parse_log_text(text)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python src/parse_logs.py /path/to/logfile')
        sys.exit(1)
    counts, top = parse_log_file(sys.argv[1])
    print('Level counts:')
    for k in ['INFO','WARN','ERROR']:
        print(f'{k}:', counts.get(k,0))
    print('\nTop messages:')
    for msg, c in top:
        print(c, msg)
