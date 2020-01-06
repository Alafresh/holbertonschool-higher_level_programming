#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -Ls "$1" -X 'GET' -H "X-HolbertonSchool-User-Id: 98"
