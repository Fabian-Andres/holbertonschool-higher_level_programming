#!/bin/bash
# 0-body_size
curl -so /dev/null $1 -w '%{size_download}\n'
