#!/bin/sh

for v in "$@"
do
  if test -f "$v"
  then
     echo "$v file"
  elif test -d "$v"
  then
    echo "$v directory"
  else
    echo "$v does not exist"
  fi
done
