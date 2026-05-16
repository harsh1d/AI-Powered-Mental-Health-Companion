# ⚙️ Configuration & Customization Guide

This guide explains how to customize MindCompanion to fit your specific needs.

## 1. Customizing Response Templates

### Location
`persona_engine.py` → `PersonaEngine.__init__()` → `self.response_templates`

### Structure
Each emotion has three components:
```python
"emotion_name": {
    "opening": [list of opening lines],
    "validation": [list of validating statements],
    "offering": [list of supportive offers]
}
```

### Example: Adding a Custom Sadness Response

Find the sadness section in `persona_engine.py`:
```python
"sadness": {
    "opening": [
        "That sounds really heavy, and I'm truly glad you shared it with me.",
        # Add your custom line here:
        "I can see this is weighing on your heart, and I'm honored you trust me with it.",
        ...
    ],
    ...
}
```

The engine randomly selects from these lists for variety.

### Example: Modifying Anxiety Coping Strategies

In `persona_engine.py`, find the anxiety coping dictionary:
```python
"anxiety": {
    ...
    "coping": {
        "breathing_exercise": """Your custom breathing guide here""",
        "grounding_5_senses": """Your custom grounding technique here"""
    }
}
```

Add a new strategy:
```python
"coping": {
    "breathing_exercise": "...",
    "grounding_5_senses": "...",
    "progressive_relaxation": """**Progressive Muscle Relaxation**
    
    1. Tense your toes for 5 seconds
    2. Release and notice the relief
    3. Move up through your body...
    """
}
```

Then update the selection logic in `generate_response()`:
```python
coping_choice = random.choice([
    templates["coping"]["breathing_exercise"],
    templates["coping"]["grounding_5_senses"],
    templates["coping"]["progressive_relaxation"]  # Add this
])
```

---

## 2. Customizing Crisis Keywords

### Location
`nlp_logic.py` → `NLPEngine.__init__()` → `self.crisis_keywords`

### Structure
```python
self.crisis_keywords = {
    "critical": [severe crisis keywords],
    "severe": [serious concern keywords],
    "moderate": [concerning pattern keywords]
}
```

### Example: Adding New Crisis Keywords

```python
self.crisis_keywords = {
    "critical": [
        "suicide", "kill myself", "hang myself",
        # Add new critical keywords:
        "take my life", "end this", "not worth living"
    ],
    "severe": [
        "self-harm", "hurt myself",
        # Add new severe keywords:
        "destructive", "self-punish"
    ],
    "moderate": [
        "anxious", "panic",
        # Add new moderate keywords:
        "stressed out", "can't cope"
    ]
}
```

### Example: Adding Domain-Specific Keywords

If targeting a specific audience (e.g., students), add relevant keywords:

```python
# Add to "moderate" section:
"academic pressure", "failing my classes", "can't handle school"

# Add to "severe" section:
"academic burnout", "failing college", "dropped out"
```

---

## 3. Customizing UI Colors & Design

### Location
`app.py` → `custom_css` variable

### Current Color Scheme
- **Primary Blue**: `#5DADE2` (calm, supportive)
- **Success Green**: `#52D273` (positive, user messages)
- **Background**: Gradient `#F5F9FF` to `#E8F4F8` (soft, soothing)

### Example: Warmer Color Scheme

Replace the CSS gradient:
```css
/* Current cool tones */
background: linear-gradient(135deg, #F5F9FF 0%, #E8F4F8 100%);

/* New warm tones */
background: linear-gradient(135deg, #FFF5E6 0%, #FFE8D6 100%);
```

Update primary color:
```python
# Current
<strong style='color: #5DADE2;'>

# New warm orange
<strong style='color: #FF9F43;'>
```

### Example: Dark Mode Theme

```css
html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
    color: #E8E8E8;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d0d0d 0%, #1a1a1a 100%);
    border-right: 2px solid #333333;
}
```

### Example: Changing Chat Bubble Colors

```css
/* User message (currently green) */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) > div > div:nth-child(2) {
    background-color: #3498DB;  /* Blue instead of green */
    color: white;
}

/* AI message (currently light blue) */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) > div > div:nth-child(2) {
    background-color: #ECF0F1;  /* Light gray instead of light blue */
    color: #2C3E50;
    border-left: 3px solid #3498DB;
}
```

---

## 4. Customizing Emotion Detection

### Location
`nlp_logic.py` → `NLPEngine.__init__()` → `self.emotion_map`

### Current Emotion Mapping
```python
self.emotion_map = {
    "sadness": {"emoji": "😢", "color": "#4A90E2"},
    "joy": {"emoji": "😊", "color": "#52D273"},
    # ... etc
}
```

### Example: Changing Emojis

```python
self.emotion_map = {
    "sadness": {"emoji": "🥀", "color": "#4A90E2"},      # rose instead of tear
    "joy": {"emoji": "✨", "color": "#52D273"},           # sparkles instead of smile
    "anger": {"emoji": "⚡", "color": "#FF5252"},         # lightning instead of angry face
    "fear": {"emoji": "🌪️", "color": "#FFB84D"},         # tornado instead of scared face
}
```

---

## 5. Customizing Session Emotion Tracking

### Location
`nlp_logic.py` → `NLPEngine.calculate_session_emotion()`

### Current Logic
- Tracks last 5 interactions
- Determines dominant emotion by frequency
- Analyzes trend (improving/declining/stable)

### Example: Longer History Window

