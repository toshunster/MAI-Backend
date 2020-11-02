#! /usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

function main()
{
  if test -z "${EXAMPLE_VAR}" ; then
    echo "Variable EXAMPLE_VAR is empty"
  fi
  echo "Content of EXAMPLE_VAR is \"${EXAMPLE_VAR}\""
  for file in text.html text.txt cat.png ; do
    echo "Try detect mime-type for ${file}..."
    ./mime_detect.py ${file}
  done
}

main $@
