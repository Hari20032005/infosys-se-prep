#!/bin/bash
# Re-run every verifier and print its summary line. Exit code 1 if any fails.
cd "$(dirname "$0")/.."
rc=0
run() { echo "--- $1"; shift; "$@" 2>&1 | tail -${TAILN:-4}; [ ${PIPESTATUS[0]} -ne 0 ] && rc=1; }
TAILN=1 run "official_sample (54 official-sample items; those a computer can decide are decided by execution)" bash -c "python3 data/official_sample.py > /dev/null && python3 data/official_sample.py | head -1"
TAILN=3 run "verify_observed (61 observed answers by execution)" bash -c "cd data && python3 verify_observed.py"
TAILN=9 run "verify_generated (generated questions, real Java, printed pseudocode run as Java)" python3 data/verify_generated.py
TAILN=6 run "verify_mock" python3 data/verify_mock.py
TAILN=1 run "verify_cheatsheet" python3 data/build_cheatsheet.py --verify
TAILN=2 run "verify_copied (copied Accenture banks re-executed)" python3 data/verify_copied.py
TAILN=6 run "verify_core_course (lessons, worked examples, practice, readability)" python3 data/verify_core_course.py
TAILN=4 run "verify_keys" python3 data/verify_keys.py
TAILN=22 run "verify_structure" python3 data/verify_structure.py
TAILN=6 run "analyze.py reconciliation" python3 data/analyze.py
exit $rc
