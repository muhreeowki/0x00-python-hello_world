#!/bin/bash
# Bash script that sends a GET request to that URL, and displays the size (in bytes) of the body of the response
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
