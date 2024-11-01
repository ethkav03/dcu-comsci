#!/bin/sh

# We expect all of these commands to succeed.  In fact, it makes no sense to continue
# if any of them fail.  So we exit with an error if any of these fail.
set -e

mkdir files
tar xf files.tgz -C files
