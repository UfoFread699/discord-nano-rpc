#!/usr/bin/env bash
# Start the "Nano" Discord Rich Presence.
set -e
cd "$(dirname "$0")"
exec .venv/bin/python nano_rpc.py
