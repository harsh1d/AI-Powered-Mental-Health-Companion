# 🚀 Quick Start Guide - MindCompanion

## For Windows Users

### Option 1: Easy One-Click Startup (Recommended)
1. Double-click `run.bat`
2. The app will start automatically and open in your browser

### Option 2: Manual Startup
1. Open Command Prompt or PowerShell
2. Navigate to the project directory:
   ```
   cd "C:\Users\[YourUsername]\OneDrive\Desktop\VS Code\IDEA\AI-Powered Mental Health Companion"
   ```
3. Run:
   ```
   streamlit run app.py
   ```
4. Open your browser and go to: `http://localhost:8501`

---

## For macOS/Linux Users

### Option 1: Easy Startup Script
1. Open Terminal
2. Navigate to the project directory:
   ```
   cd ~/path/to/AI-Powered-Mental-Health-Companion
   ```
3. Make the script executable:
   ```
   chmod +x run.sh
   ```
4. Run:
   ```
   ./run.sh
   ```

### Option 2: Manual Startup
1. Open Terminal
2. Navigate to the project directory
3. Run:
   ```
   streamlit run app.py
   ```
4. Open your browser and go to: `http://localhost:8501`

---

## Troubleshooting

### Issue: Python not found
- Install Python 3.8+ from [python.org](https://www.python.org)
- Make sure to check "Add Python to PATH" during installation

### Issue: Dependencies not installing
Try upgrading pip:
```
pip install --upgrade pip
```

Then reinstall requirements:
```
pip install -r requirements.txt
```

### Issue: Model download is slow
- The Hugging Face model (~500MB) downloads on first run
- This is normal and only happens once
- Subsequent runs will be faster
- Make sure you have stable internet connection

### Issue: Module not found errors
Try installing dependencies again with verbose output:
```
pip install -r requirements.txt -v
```

### Issue: Port 8501 already in use
Run Streamlit on a different port:
```
streamlit run app.py --server.port 8502
```

---

## Using the App

### First Time Setup
1. The emotion detection model will load (1-2 minutes on first run)
2. Once loaded, the app will display the main interface
3. Start typing in the chat box to begin

### Features to Explore
- **Chat**: Share your feelings and get empathetic responses
- **Dashboard**: See your emotional trend in the sidebar
- **Breathing Guide**: Enable guided breathing exercise
- **Quick Resources**: Access crisis hotlines anytime

### Demo Scenario (for testing)
Try typing these to see different responses:
- "I'm feeling really sad today" → Sadness response
- "I'm so anxious about the future" → Anxiety response with breathing exercise
- "I want to hurt myself" → Triggers Safety Mode with crisis resources
- "I'm having a great day!" → Joy response

---

## For Hackathon Presenters

### Pre-Presentation Checklist
- [ ] Download the Hugging Face model before the event
- [ ] Test the app once to ensure everything works
- [ ] Have talking points about emotion detection
- [ ] Know how to trigger Safety Mode (type crisis keywords)
- [ ] Have backup computer in case of technical issues

### Recommended Demo Flow
1. Show beautiful UI and explain design philosophy
2. Type a normal message and show emotion detection
3. Type an anxiety message and show breathing exercise
4. Type a crisis keyword and demonstrate Safety Mode
5. Show the emotional trend dashboard
6. Explain the NLP pipeline and safety protocols

---

## Keyboard Shortcuts (in Streamlit)

- `Ctrl+S`: Save config
- `C`: Clear cache
- `R`: Rerun script
- `E`: Show element details

---

## Files Overview

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit application |
| `nlp_logic.py` | Emotion detection & crisis detection |
| `persona_engine.py` | AI responses & personality |
| `requirements.txt` | Python dependencies |
| `test_components.py` | Component verification script |
| `run.bat` | Windows startup script |
| `run.sh` | macOS/Linux startup script |
| `README.md` | Full documentation |

---

## Getting Help

### If something goes wrong:
1. Check the console output for error messages
2. Try running `python test_components.py` to verify components
3. Check Python version: `python --version` (should be 3.8+)
4. Try reinstalling: `pip install -r requirements.txt --force-reinstall`

### Common Issues:
- **Slow first run**: Model downloading, this is normal
- **Missing responses**: Model might still be loading
- **Port already in use**: Try different port with `--server.port`

---

## Next Steps

After getting comfortable with the app:
- Customize response templates in `persona_engine.py`
- Add more crisis keywords in `nlp_logic.py`
- Modify colors and styling in `app.py` CSS
- Deploy to Streamlit Cloud for sharing

---

**Remember: This app is for support and wellness, not medical treatment. Always encourage users to seek professional help when needed. 💙**
