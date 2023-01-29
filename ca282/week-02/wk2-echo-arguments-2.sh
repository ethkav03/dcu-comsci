#!/bin/sh

#for n in $( seq "$#" )
#do
#  echo "$n. ${!n}"
#done

i=1

for v in "$@"
do
  echo "$i. $v"
  i=$(( i + 1 ))
done
