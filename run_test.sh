#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate

# Run tests
pytest test_app.py

# Return appropriate exit code
if [ $? -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Tests failed."
    exit 1
fi