#!/bin/bash
while sleep 1; do echo -n "$(date +%s) "; curl -s -l /dev/null -w "Code: %{http_code} Time: %{time_total}\n" https://google.com; done
