#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -Lsf "$1"
#curl -s -I "$1" | grep HTTP/ | awk {"print $2"}
#curl -X GET -o /dev/null --silent --head --write-out '%{http_code}\n' "$1"
