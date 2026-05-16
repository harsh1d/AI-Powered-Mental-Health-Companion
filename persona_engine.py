import random
from typing import Dict, List


class PersonaEngine:
    """
    Generates deeply empathetic, contextual responses based on detected emotion.
    Avoids toxic positivity and provides actionable coping strategies.
    """
    
    def __init__(self):
        """Initialize response templates and coping strategies."""
        self.response_templates = {
            "sadness": {
                "opening": [
                    "That sounds really heavy, and I'm truly glad you shared it with me.",
                    "It's clear you're carrying something difficult right now. Thank you for trusting me with this.",
                    "I hear you, and what you're describing sounds genuinely painful.",
                    "That must feel so isolating. I want you to know you're not alone in this.",
                    "It's okay to feel this way. Your emotions are valid, and I'm here to listen."
                ],
                "validation": [
                    "Sadness is a natural response to loss, disappointment, or struggle.",
                    "What you're feeling is a completely human response to your circumstances.",
                    "It takes courage to acknowledge and share difficult emotions like this.",
                    "Your pain is real, and you deserve compassion—especially from yourself.",
                    "Processing these feelings is an important part of healing."
                ],
                "offering": [
                    "I'm here with you. Would you like to talk about what's contributing most to these feelings?",
                    "Sometimes just naming what hurts can feel a little lighter. I'm listening.",
                    "Would it help to explore what small things might bring you a sense of comfort today?",
                    "If you'd like, we could work through some gentle strategies together.",
                    "You don't have to have it all figured out. Let's take this one moment at a time."
                ]
            },
            "anxiety": {
                "opening": [
                    "Anxiety can feel all-consuming, and I appreciate you telling me about it.",
                    "That sounds like a lot of worry on your mind. You're not alone in this.",
                    "Anxiety has a way of making everything feel urgent and overwhelming. I hear you.",
                    "Your concerns matter, and it's good that you're expressing them.",
                    "I can sense the tension in what you're sharing. Let's work through this together."
                ],
                "validation": [
                    "Anxiety is your mind's way of trying to protect you, even if it doesn't always feel helpful.",
                    "The worry you're experiencing is real, and your nervous system is responding to genuine concerns.",
                    "It's completely understandable to feel anxious about these things.",
                    "Many people experience what you're describing—you're not broken or weak.",
                    "Anxiety often feels uncontrollable, but there are tools that can help."
                ],
                "offering": [
                    "Let me share a grounding technique that many find helpful: the 4-7-8 breathing exercise.",
                    "Would you like to try a simple breathing exercise together right now?",
                    "Sometimes breaking down our worries into smaller, manageable pieces helps.",
                    "Let's identify what's truly in your control and what isn't—that can ease some of the overwhelm.",
                    "Would it help to talk through a specific worry that's been on your mind?"
                ],
                "coping": {
                    "breathing_exercise": """
**4-7-8 Breathing Exercise:**
This technique helps calm your nervous system. Try this now:

1. **Breathe in** through your nose for a count of 4
2. **Hold** your breath for a count of 7
3. **Exhale slowly** through your mouth for a count of 8

Repeat this 4-5 times. The extended exhale signals safety to your body.

Remember: Your breath is always with you. Use it as an anchor when anxiety rises.
                    """,
                    "grounding_5_senses": """
**5-4-3-2-1 Grounding Technique:**
When anxiety feels overwhelming, use your senses to return to the present moment:

- **5 things** you can see (name them)
- **4 things** you can physically feel (texture, temperature)
- **3 things** you can hear
- **2 things** you can smell
- **1 thing** you can taste

This brings you back to NOW, not to worry.
                    """
                }
            },
            "anger": {
                "opening": [
                    "Your anger is telling you something important. I'm listening.",
                    "It sounds like something has really violated your sense of fairness or respect.",
                    "Anger often arises when we feel unheard or wronged. That's valid.",
                    "I can hear the intensity in what you're expressing. Let's talk about it.",
                    "Your frustration is real, and it deserves to be acknowledged."
                ],
                "validation": [
                    "Anger isn't something to be ashamed of—it's a signal that something matters to you.",
                    "What you're angry about likely makes sense given your perspective and experiences.",
                    "Righteous anger can be fuel for positive change, even if it feels chaotic right now.",
                    "Your feelings are valid, even if the situation feels unfair or unjust.",
                    "Anger is one of the most honest emotions—it shows what you truly care about."
                ],
                "offering": [
                    "Let's explore what specifically triggered this anger. Sometimes understanding helps.",
                    "What would feel fair or just to you in this situation?",
                    "Would it help to talk about how you'd like to express this anger constructively?",
                    "Channel this energy: sometimes writing, movement, or creating something can transform anger.",
                    "What boundary or value of yours feels violated right now?"
                ]
            },
            "fear": {
                "opening": [
                    "Fear often protects us, but it can also paralyze us. Thank you for sharing this.",
                    "What you're afraid of feels very real to you, and that matters.",
                    "Fear is a natural response to uncertainty or threat. You're not weak for feeling it.",
                    "I hear the worry underneath what you're sharing.",
                    "Fear tells us something feels uncertain or unsafe. Let's explore that together."
                ],
                "validation": [
                    "Many people feel fear about similar things. You're not alone.",
                    "Fear often presents the worst-case scenario as certainty. That's how it works.",
                    "Your fear is a sign you care about outcomes and your wellbeing.",
                    "It's completely human to fear loss, failure, or the unknown.",
                    "What you're afraid of touches something deeply important to you."
                ],
                "offering": [
                    "Let's separate fact from fear. What's actually likely vs. what feels possible?",
                    "What's one small step you could take to feel a bit more in control?",
                    "Sometimes naming our fears makes them less monstrous. Want to try?",
                    "What would help you feel safer right now?",
                    "Would planning for a few scenarios—even worst-case—help ease the uncertainty?"
                ]
            },
            "joy": {
                "opening": [
                    "I love that you're experiencing joy! That's wonderful.",
                    "Something positive is happening, and I'm genuinely glad for you.",
                    "Your happiness is contagious. Tell me more about what's bringing you joy.",
                    "This is a beautiful moment. Let's sit with it for a bit.",
                    "Your enthusiasm is lifting, and that's genuinely good to see."
                ],
                "validation": [
                    "Joy and happiness are affirmations that you've found something meaningful.",
                    "It's wonderful that you're experiencing these positive emotions.",
                    "Celebrating the good moments is as important as processing the hard ones.",
                    "Your capacity for joy shows your resilience and openness to life.",
                    "This happiness is deserved and real—hold onto it."
                ],
                "offering": [
                    "What are you most grateful for right now?",
                    "How can you extend or share this good feeling?",
                    "Let's hold this moment. What would help you remember it during harder times?",
                    "What does this joy tell you about what matters most to you?",
                    "Who would you like to share this happiness with?"
                ]
            },
            "neutral": {
                "opening": [
                    "I'm here and listening, whatever you're experiencing.",
                    "Let's talk. I'm genuinely interested in what's on your mind.",
                    "It's okay to feel 'fine'—not everything needs to be intense.",
                    "How are you really doing today?",
                    "I'm here for the everyday moments too, not just the difficult ones."
                ],
                "validation": [
                    "Sometimes neutral is exactly where we need to be.",
                    "It's perfectly okay to feel steady and stable.",
                    "Not every day brings big emotions, and that's healthy.",
                    "You can process things at your own pace."
                ],
                "offering": [
                    "What's something on your mind today, however small?",
                    "Is there anything you'd like to explore or talk through?",
                    "How can I support you, even in the quieter moments?",
                    "Would you like to talk about something specific, or just check in?",
                    "What would feel good for you right now?"
                ]
            },
            "love": {
                "opening": [
                    "That warmth you're feeling—hold onto it. It's beautiful.",
                    "Love and connection are among life's greatest gifts. I'm glad you're experiencing that.",
                    "What a wonderful emotion to share with me.",
                    "Your capacity for love and connection says something beautiful about who you are.",
                    "The affection in what you're describing is really moving."
                ],
                "validation": [
                    "Love is one of the most meaningful things we can experience.",
                    "Your ability to feel and express love is a strength.",
                    "Connection and affection are fundamental to human wellbeing.",
                    "This love you're feeling is real and important.",
                    "Being open to love takes courage and hope."
                ],
                "offering": [
                    "Tell me more about the people or things you love.",
                    "How do you express this love in ways that feel authentic?",
                    "What does this love bring out in you?",
                    "How can you nurture these connections that matter so much?",
                    "Is there a way you'd like to deepen or celebrate these connections?"
                ]
            }
        }
    
    def generate_response(
        self,
        user_message: str,
        emotion: str,
        crisis_data: Dict = None
    ) -> str:
        """
        Generate a contextual, empathetic response based on emotion and crisis status.
        
        Args:
            user_message: The user's input
            emotion: Detected emotion (from emotion classifier)
            crisis_data: Dict with crisis severity and keywords (optional)
        
        Returns:
            A warm, empathetic response string
        """
        # Emergency protocol for critical crisis
        if crisis_data and crisis_data.get("severity") == "critical":
            return self._generate_crisis_response(user_message, crisis_data)
        
        # Emergency protocol for severe crisis
        if crisis_data and crisis_data.get("severity") == "severe":
            return self._generate_severe_response(user_message, crisis_data)
        
        # Normalize emotion to match templates
        emotion = emotion.lower()
        if emotion not in self.response_templates:
            emotion = "neutral"
        
        templates = self.response_templates[emotion]
        
        response = ""
        response += random.choice(templates["opening"]) + "\n\n"
        response += random.choice(templates["validation"]) + "\n\n"
        response += random.choice(templates["offering"])
        
        # Add coping strategies for anxiety
        if emotion == "anxiety":
            coping_choice = random.choice([
                templates["coping"]["breathing_exercise"],
                templates["coping"]["grounding_5_senses"]
            ])
            response += "\n\n" + coping_choice
        
        return response
    
    def _generate_crisis_response(self, user_message: str, crisis_data: Dict) -> str:
        """
        Generate response for critical crisis situations (suicidal ideation, severe self-harm intent).
        """
        crisis_keywords = ", ".join(crisis_data.get("keywords_found", [])[:3])
        
        response = f"""
🆘 **I'm truly concerned about your safety, and I want to help immediately.**

What you've shared with me suggests you're in significant distress. I'm not equipped to provide the professional intervention you need right now, but there are people who are, and they're ready to help.

**Please reach out to a crisis professional right now:**

**National Suicide Prevention Lifeline (US)**
📞 **988** (Call or Text)
💻 **suicidepreventionlifeline.org**

**Crisis Text Line**
📱 Text **HOME** to **741741**

**International Association for Suicide Prevention**
🌐 **https://www.iasp.info/resources/Crisis_Centres/**

---

**What happens next:**
- These counselors are trained, compassionate, and available 24/7
- You can be honest with them—nothing shocks them
- They're there to listen and help you find a path forward
- Your safety and wellbeing matter deeply

**If you're in immediate danger:**
🚨 **Call 911 or go to your nearest emergency room**

---

I'm here with you in this moment, and I want you to know: **You are not alone. Your life has value. What you're feeling right now can change with the right support.**

Will you reach out to one of these resources right now? I'm here with you through this.
        """
        
        return response.strip()
    
    def _generate_severe_response(self, user_message: str, crisis_data: Dict) -> str:
        """
        Generate response for severe crisis (self-harm, dark ideation).
        """
        response = f"""
**I hear how much you're hurting, and I'm genuinely concerned.**

What you've described suggests you're going through a really dark time, and this is bigger than I can fully support alone. You deserve real, human professional support right now.

**Please reach out to a mental health professional or crisis service:**

**National Suicide Prevention Lifeline (US)** - 988
**Crisis Text Line** - Text HOME to 741741
**International Crisis Lines** - https://www.iasp.info/resources/Crisis_Centres/

---

**What I want you to know:**
- You don't have to navigate this alone
- What you're feeling right now is temporary, even if it doesn't feel that way
- Professional counselors can offer tools and perspectives that genuinely help
- Your pain is valid, and so is your right to feel better

**In the immediate moment:**
Take one small step: Call or text a crisis line. They're there specifically for moments like this, and talking to someone can help.

I'm here with you, and I care about your safety. Will you reach out to someone who can provide the level of support you truly deserve?
        """
        
        return response.strip()
    
    def generate_follow_up(self, emotion: str, conversation_turn: int) -> str:
        """
        Generate follow-up prompts to deepen conversation naturally.
        """
        follow_ups = {
            "sadness": [
                "Is there someone in your life you feel comfortable talking to about this?",
                "What's one small thing that usually brings you a bit of comfort?",
                "When did these feelings start to become this heavy?"
            ],
            "anxiety": [
                "What's the thing that worries you most about this situation?",
                "Have you faced similar situations before? How did you get through?",
                "What would help you feel even slightly more in control?"
            ],
            "anger": [
                "What's one thing that would feel like a just outcome?",
                "Is there someone you need to express this to?",
                "What boundary do you need to set here?"
            ],
            "fear": [
                "What's the worst thing you're afraid might happen?",
                "What's something you've survived before that felt scary at the time?",
                "What would make you feel safer right now?"
            ],
            "joy": [
                "How does this moment compare to other happy times in your life?",
                "What would make this feeling last even longer?",
                "Who else deserves to experience this joy with you?"
            ],
            "neutral": [
                "Is there anything beneath the surface you haven't mentioned yet?",
                "How are you taking care of yourself lately?",
                "What's been on your mind more than usual?"
            ],
            "love": [
                "How do you express this love in your daily life?",
                "What makes this connection so special?",
                "How has this relationship changed you?"
            ]
        }
        
        emotion = emotion.lower()
        if emotion not in follow_ups:
            emotion = "neutral"
        
        return random.choice(follow_ups[emotion])
