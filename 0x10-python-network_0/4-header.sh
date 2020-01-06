#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -Ls -X 'GET' "$1" -H "X-HolbertonSchool-User-Id :98"
