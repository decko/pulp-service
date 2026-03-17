#!/bin/bash
# Watch for export-access-logs job pods and capture their logs.
# Usage: ./watch-job-logs.sh [namespace]
#   Logs are saved to ./job-logs/ with timestamps.

NAMESPACE="${1:+"-n $1"}"
LOG_DIR="./job-logs"
mkdir -p "${LOG_DIR}"
SEEN_PODS=""

echo "Watching for export-access-logs job pods..."
echo "Logs will be saved to ${LOG_DIR}/"
echo "Press Ctrl+C to stop."
echo ""

while true; do
  for pod in $(oc get pods ${NAMESPACE} --no-headers -l job-name -o custom-columns=NAME:.metadata.name,STATUS:.status.phase 2>/dev/null | grep -i "export-access-logs" | awk '{print $1}'); do
    if echo "${SEEN_PODS}" | grep -q "${pod}"; then
      continue
    fi

    SEEN_PODS="${SEEN_PODS} ${pod}"
    LOGFILE="${LOG_DIR}/${pod}_$(date '+%Y%m%dT%H%M%S').log"

    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Found pod: ${pod}"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Saving logs to: ${LOGFILE}"

    # Wait for container to be ready, then follow logs
    (
      oc wait ${NAMESPACE} --for=condition=Ready "pod/${pod}" --timeout=120s 2>/dev/null
      oc logs ${NAMESPACE} -f "${pod}" 2>&1 | tee "${LOGFILE}"
      echo ""
      echo "[$(date '+%Y-%m-%d %H:%M:%S')] Pod ${pod} finished. Log saved to ${LOGFILE}"
      echo ""
    ) &
  done

  sleep 10
done
