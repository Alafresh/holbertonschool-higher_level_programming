#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -is -X OPTIONS "$1" | grep Access-Control-Allow-Methods | awk '{print $2 $3 $4 $5 $6 $7}'
