#!/bin/bash
# Bash script that sends a GET request to that URL, and displays the size (in bytes) of the body of the response
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)
