#!/bin/sh

set -e

for v in "$@"
do
  test -f "$v"
done
