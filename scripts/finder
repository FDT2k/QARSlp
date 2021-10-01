#!/usr/bin/env bash

if [ ! -z "$@" ]
then
  QUERY=$@
  if [[ "$@" == /* ]]
  then
    if [[ "$@" == *\?\? ]]
    then
      coproc ( exo-open "${QUERY%\/* \?\?}"  > /dev/null 2>&1 )
      exec 1>&-
      exit;
    else
      coproc ( exo-open "$@"  > /dev/null 2>&1 )
      exec 1>&-
      exit;
    fi
  elif [[ "$@" == \!\!* ]]
  then
    echo "Search files / folders"
  elif [[ "$@" == \?* ]]
  then
    echo "--> Search again??"
    while read -r line; do
      echo "$line" \?\?
    done <<< $(find ~ -type d -path '*/\.*' -prune -o -not -name '.*' -type f -iname *"${QUERY#\?}"* -print)
  else
    echo "--> Search again??"
    find ~ -type d -path '*/\.*' -prune -o -not -name '.*' -type f -iname *"${QUERY#!}"* -print
  fi
else
  echo "Search files / folders"
fi
