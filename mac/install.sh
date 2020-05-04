#!/bin/sh
readonly PROJECT_DIR=$(git rev-parse --show-toplevel)

ln -sfv ${PROJECT_DIR}/mac/config.py ~/Library/Application\ Support/Keyhac/config.py
