#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -X GET -o /dev/null --silent --head --write-out '%{http_code}\n' "$1"
