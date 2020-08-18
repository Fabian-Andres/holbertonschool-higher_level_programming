#!/bin/bash
# cURL a JSON file 
curl -sX POST -H "Content-Type: application/json" --data @$1 $2
