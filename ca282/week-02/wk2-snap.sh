#!/bin/sh

read s

while read n && test ! "$s" = "$n"
do
  s="$n"
done

echo "$n"
