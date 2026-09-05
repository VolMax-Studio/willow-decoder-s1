#!/usr/bin/env bash
# Concrete execution command
./runner.sh run-003-recreation 6daa877b181aa6ca09900589218eac2d1e8a5282

# Child command invoked by runner.sh:
python3 reproduce.py --run-id run-003-recreation --prereg-sha 6daa877b181aa6ca09900589218eac2d1e8a5282
