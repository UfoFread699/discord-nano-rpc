#!/usr/bin/env bash
# Setup for Arch Linux (also works on other distros with python3).
# Installs the required packages, creates a virtualenv and installs pypresence.
set -e

echo "[1/3] Checking / installing required packages..."
if command -v pacman >/dev/null 2>&1; then
    sudo pacman -S --needed --noconfirm git python
else
    echo "  (pacman not found – skipping package install, continuing with venv)"
fi

echo "[2/3] Creating virtual environment..."
python -m venv .venv

echo "[3/3] Installing pypresence..."
.venv/bin/pip install --upgrade pip >/dev/null
.venv/bin/pip install -r requirements.txt

echo ""
echo "Done!"
echo "If you don't have your own Discord app yet, follow README.md."
echo "Start it with:  ./nano.sh"
