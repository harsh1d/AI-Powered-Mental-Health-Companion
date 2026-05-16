# 🧠 MindCompanion: AI-Powered Mental Health Companion

A beautiful, empathetic, and intelligent mental health support chatbot built with Streamlit, Hugging Face Transformers, and advanced NLP. Designed for hackathon presentations and local deployment.

## ✨ Features

### 🎨 Beautiful, Calming UI/UX
- **Gradient backgrounds** with soft pastel colors (blues, greens, whites)
- **Modern chat bubbles** with distinct styling for user and AI messages
- **Responsive design** that works on desktop and tablet devices
- **Smooth animations** and intuitive navigation
- **Accessibility-first** design approach

### 🤖 Emotionally Intelligent AI
- **Warm, validating personality** that avoids toxic positivity
- **Context-aware responses** based on detected emotions
- **Empathetic language** that mirrors and validates user feelings
- **Actionable coping strategies** (e.g., 4-7-8 breathing exercise)
- **Non-judgmental and compassionate** support

### 🧠 Advanced NLP Engine
- **Emotion detection** using Hugging Face's `distilbert-base-uncased-emotion` model
- **Crisis keyword detection** with severity classification (critical, severe, moderate)
- **Text preprocessing** with tokenization, stemming, and stopword removal
- **Session emotion tracking** with trend analysis

### 🆘 Safety & Crisis Management
- **Automatic Safety Mode** activation for critical situations
- **Crisis hotline information** prominently displayed
- **Escalation detection** through consecutive negative emotions
- **Gentle, non-judgmental** crisis protocols
- **Immediate access** to professional mental health resources

### 📊 Wellness Dashboard
- **Emotional trend visualization** with interactive charts
- **Real-time mood tracking** across your session
- **Guided breathing exercises** (4-7-8 breathing technique)
- **Session statistics** (message count, session duration)
- **Quick access to crisis resources**

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project:**
```bash
cd "path/to/AI-Powered Mental Health Companion"
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

   The first time you run the app, it will automatically download the Hugging Face model (~500MB).

3. **Run the application:**
```bash
streamlit run app.py
```

4. **Access the application:**
The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
AI-Powered Mental Health Companion/
├── app.py                 # Main Streamlit application
├── nlp_logic.py          # NLP engine with emotion detection & crisis detection
├── persona_engine.py     # AI personality & response generation
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## 🔧 Architecture & Components

### 1. **nlp_logic.py** - NLP Engine
- **NLPEngine class** handles all natural language processing
- **Emotion Detection**: Uses Hugging Face transformer for 7-class emotion classification (sadness, joy, anger, fear, surprise, love, neutral)
- **Crisis Detection**: Scans for crisis keywords organized by severity level
- **Text Preprocessing**: Tokenization, stemming, and stopword removal
- **Session Analysis**: Calculates dominant emotion and emotional trend
- **Chart Data Generation**: Converts emotion history to visualization data

### 2. **persona_engine.py** - AI Personality
- **PersonaEngine class** generates deeply empathetic responses
- **Response Templates**: Organized by emotion with opening, validation, and offering phases
- **Crisis Protocols**: Special handling for critical and severe situations
- **Coping Strategies**: Includes breathing exercises and grounding techniques
- **Follow-up Questions**: Natural conversation continuers for engagement

### 3. **app.py** - Streamlit Application
- **Session State Management**: Tracks chat history, emotions, and safety status
- **Custom CSS**: Beautiful, soothing visual design with gradient backgrounds and modern styling
- **Chat Interface**: Modern message bubbles with emotion-aware styling
- **Sidebar Dashboard**: Wellness tracking with charts and quick resources
- **Safety Mode Rendering**: Emergency UI for crisis situations
- **Error Handling**: Graceful handling of NLP model errors and edge cases

## 💡 How It Works

### Conversation Flow
1. **User Input**: User shares their thoughts or feelings
2. **Emotion Detection**: NLP engine classifies the emotional content (confidence: 0-1)
3. **Crisis Detection**: System scans for crisis keywords and severity levels
4. **Safety Check**: If critical/severe crisis detected, activate Safety Mode
5. **Escalation Check**: Track last 3 emotions for pattern of distress
6. **Response Generation**: AI generates contextual, empathetic response
7. **History Tracking**: Store emotion data for trend analysis
8. **Dashboard Update**: Sidebar refreshes with new emotional trend data

### Safety Mode Activation
Safety Mode triggers automatically when:
- **Critical crisis keywords** detected (suicide, self-harm intent, etc.)
- **Severe crisis keywords** detected (dark ideation, hopelessness, etc.)
- **Escalation pattern** observed (3+ consecutive negative emotions)

When activated:
- Main chat area displays crisis hotline information prominently
- Normal conversation responses are replaced with emergency protocols
- User is gently encouraged to contact professional resources
- Information is presented with compassion, not alarm

## 🌍 Crisis Resources Built-In

The app includes immediate access to:

**🇺🇸 United States**
- National Suicide Prevention Lifeline: **988** (call or text)
- Crisis Text Line: Text **HOME** to **741741**

**🌍 International**
- International Association for Suicide Prevention: https://www.iasp.info/resources/Crisis_Centres/

## 🧠 Response Philosophy

MindCompanion follows these principles:

1. **Validation Over Solutions**: Acknowledge feelings before offering strategies
2. **No Toxic Positivity**: Never minimize suffering with "just think positive" advice
3. **Contextual Awareness**: Responses vary based on detected emotion
4. **Actionable Support**: Provide specific coping techniques when appropriate
5. **Professional Humility**: Clear boundaries about when professional help is needed
6. **Compassionate Language**: Warm, human tone without clinical detachment
7. **Crisis-First Safety**: Immediate, clear protocols for serious situations

## 📊 Emotions Detected

The emotion classifier recognizes:
- 😢 **Sadness** - Loss, disappointment, grief
- 😊 **Joy** - Happiness, contentment, celebration
- 😠 **Anger** - Frustration, rage, indignation
- 😰 **Fear** - Anxiety, terror, worry
- 😲 **Surprise** - Shock, astonishment
- 💖 **Love** - Affection, warmth, care
- 😐 **Neutral** - Balanced, informative, factual

## ⚙️ Configuration & Customization

### Adjusting Crisis Keywords
Edit the `crisis_keywords` dictionary in `nlp_logic.py`:
```python
self.crisis_keywords = {
    "critical": [keywords for severe situations],
    "severe": [keywords for serious situations],
    "moderate": [keywords for concerning patterns]
}
```

### Customizing Response Templates
Edit response templates in `persona_engine.py`:
```python
self.response_templates = {
    "emotion_name": {
        "opening": [opening lines],
        "validation": [validating statements],
        "offering": [supportive offers],
        "coping": {additional coping strategies}
    }
}
```

### Adjusting Escalation Detection
In `app.py`, modify the escalation check logic:
```python
# Current: 3+ consecutive negative emotions trigger safety mode
if len(recent_emotions) >= 3:
    ...
