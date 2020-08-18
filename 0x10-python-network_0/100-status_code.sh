#!/bin/bash
# Curl status code
curl -so /dev/null $1 -w '%{http_code}'
