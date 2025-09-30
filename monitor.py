# src/monitor.py
# Lightweight system monitor using psutil.
import time
import json
try:
    import psutil
except Exception:
    psutil = None

def snapshot():
    if psutil is None:
        raise RuntimeError('psutil not installed')
    return {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'virtual_memory': psutil.virtual_memory()._asdict(),
        'disk_usage': psutil.disk_usage('/')._asdict()
    }

def write_snapshot_to_file(path):
    s = snapshot()
    with open(path, 'w') as f:
        json.dump(s, f, indent=2)

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--out', default='snapshot.json')
    p.add_argument('--interval', type=int, default=60)
    args = p.parse_args()
    while True:
        write_snapshot_to_file(args.out)
        print('Wrote', args.out)
        time.sleep(args.interval)
