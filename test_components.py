#!/usr/bin/env python
"""
Quick start script to verify all components work before launching the app.
"""

def test_nlp_engine():
    """Test NLP engine functionality."""
    print("\n🧠 Testing NLP Engine...")
    from nlp_logic import NLPEngine
    
    engine = NLPEngine()
    print("  ✓ NLPEngine initialized")
    
    # Test emotion detection
    test_cases = [
        ("I feel very sad today", "sadness"),
        ("I'm so happy and excited!", "joy"),
        ("I'm really worried about this", "fear"),
        ("This makes me so angry!", "anger"),
    ]
    
    for text, expected_emotion in test_cases:
        result = engine.detect_emotion(text)
        emotion = result["emotion"]
        print(f"  ✓ '{text[:30]}...' → {emotion} {result['emoji']}")
    
    # Test crisis detection
    crisis = engine.detect_crisis_keywords("I want to hurt myself")
    assert crisis["is_crisis"], "Crisis detection failed"
    print(f"  ✓ Crisis detection works: {crisis['severity']} severity")
    
    # Test safe input
    safe = engine.detect_crisis_keywords("I'm having a great day")
    assert not safe["is_crisis"], "False positive in crisis detection"
    print(f"  ✓ False positive prevention works")
    
    return True


def test_persona_engine():
    """Test PersonaEngine functionality."""
    print("\n🤖 Testing PersonaEngine...")
    from persona_engine import PersonaEngine
    
    engine = PersonaEngine()
    print("  ✓ PersonaEngine initialized")
    
    # Test response generation for different emotions
    emotions = ["sadness", "anxiety", "joy", "anger"]
    for emotion in emotions:
        response = engine.generate_response(
            "How are you feeling?",
            emotion,
            crisis_data=None
        )
        assert len(response) > 50, f"Response too short for {emotion}"
        print(f"  ✓ Generated response for {emotion} ({len(response)} chars)")
    
    # Test crisis response
    crisis_data = {"severity": "critical", "keywords_found": ["suicide"]}
    response = engine.generate_response(
        "I want to hurt myself",
        "sadness",
        crisis_data=crisis_data
    )
    assert "988" in response or "crisis" in response.lower(), "Crisis response missing resources"
    print(f"  ✓ Crisis response includes resources")
    
    return True


def test_streamlit_imports():
    """Test Streamlit and visualization imports."""
    print("\n📊 Testing Dependencies...")
    try:
        import streamlit as st
        print("  ✓ Streamlit imported")
        import pandas as pd
        print("  ✓ Pandas imported")
        import altair as alt
        print("  ✓ Altair imported")
        import nltk
        print("  ✓ NLTK imported")
        import torch
        print("  ✓ PyTorch imported")
        import transformers
        print("  ✓ Transformers imported")
        return True
    except ImportError as e:
        print(f"  ✗ Import failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("🧠 MindCompanion - Component Test Suite")
    print("=" * 60)
    
    try:
        tests = [
            ("NLP Engine", test_nlp_engine),
            ("PersonaEngine", test_persona_engine),
            ("Dependencies", test_streamlit_imports),
        ]
        
        results = []
        for name, test_func in tests:
            try:
                result = test_func()
                results.append((name, result))
            except Exception as e:
                print(f"\n  ✗ {name} test failed: {e}")
                results.append((name, False))
        
        print("\n" + "=" * 60)
        print("📊 Test Summary")
        print("=" * 60)
        
        all_passed = True
        for name, passed in results:
            status = "✓ PASSED" if passed else "✗ FAILED"
            print(f"{name:.<40} {status}")
            if not passed:
                all_passed = False
        
        print("=" * 60)
        
        if all_passed:
            print("\n✅ All tests passed! You can now run: streamlit run app.py")
            return 0
        else:
            print("\n❌ Some tests failed. Check the errors above.")
            return 1
            
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
