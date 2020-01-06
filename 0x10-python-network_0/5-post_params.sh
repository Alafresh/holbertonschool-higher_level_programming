#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -H "X-Holber
tonSchool-User-Id: 98" -X 'POST' "$1"
