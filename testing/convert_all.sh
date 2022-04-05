#!/bin/sh

find ./documentation -type d -not -path "./documentation" -print0 | xargs -0 -I file bash ./convert.sh file