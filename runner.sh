#!/usr/bin/env bash
# runner.sh — Official Frozen Execution Wrapper for willow-decoder-s1
# Strictly enforces pre-execution preconditions and captures literal execution logs.

set -euo pipefail

RUN_ID="${1:-run-003-recreation}"
PREREG_SHA="${2:-}"

if [ -z "$PREREG_SHA" ]; then
    echo "Usage: ./runner.sh <RUN_ID> <PREREG_SHA>" >&2
    exit 1
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

# Pre-execution checks
if [ -n "$(git status --porcelain)" ]; then
    echo "FATAL [EXECUTION_STATE_INVALID]: Working tree is not clean before execution." >&2
    git status --porcelain >&2
    exit 1
fi

HEAD_SHA="$(git rev-parse HEAD)"
if [ "$HEAD_SHA" != "$PREREG_SHA" ]; then
    echo "FATAL [EXECUTION_STATE_INVALID]: HEAD ($HEAD_SHA) != expected PREREG_SHA ($PREREG_SHA)" >&2
    exit 1
fi

TMP_DIR="$(mktemp -d /tmp/willow_exec_XXXXXX)"
RUN_EVIDENCE_DIR="$REPO_ROOT/evidence/runs/$RUN_ID"

# Ensure evidence directory exists early to preserve logs even on early Python halt (W-3)
mkdir -p "$RUN_EVIDENCE_DIR"

echo "[runner.sh] Starting execution for $RUN_ID under PREREG_SHA $PREREG_SHA..."

# Execute reproduce.py with external log redirection
EXIT_CODE=0
python3 reproduce.py --run-id "$RUN_ID" --prereg-sha "$PREREG_SHA" > "$TMP_DIR/stdout.log" 2> "$TMP_DIR/stderr.log" || EXIT_CODE=$?

echo "$EXIT_CODE" > "$TMP_DIR/exit_code.txt"

# Record concrete executed command with expanded variables
cat << CMD_EOF > "$TMP_DIR/command.sh"
#!/usr/bin/env bash
# Concrete execution command
./runner.sh $RUN_ID $PREREG_SHA

# Child command invoked by runner.sh:
python3 reproduce.py --run-id $RUN_ID --prereg-sha $PREREG_SHA
CMD_EOF
chmod +x "$TMP_DIR/command.sh"

{
    echo "HOSTNAME: $(hostname)"
    echo "DATETIME_UTC: $(date -u +'%Y-%m-%dT%H:%M:%SZ')"
    echo "UNAME: $(uname -a)"
    echo "PYTHON_VERSION: $(python3 --version 2>&1)"
    echo "GIT_COMMIT: $HEAD_SHA"
    echo "RUN_ID: $RUN_ID"
    echo "PREREG_SHA: $PREREG_SHA"
} > "$TMP_DIR/env.txt"

# Copy captured artifacts into evidence directory
cp "$TMP_DIR/stdout.log" "$RUN_EVIDENCE_DIR/stdout.log"
cp "$TMP_DIR/stderr.log" "$RUN_EVIDENCE_DIR/stderr.log"
cp "$TMP_DIR/exit_code.txt" "$RUN_EVIDENCE_DIR/exit_code.txt"
cp "$TMP_DIR/command.sh" "$RUN_EVIDENCE_DIR/command.sh"
cp "$TMP_DIR/env.txt" "$RUN_EVIDENCE_DIR/env.txt"

# Re-finalize outputs.sha256 to cover all artifacts
python3 -c '
import os, sys, hashlib
run_dir = sys.argv[1]
hashes = []
for root, _, files in os.walk(run_dir):
    for f in sorted(files):
        if f == "outputs.sha256":
            continue
        fpath = os.path.join(root, f)
        relpath = os.path.relpath(fpath, run_dir)
        with open(fpath, "rb") as fp:
            h = hashlib.sha256(fp.read()).hexdigest()
        hashes.append(f"{h}  {relpath}")
with open(os.path.join(run_dir, "outputs.sha256"), "w") as fp:
    fp.write("\n".join(hashes) + "\n")
' "$RUN_EVIDENCE_DIR"

rm -rf "$TMP_DIR"

echo "[runner.sh] Execution finished with exit code $EXIT_CODE."
echo "[runner.sh] Evidence directory: $RUN_EVIDENCE_DIR"
cat "$RUN_EVIDENCE_DIR/stdout.log"

exit "$EXIT_CODE"
