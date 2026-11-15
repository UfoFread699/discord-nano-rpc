#!/usr/bin/env bash
# Setup pro Arch Linux (funguje i na jiných distribucích s python3).
# Nainstaluje potřebné balíčky, vytvoří virtuální prostředí a nainstaluje pypresence.
set -e

echo "[1/3] Kontroluji/instaluji potřebné balíčky..."
if command -v pacman >/dev/null 2>&1; then
    sudo pacman -S --needed --noconfirm git python
else
    echo "  (pacman nenalezen – přeskakuji instalaci balíčků, pokračuji s venv)"
fi

echo "[2/3] Vytvářím virtuální prostředí..."
python -m venv .venv

echo "[3/3] Instaluji pypresence..."
.venv/bin/pip install --upgrade pip >/dev/null
.venv/bin/pip install -r requirements.txt

echo ""
echo "Hotovo!"
echo "Pokud ještě nemáš vlastní Discord aplikaci, postupuj podle README.md."
echo "Spusť to příkazem:  ./nano.sh"
