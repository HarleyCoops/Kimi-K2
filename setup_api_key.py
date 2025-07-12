#!/usr/bin/env python3
"""
Kimi-K2 API Key Configuration Utility

This utility facilitates the secure configuration of API credentials
for the Kimi-K2 language model interface.
"""

import os
import getpass
import sys

def setup_api_key():
    """Interactive configuration utility for API key initialization"""
    print("KIMI-K2 API KEY CONFIGURATION UTILITY")
    print("=" * 70)
    
    print("\nAPI Key Acquisition Procedure:")
    print("1. Navigate to: https://platform.moonshot.ai")
    print("2. Authenticate with your institutional credentials")
    print("3. Access the API Management section")
    print("4. Generate and copy your unique API key")
    
    print("\nSECURITY NOTICE: API keys must be treated as sensitive credentials.")
    print("Do not share or expose your API key in public repositories.\n")
    
    # Check for existing API key configuration
    current_key = os.getenv("MOONSHOT_API_KEY")
    if current_key and current_key != "your_api_key_here":
        print(f"[INFO] Existing API key detected: {current_key[:8]}{'*' * 32}")
        choice = input("Would you like to update the existing configuration? (y/N): ").lower()
        if choice != 'y':
            print("[INFO] Configuration update cancelled by user.")
            return
    
    print("\nAPI Key Entry (input will be hidden for security):")
    api_key = getpass.getpass("Enter API Key: ").strip()
    
    if not api_key:
        print("[ERROR] No API key provided. Configuration process terminated.")
        return
    
    if api_key == "your_api_key_here":
        print("[ERROR] Invalid API key. Please provide your actual API credentials.")
        return
    
    # Create .env file with proper formatting
    env_content = f"# Kimi-K2 API Configuration\nMOONSHOT_API_KEY={api_key}\n"
    
    try:
        with open(".env", "w") as f:
            f.write(env_content)
        print("[SUCCESS] API key successfully written to .env file")
        
        # Validate the API key
        print("\n[INFO] Initiating API key validation...")
        test_api_key(api_key)
        
    except Exception as e:
        print(f"[ERROR] Failed to write configuration file: {e}")
        print("\nAlternative Configuration Methods:")
        print("PowerShell: $env:MOONSHOT_API_KEY='your_api_key'")
        print("Command Prompt: set MOONSHOT_API_KEY=your_api_key")
        print("Linux/macOS: export MOONSHOT_API_KEY='your_api_key'")

def test_api_key(api_key):
    """Validate API key functionality through test request"""
    try:
        from openai import OpenAI
        
        client = OpenAI(
            base_url="https://api.moonshot.ai/v1",
            api_key=api_key
        )
        
        # Execute minimal test request
        response = client.chat.completions.create(
            model="moonshotai/kimi-k2-0711-preview",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=10
        )
        
        print("[SUCCESS] API key validation completed successfully.")
        print("\nAvailable Example Scripts:")
        print("  - quick_test.py: Basic functionality demonstration")
        print("  - kimi_k2_api_example.py: Comprehensive API usage examples")
        print("\nExecute with: python <script_name>")
        
    except Exception as e:
        print(f"[ERROR] API key validation failed: {e}")
        print("\nTroubleshooting Steps:")
        print("1. Verify API key correctness")
        print("2. Ensure network connectivity")
        print("3. Confirm API service availability")
        print("4. Check account permissions and quotas")

if __name__ == "__main__":
    setup_api_key() 