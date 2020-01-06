#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -Ls "$1" -X 'POST' -H "email: hr@holbertonschool.com\nsubject: I will always be here for PLD"