```

## 🔐 Privacy & Security

- **No data storage**: All conversations exist only in session state
- **No external logging**: NLP happens locally (no cloud transmission)
- **Open source**: Code is transparent and auditable
- **No authentication required**: Works completely locally
- **Disclaimer included**: Clear messaging about limitations and professional resources

## ⚠️ Important Disclaimer

**MindCompanion is not a substitute for professional mental health care.** 

This application is designed to:
- ✅ Provide emotional support and companionship
- ✅ Detect crisis situations and connect users to professional help
- ✅ Offer coping strategies and wellness resources
- ✅ Reduce stigma around mental health conversations

This application does NOT:
- ❌ Replace therapy or counseling
- ❌ Diagnose mental health conditions
- ❌ Prescribe treatments or medications
- ❌ Provide medical advice

**If you are experiencing a mental health crisis or suicidal thoughts, please contact a mental health professional or crisis service immediately.**

## 🛠️ Troubleshooting

### Issue: Model loading is slow on first run
**Solution**: The Hugging Face model (~500MB) is downloaded on first run. This is normal. Subsequent runs will be faster.

### Issue: Out of memory errors
**Solution**: The model uses CPU inference by default. If you have a GPU, you can modify `device=-1` to `device=0` in `nlp_logic.py`.

### Issue: Some emotions not being detected correctly
**Solution**: The emotion classifier works best with clear emotional language. Very sarcastic or indirect expressions may be misclassified—this is expected behavior for the model.

### Issue: NLTK data not found
**Solution**: The app automatically downloads NLTK data on first run. If you encounter errors, run:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## 🚀 Deployment & Hackathon Tips

### For Hackathon Presentations:
1. **Pre-download the model** before the presentation (first run takes 1-2 minutes)
2. **Use a stable internet connection** for downloading models
3. **Test crisis mode activation** before presenting (type keywords like "suicide" to demo)
4. **Prepare talking points** about the emotion detection and safety protocols
5. **Have a backup computer** in case of technical issues

### For Production Deployment:
1. **Use Streamlit Cloud** for hosted deployments (free tier available)
2. **Implement database logging** for conversation history (optional)
3. **Add authentication** if needed
4. **Set up monitoring** for crisis keyword detection
5. **Add admin dashboard** for analytics
6. **Implement rate limiting** to prevent abuse

## 📚 Technical Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit 1.40+ |
| **NLP Model** | Hugging Face Transformers (DistilBERT) |
| **ML Framework** | PyTorch 2.0+ |
| **Text Processing** | NLTK 3.8+ |
| **Data Handling** | Pandas 2.0+ |
| **Visualization** | Altair 5.0+ |
| **Language** | Python 3.8+ |

## 📖 Documentation & References

- [Streamlit Documentation](https://docs.streamlit.io)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [NLTK Documentation](https://www.nltk.org)
- [Mental Health Resources](https://www.samhsa.gov/find-help/national-helpline)

## 🤝 Contributing

This is an open project. Contributions are welcome! Areas for improvement:
- Additional emotion detection models
- Multi-language support
- Conversation persistence
- Advanced analytics
- Voice interface
- Mobile app version

## 📝 License

This project is provided as-is for educational and hackathon purposes. 

## 💙 Built With Care

MindCompanion was created with the belief that technology can be a compassionate, accessible tool for mental wellness. Every design decision prioritizes user wellbeing and safety.

If you use this project, please remember: **Your mental health matters. Reach out for professional help when you need it.**

---

**Questions or feedback?** Feel free to modify and adapt this project for your needs!

**Remember: Take care of yourself. You matter. 💙**
