import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime
from nlp_logic import NLPEngine
from persona_engine import PersonaEngine


# Page configuration
st.set_page_config(
    page_title="MindCompanion | Mental Health Support",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Futuristic Dark Theme CSS
custom_css = """
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    :root {
        --bg-primary: #0a0e27;
        --bg-secondary: #151b2f;
        --bg-tertiary: #1a2240;
        --text-primary: #e0e6ff;
        --text-secondary: #a0aac4;
        --neon-blue: #00d9ff;
        --neon-magenta: #ff006e;
        --neon-green: #00ff41;
        --neon-purple: #b000ff;
        --glass-light: rgba(255, 255, 255, 0.05);
        --glass-border: rgba(255, 255, 255, 0.1);
    }
    
    /* Main background */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMainBlockContainer"] {
        background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 50%, var(--bg-primary) 100%) !important;
        color: var(--text-primary) !important;
        font-family: 'Segoe UI', 'Courier New', monospace !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(21, 27, 47, 0.6) !important;
        backdrop-filter: blur(20px) !important;
        border-right: 1px solid var(--glass-border) !important;
    }
    
    /* Chat messages - User */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        flex-direction: row-reverse;
    }
    
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) > div > div:nth-child(2) {
        background: linear-gradient(135deg, rgba(0, 217, 255, 0.15), rgba(0, 217, 255, 0.05)) !important;
        color: var(--neon-blue) !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        border: 1px solid var(--glass-border) !important;
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.1) !important;
    }
    
    /* Chat messages - Assistant */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) > div > div:nth-child(2) {
        background: linear-gradient(135deg, rgba(176, 0, 255, 0.1), rgba(255, 0, 110, 0.05)) !important;
        color: var(--text-primary) !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        border: 1px solid var(--glass-border) !important;
        box-shadow: 0 0 20px rgba(255, 0, 110, 0.1) !important;
        border-left: 3px solid var(--neon-magenta) !important;
    }
    
    /* Avatars */
    [data-testid="chatAvatarIcon-assistant"] {
        background-color: var(--neon-magenta) !important;
        box-shadow: 0 0 15px var(--neon-magenta) !important;
    }
    
    [data-testid="chatAvatarIcon-user"] {
        background-color: var(--neon-blue) !important;
        box-shadow: 0 0 15px var(--neon-blue) !important;
    }
    
    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: var(--neon-blue) !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
    }
    
    p, span, label {
        color: var(--text-primary) !important;
    }
    
    /* Buttons */
    [data-testid="baseButton-primary"] {
        background: linear-gradient(135deg, var(--neon-blue), var(--neon-magenta)) !important;
        color: var(--bg-primary) !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.3) !important;
        border: none !important;
    }
    
    [data-testid="baseButton-primary"]:hover {
        box-shadow: 0 0 40px rgba(0, 217, 255, 0.6) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Metrics */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, rgba(0, 217, 255, 0.05), rgba(255, 0, 110, 0.05)) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: 8px !important;
        padding: 15px !important;
        box-shadow: 0 0 15px rgba(0, 217, 255, 0.1) !important;
    }
    
    /* Chat Input */
    [data-testid="stChatInputContainer"] input {
        background-color: rgba(21, 27, 47, 0.8) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        color: var(--text-primary) !important;
        caret-color: var(--neon-blue) !important;
    }
    
    [data-testid="stChatInputContainer"] input:focus {
        border-color: var(--neon-blue) !important;
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.2) !important;
        background-color: rgba(21, 27, 47, 0.95) !important;
    }
    
    /* Alerts and Info boxes */
    [data-testid="stAlert"] {
        background: linear-gradient(135deg, rgba(0, 217, 255, 0.1), rgba(0, 255, 65, 0.05)) !important;
        border-left: 4px solid var(--neon-green) !important;
        border-radius: 8px !important;
        border: 1px solid var(--glass-border) !important;
    }
    
    /* Expander */
    [data-testid="stExpander"] {
        border-radius: 8px !important;
        border: 1px solid var(--glass-border) !important;
        background: rgba(21, 27, 47, 0.4) !important;
    }
    
    [data-testid="stExpanderDetails"] {
        background: rgba(10, 14, 39, 0.4) !important;
    }
    
    /* Breathing animation */
    @keyframes breathe {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    @keyframes glow-pulse {
        0%, 100% { 
            box-shadow: 0 0 10px var(--neon-blue), inset 0 0 10px rgba(0, 217, 255, 0.2);
            opacity: 1;
        }
        50% { 
            box-shadow: 0 0 25px var(--neon-blue), inset 0 0 20px rgba(0, 217, 255, 0.3);
            opacity: 0.8;
        }
    }
    
    .breathe-circle {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--neon-blue), var(--neon-magenta));
        margin: 20px auto;
        animation: breathe 8s infinite;
        box-shadow: 0 0 20px var(--neon-blue);
    }
    
    /* Disclaimer */
    .disclaimer {
        background: linear-gradient(135deg, rgba(255, 0, 110, 0.1), rgba(255, 0, 110, 0.05)) !important;
        border-left: 4px solid var(--neon-magenta) !important;
        padding: 12px !important;
        border-radius: 4px !important;
        margin: 15px 0 !important;
        font-size: 12px !important;
        color: var(--text-secondary) !important;
        border: 1px solid var(--glass-border) !important;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 6px !important;
        height: 6px !important;
    }
    
    ::-webkit-scrollbar-track {
        background: transparent !important;
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(0, 217, 255, 0.3) !important;
        border-radius: 3px !important;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(0, 217, 255, 0.6) !important;
    }
    
    /* Container styling */
    [data-testid="column"] {
        background: transparent !important;
    }
    
    /* Text styling */
    a {
        color: var(--neon-blue) !important;
        text-decoration: none !important;
    }
    
    a:hover {
        color: var(--neon-magenta) !important;
        text-decoration: underline !important;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)


def initialize_session_state():
    """Initialize or restore session state variables."""
    if "nlp_engine" not in st.session_state:
        st.session_state.nlp_engine = NLPEngine()
    
    if "persona_engine" not in st.session_state:
        st.session_state.persona_engine = PersonaEngine()
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "emotion_history" not in st.session_state:
        st.session_state.emotion_history = []
    
    if "safety_mode" not in st.session_state:
        st.session_state.safety_mode = False
    
    if "session_start_time" not in st.session_state:
        st.session_state.session_start_time = datetime.now()


def render_sidebar():
    """Render the wellness dashboard sidebar."""
    with st.sidebar:
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(0, 217, 255, 0.08), rgba(255, 0, 110, 0.08)); border-radius: 8px; padding: 12px; margin-bottom: 16px; border: 1px solid rgba(0, 217, 255, 0.15);'>
            <h3 style='color: #00d9ff; margin: 0; letter-spacing: 2px; font-size: 14px;'>🧠 WELLNESS DASHBOARD</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Session stats with dark theme
        st.markdown("<p style='color: #a0aac4; font-size: 12px; letter-spacing: 1px; text-transform: uppercase;'>📊 SESSION METRICS</p>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                "Messages",
                len([m for m in st.session_state.messages if m["role"] == "user"]),
                delta=None
            )
        with col2:
            st.metric(
                "Session Time",
                f"{(datetime.now() - st.session_state.session_start_time).seconds // 60}m",
                delta=None
            )
        
        st.markdown("---")
        
        # Emotional trend with neon styling
        st.markdown("<p style='color: #00d9ff; font-size: 12px; letter-spacing: 1px; text-transform: uppercase;'>📊 EMOTIONAL TREND</p>", unsafe_allow_html=True)
        
        if st.session_state.emotion_history:
            dominant = st.session_state.nlp_engine.calculate_session_emotion(
                st.session_state.emotion_history
            )
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                <div style='text-align: center; background: linear-gradient(135deg, rgba(0, 217, 255, 0.1), rgba(255, 0, 110, 0.1)); padding: 15px; border-radius: 8px; border: 1px solid rgba(0, 217, 255, 0.2);'>
                    <h2 style='font-size: 32px; margin: 0;'>{dominant['emoji']}</h2>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                <div style='background: rgba(10, 14, 39, 0.4); padding: 12px; border-radius: 8px; border: 1px solid rgba(0, 217, 255, 0.1);'>
                    <p style='color: #a0aac4; font-size: 11px; margin: 0; text-transform: uppercase; letter-spacing: 1px;'>Current State</p>
                    <p style='color: #00d9ff; font-size: 14px; font-weight: 600; margin: 4px 0;'>{dominant['dominant_emotion'].title()}</p>
                    <p style='color: #a0aac4; font-size: 11px; margin: 0; text-transform: uppercase; letter-spacing: 1px;'>Trend: {dominant['trend'].title()}</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Emotion trend chart
            if len(st.session_state.emotion_history) > 1:
                chart_data = st.session_state.nlp_engine.get_emotion_history_for_chart(
                    st.session_state.emotion_history
                )
                
                df_chart = pd.DataFrame(chart_data)
                emotion_values = {
                    "sadness": 1, "fear": 2, "anger": 2.5, "neutral": 3,
                    "surprise": 3.5, "love": 4.5, "joy": 5
                }
                
                df_chart["emotion_score"] = df_chart["emotion"].map(emotion_values)
                
                chart = alt.Chart(df_chart).mark_line(point=True, color="#00d9ff", size=3).encode(
                    x=alt.X("interaction:Q", title="Interaction #"),
                    y=alt.Y("emotion_score:Q", scale=alt.Scale(domain=[0, 5.5]), title="Mood Score"),
                    tooltip=["interaction:Q", "emotion:N", "score:Q"],
                    color=alt.value("#00d9ff")
                ).properties(
                    height=200,
                    width=300
                ).interactive()
                
                st.altair_chart(chart, use_container_width=True, theme=None)
        else:
            st.info("📈 Your emotional trend will appear as we chat. Start sharing to see your pattern.")
        
        st.markdown("---")
        
        # Guided breathing
        st.markdown("<p style='color: #00ff41; font-size: 12px; letter-spacing: 1px; text-transform: uppercase;'>🫁 GUIDED BREATHING</p>", unsafe_allow_html=True)
        breathing_enabled = st.checkbox("Enable Breathing Guide", value=False)
        
        if breathing_enabled:
            st.markdown("""
            <div style='background: rgba(0, 255, 65, 0.05); border-left: 3px solid #00ff41; padding: 12px; border-radius: 6px; border: 1px solid rgba(0, 255, 65, 0.1);'>
                <p style='color: #00ff41; margin: 0 0 8px 0; font-weight: 600; font-size: 12px;'>4-7-8 BREATHING EXERCISE</p>
                <p style='color: #a0aac4; margin: 0; font-size: 11px;'>A calming technique to reduce anxiety and stress</p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("""
                <div style='text-align: center; background: rgba(0, 217, 255, 0.08); padding: 12px; border-radius: 6px; border: 1px solid rgba(0, 217, 255, 0.15);'>
                    <p style='color: #00d9ff; margin: 0; font-size: 12px; font-weight: 600;'>Breathe In</p>
                    <p style='color: #a0aac4; margin: 4px 0 0 0; font-size: 16px;'>4s</p>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown("""
                <div style='text-align: center; background: rgba(255, 0, 110, 0.08); padding: 12px; border-radius: 6px; border: 1px solid rgba(255, 0, 110, 0.15);'>
                    <p style='color: #ff006e; margin: 0; font-size: 12px; font-weight: 600;'>Hold</p>
                    <p style='color: #a0aac4; margin: 4px 0 0 0; font-size: 16px;'>7s</p>
                </div>
                """, unsafe_allow_html=True)
            with col3:
                st.markdown("""
                <div style='text-align: center; background: rgba(0, 255, 65, 0.08); padding: 12px; border-radius: 6px; border: 1px solid rgba(0, 255, 65, 0.15);'>
                    <p style='color: #00ff41; margin: 0; font-size: 12px; font-weight: 600;'>Exhale</p>
                    <p style='color: #a0aac4; margin: 4px 0 0 0; font-size: 16px;'>8s</p>
                </div>
                """, unsafe_allow_html=True)
            
            if st.button("▶️ Start 1-Minute Session"):
                st.info("🌬️ Close your eyes. Breathe in for 4 seconds... Hold for 7... Exhale for 8. Repeat 5 times. You're doing great! 💙")
        
        st.markdown("---")
        
        # Quick resources
        with st.expander("🆘 Quick Resources"):
            st.markdown("""
            <div style='color: #a0aac4; font-size: 12px;'>
                <p style='margin: 0 0 12px 0; color: #00d9ff; font-weight: 600;'>If you're in crisis, reach out immediately:</p>
                
                <p style='margin: 8px 0; color: #ff006e;'><strong>🇺🇸 National Suicide Prevention Lifeline</strong></p>
                <p style='margin: 0 0 8px 0;'>📞 <strong style="color: #00d9ff;">988</strong> | 💻 suicidepreventionlifeline.org</p>
                
                <p style='margin: 8px 0; color: #00ff41;'><strong>📱 Crisis Text Line</strong></p>
                <p style='margin: 0 0 8px 0;'>Text <strong style="color: #00d9ff;">HOME</strong> to <strong style="color: #00d9ff;">741741</strong></p>
                
                <p style='margin: 8px 0; color: #b000ff;'><strong>🌍 International</strong></p>
                <p style='margin: 0;'>https://www.iasp.info/resources/Crisis_Centres/</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Disclaimer with dark theme
        st.markdown("""
        <div class='disclaimer'>
        ⚠️ <strong>IMPORTANT DISCLAIMER:</strong> MindCompanion is an AI tool designed for emotional support and wellness, not medical treatment. 
        If you're experiencing a mental health crisis or suicidal thoughts, please contact a mental health professional or crisis service immediately.
        </div>
        """, unsafe_allow_html=True)


def render_safety_mode():
    """Render the safety mode interface for crisis situations."""
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(255, 0, 110, 0.2), rgba(255, 0, 110, 0.1)); border-left: 4px solid #ff006e; padding: 20px; border-radius: 8px; margin: 20px 0; border: 1px solid rgba(255, 0, 110, 0.3);'>
        <h2 style='color: #ff006e; margin: 0 0 15px 0; letter-spacing: 2px;'>🆘 SAFETY MODE ACTIVATED</h2>
        <p style='color: #e0e6ff; margin: 10px 0; font-size: 14px;'>
            I'm concerned about your wellbeing. You deserve professional support right now, and I want to connect you with someone who can help.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background: rgba(0, 217, 255, 0.08); border-radius: 8px; padding: 16px; border: 1px solid rgba(0, 217, 255, 0.15);'>
            <h3 style='color: #00d9ff; margin: 0 0 12px 0;'>📞 Talk to Someone Now</h3>
            
            <p style='color: #a0aac4; margin: 0 0 8px 0; font-weight: 600;'><span style='color: #00ff41;'>●</span> National Suicide Prevention Lifeline (US)</p>
            <p style='color: #a0aac4; margin: 0 0 8px 0;'>☎️ Call <span style='color: #00d9ff;'><strong>988</strong></span> (available 24/7)</p>
            <p style='color: #a0aac4; margin: 0 0 12px 0;'>🌐 suicidepreventionlifeline.org</p>
            
            <p style='color: #a0aac4; margin: 0 0 8px 0; font-weight: 600;'><span style='color: #ff006e;'>●</span> Crisis Text Line</p>
            <p style='color: #a0aac4; margin: 0;'>📱 Text <span style='color: #00d9ff;'><strong>HOME</strong></span> to <span style='color: #00d9ff;'><strong>741741</strong></span></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: rgba(0, 255, 65, 0.08); border-radius: 8px; padding: 16px; border: 1px solid rgba(0, 255, 65, 0.15);'>
            <h3 style='color: #00ff41; margin: 0 0 12px 0;'>🏥 Immediate Help</h3>
            
            <p style='color: #a0aac4; margin: 0 0 8px 0;'>If you're in immediate danger:</p>
            
            <p style='color: #a0aac4; margin: 0 0 6px 0;'><span style='color: #ff006e;'>●</span> Call <span style='color: #00d9ff;'><strong>911</strong></span> (or your local emergency number)</p>
            <p style='color: #a0aac4; margin: 0 0 6px 0;'><span style='color: #ff006e;'>●</span> Go to the <span style='color: #00d9ff;'><strong>nearest emergency room</strong></span></p>
            <p style='color: #a0aac4; margin: 0 0 12px 0;'><span style='color: #ff006e;'>●</span> Call a <span style='color: #00d9ff;'><strong>trusted family member or friend</strong></span></p>
            
            <p style='color: #00ff41; margin: 0 0 4px 0; font-weight: 600;'>Remember:</p>
            <p style='color: #a0aac4; margin: 0; font-style: italic;'>Your life has value. This moment is temporary. Help is available right now.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div style='color: #a0aac4; background: rgba(176, 0, 255, 0.05); padding: 16px; border-radius: 8px; border: 1px solid rgba(176, 0, 255, 0.1);'>
        <p style='margin: 0;'>I'm here for you, but I also know my limitations. The professionals on the other end of these lines are trained to help in ways I simply cannot.</p>
        <p style='margin: 8px 0 0 0; color: #ff006e; font-weight: 600;'>Will you reach out to one of these resources right now? You deserve support from someone who can truly understand the depth of what you're experiencing.</p>
    </div>
    """, unsafe_allow_html=True)


def render_chat_interface():
    """Render the main chat interface."""
    # Display safety mode if activated
    if st.session_state.safety_mode:
        render_safety_mode()
        st.markdown("---")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=message.get("avatar")):
            st.markdown(message["content"])
    
    # Chat input
    user_input = st.chat_input(
        placeholder="Share what's on your mind... I'm listening. 💙",
        disabled=False
    )
    
    if user_input:
        # Add user message to history
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "avatar": "👤"
        })
        
        # Detect emotion
        emotion_result = st.session_state.nlp_engine.detect_emotion(user_input)
        st.session_state.emotion_history.append(emotion_result)
        
        # Keep only last 5 interactions for crisis detection
        if len(st.session_state.emotion_history) > 5:
            st.session_state.emotion_history = st.session_state.emotion_history[-5:]
        
        # Detect crisis keywords
        crisis_data = st.session_state.nlp_engine.detect_crisis_keywords(user_input)
        
        # Activate safety mode if critical crisis detected
        if crisis_data["is_crisis"] and crisis_data["severity"] in ["critical", "severe"]:
            st.session_state.safety_mode = True
        
        # Check for escalation pattern (3+ consecutive negative emotions)
        if len(st.session_state.emotion_history) >= 3:
            recent_emotions = [e["emotion"] for e in st.session_state.emotion_history[-3:]]
            negative_emotions = ["sadness", "anger", "fear"]
            if all(e in negative_emotions for e in recent_emotions):
                st.session_state.safety_mode = True
        
        # Generate AI response
        ai_response = st.session_state.persona_engine.generate_response(
            user_message=user_input,
            emotion=emotion_result["emotion"],
            crisis_data=crisis_data if crisis_data["is_crisis"] else None
        )
        
        # Add AI message to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": ai_response,
            "avatar": "🤖"
        })
        
        # Rerun to display new messages
        st.rerun()


def main():
    """Main application entry point."""
    initialize_session_state()
    
    # Futuristic Header with gradient
    st.markdown("""
    <div style='text-align: center; padding: 25px 0; background: linear-gradient(135deg, rgba(0, 217, 255, 0.1), rgba(255, 0, 110, 0.1)); border-radius: 12px; margin-bottom: 20px; border: 1px solid rgba(0, 217, 255, 0.2);'>
        <h1 style='color: #00d9ff; margin: 0; letter-spacing: 3px; font-size: 36px; text-shadow: 0 0 20px rgba(0, 217, 255, 0.4);'>🧠 MindCompanion</h1>
        <p style='color: #a0aac4; font-size: 16px; margin: 8px 0 0 0; letter-spacing: 2px; font-weight: 300;'>Neural Mental Wellness Companion</p>
        <div style='margin-top: 12px; display: flex; justify-content: center; gap: 12px;'>
            <span style='width: 8px; height: 8px; background: #00ff41; border-radius: 50%; box-shadow: 0 0 10px #00ff41;'></span>
            <span style='color: #a0aac4; font-size: 12px; font-family: Courier New;'>SYSTEM ONLINE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Main content layout
    render_sidebar()
    render_chat_interface()
    
    # Futuristic Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; background: linear-gradient(135deg, rgba(0, 217, 255, 0.05), rgba(255, 0, 110, 0.05)); border: 1px solid rgba(0, 217, 255, 0.1); border-radius: 8px; padding: 15px; color: #a0aac4; font-size: 12px;'>
        <p style='margin: 0 0 8px 0;'>MindCompanion provides emotional support, not medical treatment. For mental health crises, please contact a professional or crisis line immediately.</p>
        <p style='margin: 0; letter-spacing: 1px;'>💙 Take care of yourself. You matter.</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
