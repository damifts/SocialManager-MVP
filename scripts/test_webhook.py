#!/usr/bin/env python3
"""
Webhook Test Script - DevOps Utility

Tests webhooks for Google Chat, GitHub, or other services.

Usage:
    python scripts/test_webhook.py                  # Uses WEBHOOK_URL from config
    WEBHOOK_URL="<your-url>" python scripts/test_webhook.py    # Override
"""

import json
import sys
import os
from datetime import datetime
from typing import Optional, Dict, Any

try:
    import requests
except ImportError:
    print("❌ Error: 'requests' module not found.")
    print("   Install it with: pip install requests")
    sys.exit(1)


# ============================================================================
# CONFIGURATION
# ============================================================================

# Define your webhook URL here or set WEBHOOK_URL environment variable
WEBHOOK_URL: Optional[str] = os.getenv("WEBHOOK_URL", "")

# Team/Developer info
DEVELOPER_NAME = "Damiano"
TEAM_NAME = "Social Manager Team"


# ============================================================================
# WEBHOOK PAYLOAD BUILDERS
# ============================================================================

def build_google_chat_payload(message: str, title: str = "Test Webhook") -> Dict[str, Any]:
    """Build a Google Chat webhook payload."""
    return {
        "text": f"🔔 *{title}*\n\n{message}\n\n_Sent from: {DEVELOPER_NAME}'s Terminal_"
    }


def build_github_payload(message: str, title: str = "Test Webhook") -> Dict[str, Any]:
    """Build a GitHub webhook payload (adapted format)."""
    return {
        "action": "opened",
        "title": title,
        "body": message,
        "head_commit": {
            "message": f"Test: {message}",
            "author": {
                "name": DEVELOPER_NAME,
                "email": f"{DEVELOPER_NAME}@example.com"
            }
        }
    }


def build_generic_payload(message: str, title: str = "Test Webhook") -> Dict[str, Any]:
    """Build a generic webhook payload."""
    return {
        "timestamp": datetime.now().isoformat(),
        "title": title,
        "message": message,
        "source": "test_webhook.py",
        "developer": DEVELOPER_NAME,
        "team": TEAM_NAME
    }


# ============================================================================
# WEBHOOK TESTER
# ============================================================================

def test_webhook(
    webhook_url: str,
    payload: Dict[str, Any],
    webhook_type: str = "generic",
    timeout: int = 10
) -> bool:
    """
    Send a test payload to a webhook.
    
    Args:
        webhook_url: The webhook URL
        payload: The payload to send
        webhook_type: Type of webhook (google_chat, github, generic)
        timeout: Request timeout in seconds
        
    Returns:
        True if successful (status 200), False otherwise
    """
    
    print(f"\n{'='*70}")
    print(f"🧪 WEBHOOK TEST - {webhook_type.upper()}")
    print(f"{'='*70}\n")
    
    # Validate URL
    if not webhook_url:
        print("❌ Error: WEBHOOK_URL is empty!")
        print("\n   Set it using:")
        print("   - Environment variable: WEBHOOK_URL='<url>' python scripts/test_webhook.py")
        print("   - Or edit this script and set WEBHOOK_URL directly")
        return False
    
    if not webhook_url.startswith(("http://", "https://")):
        print(f"❌ Error: Invalid URL format: {webhook_url}")
        print("   URL must start with http:// or https://")
        return False
    
    # Print request details
    print(f"📍 Webhook URL:")
    print(f"   {webhook_url}\n")
    
    print(f"📦 Payload:")
    print(f"   {json.dumps(payload, indent=2, ensure_ascii=False)}\n")
    
    # Send request
    try:
        print("📤 Sending POST request...\n")
        
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            webhook_url,
            json=payload,
            headers=headers,
            timeout=timeout
        )
        
        # Print response details
        print(f"{'─'*70}")
        print(f"📥 Response Status: {response.status_code}")
        print(f"{'─'*70}\n")
        
        # Check status code
        if response.status_code == 200:
            print("✅ SUCCESS! Webhook delivered successfully.")
            if response.text:
                print(f"\nResponse body:\n{response.text}")
            return True
        
        elif response.status_code in (201, 202, 204):
            print(f"✅ SUCCESS! (Status {response.status_code})")
            if response.text:
                print(f"\nResponse body:\n{response.text}")
            return True
        
        else:
            print(f"⚠️  Unexpected Status: {response.status_code}")
            print(f"\nResponse headers:")
            for key, value in response.headers.items():
                print(f"   {key}: {value}")
            if response.text:
                print(f"\nResponse body:\n{response.text}")
            return False
    
    except requests.exceptions.Timeout:
        print(f"❌ Error: Request timeout (>{timeout}s)")
        print("   - Check your internet connection")
        print("   - Webhook URL might be unresponsive")
        return False
    
    except requests.exceptions.ConnectionError:
        print(f"❌ Error: Connection failed")
        print("   - Check if the webhook URL is correct")
        print("   - Verify your internet connection")
        print("   - The webhook service might be down")
        return False
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: Request failed")
        print(f"   {type(e).__name__}: {e}")
        return False
    
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Main entry point."""
    
    # Get webhook URL from environment or script variable
    webhook_url = os.getenv("WEBHOOK_URL", WEBHOOK_URL)
    
    if not webhook_url:
        print("\n" + "="*70)
        print("❌ WEBHOOK_URL NOT SET")
        print("="*70 + "\n")
        print("You must provide a webhook URL. Set it using one of:\n")
        print("Option 1 - Environment Variable (Windows PowerShell):")
        print('  $env:WEBHOOK_URL = "https://your-webhook-url-here"')
        print("  python scripts/test_webhook.py\n")
        print("Option 2 - Environment Variable (CMD):")
        print("  set WEBHOOK_URL=https://your-webhook-url-here")
        print("  python scripts/test_webhook.py\n")
        print("Option 3 - Inline (All platforms):")
        print('  WEBHOOK_URL="https://your-webhook-url-here" python scripts/test_webhook.py\n')
        print("Option 4 - Edit this script:")
        print("  Open scripts/test_webhook.py and set WEBHOOK_URL directly\n")
        print("="*70 + "\n")
        sys.exit(1)
    
    # Build test payload
    test_message = f"""
✅ Webhook Test Successful!

Team: {TEAM_NAME}
Developer: {DEVELOPER_NAME}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Branch Status: ✅ All synchronized
Tests: ✅ Passing
Documentation: ✅ Updated

This is an automated test message from the development terminal.
"""
    
    payload = build_generic_payload(
        message=test_message.strip(),
        title="🧪 Test dal terminale di Damiano - Sincronizzate i branch!"
    )
    
    # Test the webhook
    success = test_webhook(
        webhook_url=webhook_url,
        payload=payload,
        webhook_type="generic",
        timeout=10
    )
    
    # Exit with appropriate code
    if success:
        print("\n" + "="*70)
        print("✅ TEST COMPLETED SUCCESSFULLY")
        print("="*70 + "\n")
        sys.exit(0)
    else:
        print("\n" + "="*70)
        print("❌ TEST FAILED")
        print("="*70 + "\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
