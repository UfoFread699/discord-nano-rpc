#!/usr/bin/env bash
# Spustí Discord Rich Presence "Nano".
set -e
cd "$(dirname "$0")"
exec .venv/bin/python nano_rpc.py
