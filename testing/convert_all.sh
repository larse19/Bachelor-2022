#!/bin/sh

find ./documentation -type f -name "*.md" -not -path "./documentation" -print0 | xargs -0 -I file bash ./convert.sh file
#find ./documentation -type f -name "*.html" -print0 | xargs -0 -I file rm file