```python
# In app.py, change:
if len(st.session_state.emotion_history) > 5:
    st.session_state.emotion_history = st.session_state.emotion_history[-5:]

# To:
if len(st.session_state.emotion_history) > 10:  # Track 10 instead of 5
    st.session_state.emotion_history = st.session_state.emotion_history[-10:]
```

### Example: Custom Trend Analysis

Replace the trend calculation in `calculate_session_emotion()`:

```python
# Current simple trend
if last_emotion == "joy" or last_emotion == "love":
    trend = "improving"

# New: Track mood improvement score
mood_values = {"joy": 5, "love": 5, "surprise": 3.5, "neutral": 3, "fear": 2, "anger": 2, "sadness": 1}
recent_mood_scores = [mood_values.get(e.get("emotion"), 3) for e in session_emotions[-3:]]

if len(recent_mood_scores) >= 2:
    if recent_mood_scores[-1] > recent_mood_scores[0] + 0.5:
        trend = "improving"
    elif recent_mood_scores[-1] < recent_mood_scores[0] - 0.5:
        trend = "declining"
    else:
        trend = "stable"
```

---

## 6. Customizing Sidebar Dashboard

### Location
`app.py` → `render_sidebar()` function

### Example: Adding a New Dashboard Widget

```python
def render_sidebar():
    with st.sidebar:
        st.markdown("# 🧠 Your Wellness Dashboard")
        st.markdown("---")
        
        # Existing widgets...
        
        # NEW: Add gratitude tracker
        st.markdown("### 🙏 Today's Gratitude")
        gratitude = st.text_area("What are you grateful for today?")
        if st.button("Save"):
            st.success("Gratitude saved! 💙")
```

### Example: Custom Chart Colors

In `render_sidebar()`, modify the Altair chart:

```python
chart = alt.Chart(df_chart).mark_line(
    point=True,
    color="#FF6B6B",  # Change from blue to red
    size=3            # Make line thicker
).encode(
    x=alt.X("interaction:Q", title="Interaction #"),
    y=alt.Y("emotion_score:Q", scale=alt.Scale(domain=[0, 5.5]), title="Mood"),
)
```

---

## 7. Customizing Safety Mode

### Location
`app.py` → `render_safety_mode()` function

### Example: Adding Custom Crisis Resources

```python
st.markdown("""
    ### 🌍 Regional Resources
    
    **For Asia-Pacific Region:**
    - 🇮🇳 India: AASRA 9820466726
    - 🇦🇺 Australia: Lifeline 13 11 14
    - 🇯🇵 Japan: TELL 03-5774-0992
    
    **For Europe:**
    - 🇬🇧 UK: Samaritans 116 123
    - 🇩🇪 Germany: Teleseelsorge 0800-111 0 111
""")
```

---

## 8. Customizing Follow-up Questions

### Location
`persona_engine.py` → `PersonaEngine.generate_follow_up()` function

### Example: Adding Custom Follow-ups

```python
follow_ups = {
    "sadness": [
        "Is there someone in your life you feel comfortable talking to about this?",
        "What's one small thing that usually brings you a bit of comfort?",
        # Add custom follow-up:
        "What would help you feel just a little bit better right now?",
        "Have you been able to take care of yourself today?",
    ],
    # ... rest of emotions
}
```

---

## 9. Advanced: Using a Different Emotion Model

### Current Model
`bhadresh-savani/distilbert-base-uncased-emotion` (lightweight, CPU-friendly)

### Alternative Models
```python
# More accurate but slower:
# "j-hartmann/emotion-english-distilroberta-base"

# For specific domains:
# "facebook/bart-large-mnli"  # for zero-shot classification

# Simple rule-based (no model):
# Custom implementation using keyword matching
```

### Example: Using Different Model

In `nlp_logic.py`:
```python
self.emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",  # More accurate model
    framework="pt"
)
```

---

## 10. Advanced: Custom Coping Strategies

### Adding Interactive Coping Exercises

In `app.py`, add to sidebar:

```python
if st.sidebar.checkbox("🎵 Music Therapy"):
    st.sidebar.markdown("""
    **Calming Music Recommendations:**
    - Ambient: Brian Eno - "Music for Airports"
    - Nature sounds: Rain, ocean waves
    - Classical: Debussy - "Clair de Lune"
    """)
    if st.sidebar.button("Open Spotify"):
        st.sidebar.info("Search for 'Calm' or 'Sleep' playlists")
```

---

## 11. Configuration Best Practices

1. **Test changes locally first** before deploying
2. **Keep backups** of original files
3. **Use version control** (Git) to track changes
4. **Document custom changes** in comments
5. **Test edge cases** after modifications
6. **Monitor crisis detection** to prevent false positives/negatives

---

## 12. Quick Reference: File Locations

| What to Customize | File | Function/Section |
|------------------|------|------------------|
| Response text | `persona_engine.py` | `response_templates` |
| Crisis keywords | `nlp_logic.py` | `crisis_keywords` |
| Colors/UI | `app.py` | `custom_css` |
| Dashboard | `app.py` | `render_sidebar()` |
| Safety Mode | `app.py` | `render_safety_mode()` |
| Follow-up questions | `persona_engine.py` | `generate_follow_up()` |
| Emojis/emotions | `nlp_logic.py` | `emotion_map` |

---

## Need More Help?

- Check the main `README.md` for architecture details
- Review inline code comments
- Test changes with `test_components.py`
- Refer to Streamlit docs: https://docs.streamlit.io

**Remember: Always prioritize user safety when customizing crisis detection!** 💙
