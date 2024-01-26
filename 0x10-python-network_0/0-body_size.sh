#!/bin/bash
# Finds the byte size of the HTTP response header for given URL.
curl -s "$1" | wc -c
