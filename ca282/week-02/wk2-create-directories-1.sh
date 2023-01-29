#!/bin/sh

n="$1"

seq -f "dir.%.0f" $n |
xargs mkdir -p
