#!/usr/bin/env bash
# scripts/parse_logs.sh
# Usage: ./parse_logs.sh /path/to/logfile > summary.csv
LOGFILE="$1"
if [ -z "$LOGFILE" ]; then
  echo "Usage: $0 /path/to/logfile"
  exit 1
fi
if [ ! -f "$LOGFILE" ]; then
  echo "Log file not found: $LOGFILE"
  exit 2
fi

# Count by level (INFO/WARN/ERROR) and output CSV: level,count
echo "level,count"
grep -E "INFO|WARN|ERROR|ERROR:" "$LOGFILE" | awk '{print $0}' |       awk '{
    if ($0 ~ /ERROR/) e++;
    else if ($0 ~ /WARN/) w++;
    else if ($0 ~ /INFO/) i++;
  }
  END {print "INFO," (i+0) "\nWARN," (w+0) "\nERROR," (e+0)}
  '     