#!/bin/bash
# MindCompanion Startup Script for macOS/Linux

set -e

echo ""
echo "========================================"
echo "  🧠 MindCompanion - Mental Health AI"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    echo "Please install Python 3.8+ from python.org"
    exit 1
fi

echo "✓ Python found: $(python3 --version)"
echo ""

# Check if requirements are installed
echo "Checking dependencies..."
if ! python3 -c "import streamlit, transformers, torch, nltk, pandas, altair" 2>/dev/null; then
    echo "⚠️  Some dependencies are missing. Installing..."
    pip install -r requirements.txt
fi

echo "✓ All dependencies installed"
echo ""

# Run component tests
echo "Running component tests..."
python3 test_components.py
if [ $? -ne 0 ]; then
    echo "❌ Component tests failed"
    exit 1
fi

echo ""
echo "========================================"
echo "   🚀 Starting MindCompanion..."
echo "========================================"
echo ""
echo "The app will open in your browser at:"
echo "💻 http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Launch Streamlit
streamlit run app.py
