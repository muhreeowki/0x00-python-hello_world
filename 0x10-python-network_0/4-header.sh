#!/bin/bash
# Bash script that sends a GET request to that URL, and displays the size (in bytes) of the body of the response
curl -s -X GET -H "X-School-User-Id: 98" $1
