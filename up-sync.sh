#! /usr/bin/env bash
rsync -avzhP --delete --exclude '.git*' --exclude 'README.md' --exclude 'LICENSE' --exclude `basename $0` * deb:
