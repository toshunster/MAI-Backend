#! /usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

readonly WORKERS_CNT=4

function main()
{
  if ! gunicorn --workers ${WORKERS_CNT} myapp:app ; then
    echo "Failed to run gunicorn..."
    return 1
  fi
}

main $@
