#!/bin/bash

# Navigate to parent directory
cd ..

# Check if .venv is not built
if [ ! -d ".venv" ]; then
  echo ".venv not found, creating virtual environment..."
  python3 -m venv .venv
else
  echo "Virtual env already exists. splendid"
fi

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
echo "Environment setup and checked. Launching..."

# Launch app
python app.py
