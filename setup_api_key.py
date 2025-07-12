#!/usr/bin/env python3
"""
Setup script for Kimi-K2 API Key

This script helps you set up your API key for the Kimi-K2 examples.
"""

import os
import getpass

def setup_api_key():
    """Interactive setup for API key"""
    print("🔑 Kimi-K2 API Key Setup")
    print("=" * 50)
    
    print("\n📋 To get your API key:")
    print("1. Visit: https://platform.moonshot.ai")
    print("2. Sign up or log in to your account")
    print("3. Navigate to the API section")
    print("4. Generate your API key")
    
    print("\n⚠️  Important: Keep your API key secure and never share it!")
    
    # Check if API key already exists
    current_key = os.getenv("MOONSHOT_API_KEY")
    if current_key and current_key != "your_api_key_here":
        print(f"\n✅ API key already set: {current_key[:8]}...")
        choice = input("Do you want to update it? (y/N): ").lower()
        if choice != 'y':
            print("Setup cancelled.")
            return
    
    print("\n🔐 Enter your API key:")
    api_key = getpass.getpass("API Key: ").strip()
    
    if not api_key:
        print("❌ No API key provided. Setup cancelled.")
        return
    
    if api_key == "your_api_key_here":
        print("❌ Please enter your actual API key, not the placeholder.")
        return
    
    # Create .env file
    env_content = f"# Kimi-K2 API Configuration\nMOONSHOT_API_KEY={api_key}\n"
    
    try:
        with open(".env", "w") as f:
            f.write(env_content)
        print("✅ API key saved to .env file")
        
        # Test the API key
        print("\n🧪 Testing API key...")
        test_api_key(api_key)
        
    except Exception as e:
        print(f"❌ Error saving API key: {e}")
        print("\n💡 Alternative: Set environment variable manually:")
        print("   PowerShell: $env:MOONSHOT_API_KEY='your_api_key'")
        print("   CMD: set MOONSHOT_API_KEY=your_api_key")

def test_api_key(api_key):
    """Test if the API key works"""
    try:
        from openai import OpenAI
        
        client = OpenAI(
            base_url="https://api.moonshot.ai/v1",
            api_key=api_key
        )
        
        # Simple test call
        response = client.chat.completions.create(
            model="moonshotai/kimi-k2-0711-preview",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=10
        )
        
        print("✅ API key is valid!")
        print("🚀 You can now run the examples:")
        print("   python quick_test.py")
        print("   python kimi_k2_api_example.py")
        
    except Exception as e:
        print(f"❌ API key test failed: {e}")
        print("💡 Please check your API key and try again.")

if __name__ == "__main__":
    setup_api_key() 