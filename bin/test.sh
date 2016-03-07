#!/bin/bash
# (c) Crown Owned Copyright, 2016. Dstl.
dot="$(cd "$(dirname "$0")"; pwd)"
cd "$dot/../"
result=0

# Ensure we are in a virtualenv
. ./bin/virtualenv.sh
(( result+=$? ))

# Run the tests
./manage.py test
(( result+=$? ))

exit $result
