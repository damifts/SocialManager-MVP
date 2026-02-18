# Scripts - DevOps & Automation Utilities

This directory contains automation scripts for testing webhooks, managing deployments, and integrating with external services.

## 📋 Available Scripts

### 🔔 test_webhook.py

Test webhook integrations for Google Chat, GitHub, Slack, or custom services.

**Quick Start:**

```powershell
# PowerShell - Set webhook URL
$env:WEBHOOK_URL = "https://your-webhook-url-here"
python scripts/test_webhook.py

# Or inline (all platforms)
$env:WEBHOOK_URL="https://your-webhook-url-here"; python scripts/test_webhook.py
```

**Features:**
- ✅ Multiple webhook format support (Google Chat, GitHub, Generic)
- ✅ Detailed error reporting and diagnostics
- ✅ Automatic payload formatting
- ✅ Connection timeout handling
- ✅ Response status validation

---

## 🔗 Getting Webhook URLs

### Google Chat

1. Open your Google Chat workspace
2. Right-click on a space/room → "Edit space"
3. Go to "Apps & Integrations" → "Manage webhooks"
4. Click "Create new webhook"
5. Name it (e.g., "SocialManager-Notifications")
6. Copy the webhook URL (looks like):
   ```
   https://chat.googleapis.com/v1/spaces/XXXXXX/messages?key=XXXXXX
   ```

### GitHub

1. Go to your repository → Settings → Webhooks
2. Click "Add webhook"
3. **Payload URL**: Enter your endpoint (e.g., `https://your-server.com/webhook`)
4. **Content type**: Select `application/json`
5. **Events**: Choose which events trigger the webhook
6. Copy the webhook URL

### Slack

1. Go to [Slack Apps](https://api.slack.com/apps)
2. Create a new app → "From scratch"
3. Name it (e.g., "SocialManager")
4. Select your workspace
5. Go to "Incoming Webhooks" → "Add New Webhook to Workspace"
6. Copy the webhook URL (example format):
   ```
   https://hooks.slack.com/services/YOUR-TEAM-ID/YOUR-CHANNEL-ID/YOUR-SECRET-KEY
   ```

---

## 💻 Alternative: Using curl

If you prefer testing from the terminal without Python:

**PowerShell:**
```powershell
$url = "https://your-webhook-url-here"
$payload = @{
    title = "🧪 Test dal terminale di Damiano"
    message = "Sincronizzate i branch!"
    timestamp = (Get-Date -Format 'o')
} | ConvertTo-Json

Invoke-WebRequest -Uri $url -Method Post -Body $payload -ContentType "application/json" -Verbose
```

**Command Prompt (cmd.exe):**
```batch
curl -X POST https://your-webhook-url-here ^
  -H "Content-Type: application/json" ^
  -d "{\"title\":\"Test dal terminale\",\"message\":\"Sincronizzate i branch!\"}"
```

**Unix/Linux/Mac:**
```bash
curl -X POST https://your-webhook-url-here \
  -H "Content-Type: application/json" \
  -d '{"title":"Test dal terminale di Damiano","message":"Sincronizzate i branch!"}'
```

---

## 🧪 Usage Examples

### Test with verbose output:

```powershell
# PowerShell
$env:WEBHOOK_URL="https://chat.googleapis.com/v1/spaces/..."
python scripts/test_webhook.py
```

### Check if webhook endpoint is reachable:

```powershell
# Quick connectivity check
curl -I https://your-webhook-url-here
```

### Capture full response:

```powershell
$response = Invoke-WebRequest -Uri "https://your-webhook-url-here" `
  -Method Post `
  -Body '{"test":"message"}' `
  -ContentType "application/json" `
  -PassThru

$response | Select-Object StatusCode, StatusDescription
$response.Content
```

---

## 📊 Expected Webhook Responses

### ✅ Successful Responses

**Google Chat:**
- Status: `200 OK`
- Response: Empty or `name: projects/.../messages/...`

**GitHub:**
- Status: `200 OK` or `204 No Content`
- Response: May contain repository information

**Slack:**
- Status: `200 OK`
- Response: `ok` (plain text)

### ❌ Common Errors

| Status | Meaning | Solution |
|--------|---------|----------|
| 400 | Bad Request | Check payload format (JSON structure) |
| 401 | Unauthorized | Invalid or expired webhook URL |
| 403 | Forbidden | Insufficient permissions or IP blocked |
| 404 | Not Found | Webhook URL doesn't exist |
| 429 | Rate Limited | Too many requests; wait before retrying |
| 500 | Server Error | Webhook service is down |
| Timeout | Connection failed | Check internet; webhook URL might be wrong |

---

## 🔧 Environment Variables

### Required

- `WEBHOOK_URL` - The webhook endpoint to test

### Optional (in test_webhook.py)

- `DEVELOPER_NAME` - Name to include in messages (default: "Damiano")
- `TEAM_NAME` - Team name in messages (default: "Social Manager Team")

---

## 📝 Adding New Scripts

To add a new automation script:

1. Create the script in this directory: `scripts/new_script.py`
2. Add documentation in this README
3. Include proper error handling and logging
4. Test with: `python scripts/new_script.py`
5. Commit and document in the main README

**Example template:**

```python
#!/usr/bin/env python3
"""
Script description.

Usage:
    python scripts/new_script.py --option value
"""

import sys
import os

def main():
    """Main entry point."""
    print("Script executing...")

if __name__ == "__main__":
    main()
```

---

## 🆘 Troubleshooting

### "requests module not found"

```powershell
pip install requests
```

### Webhook URL contains special characters

Ensure the URL is properly quoted:

```powershell
$env:WEBHOOK_URL='https://your-webhook-url-with-special-chars?key=value&test=1'
```

### Certificate verification errors (on Windows)

```powershell
# Temporarily disable SSL verification (NOT for production)
$env:PYTHONHTTPSVERIFY=0
python scripts/test_webhook.py
```

### Testing from behind a corporate proxy

```powershell
python scripts/test_webhook.py `
  --proxy http://proxy.company.com:8080
```

---

## 📚 Related Documentation

- [README.md](../README.md) - Main project documentation
- [docs/API.md](../docs/API.md) - Backend API reference
- GitHub Actions workflows - CI/CD integration (`.github/workflows/`)

---

**Last Updated:** 2026-02-17
**Maintainer:** Social Manager DevOps Team
