#!/usr/bin/env bash
set -e

# Create venv and activate
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip and install build helpers
python -m pip install --upgrade pip setuptools wheel setuptools_scm

# Install Pillow using current environment to avoid isolated-build issues
pip install --no-build-isolation pillow==10.0.0

# Install remaining requirements
pip install -r ../requirements.txt

echo "Done. If you still see build errors, install OS-level build deps (libjpeg, zlib, build-essential)."
