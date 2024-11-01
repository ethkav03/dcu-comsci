#!/bin/sh

n="$1"

seq -f "dir.%06.0f" $n |
xargs mkdir -p
