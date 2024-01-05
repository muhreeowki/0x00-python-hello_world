#!/bin/bash
# Bash script that sends a GET request to that URL, and displays the size (in bytes) of the body of the response
curl -s -w '%{response_code}\n' -o /dev/null $1
