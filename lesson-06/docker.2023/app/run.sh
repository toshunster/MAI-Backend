#! /usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

function main()
{
  local message=; message=$(/usr/games/fortune)
  if [ $# -ne 0 ]; then
    message=${@}
  fi
  echo ${message} | /usr/games/cowsay -f tux
}

main ${@}
