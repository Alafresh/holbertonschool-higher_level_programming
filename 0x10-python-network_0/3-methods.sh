#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -is -X OPTIONS "$1" | grep Allow: | grep Allow: | cut -d ' ' -f2-
