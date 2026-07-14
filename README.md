
# ResQAI: Agentic Disaster Response & Rescue Coordination Platform

ResQAI is an enterprise-grade, agentic AI platform engineered to streamline disaster response and rescue coordination. By integrating **IBM Granite models** via **Watsonx** and leveraging the **IBM BoB** development ecosystem, this platform delivers data-driven insights in critical, high-latency environments.

## 🎯 Project Objective
The primary mission of ResQAI is to enhance rescue efficiency by automating the triage of incident reports and optimizing resource dispatch. Our system exploits location-specific data and **Quality of Service (QoS) factors** to ensure reliable communication and actionable recommendations during emergency scenarios.

## 🏗️ Technical Architecture
The platform is built on a modular, agentic framework designed for resilience:
*   **Agentic Core:** Powered by Watsonx, IBM Granite models for contextual reasoning and rapid decision-making.
*   **QoS-Aware Recommendation Engine:** Utilizes specialized algorithms to determine the most reliable communication routes and rescue paths based on real-time network stability.
*   **Infrastructure:** Deployed within the IBM BoB environment to ensure scalability and integration with enterprise AI services.

## 📁 Repository Contents
| Description |
| :--- | :--- |
| Project configuration and environment manifest. |
| Detailed problem statement and research context. |

## 🛠️ Key Technical Skills Demonstrated
*   **Software Engineering:** Architecture design and implementation of complex recommendation systems.
*   **AI Integration:** Application of Large Language Models (LLMs) to real-world humanitarian logistics.
*   **Professional Documentation:** Structured reporting of technical projects for evaluation and stakeholder review.


Developed as part of a comprehensive curriculum in Computer Science Engineering (B.Tech CSE), this project underscores a commitment to advancing AI-driven solutions for public safety. 
=======
# 🛡️ ResQAI — AI-Powered Emergency Response Platform

> Real-time emergency guidance, first aid instructions, SOS generation, disaster
> checklists, and AI incident reports — powered by **IBM Watsonx.ai** and
> **IBM Granite 13B Chat v2**.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Prerequisites](#prerequisites)
5. [IBM Cloud Setup](#ibm-cloud-setup)
6. [Local Deployment](#local-deployment)
7. [Environment Variables](#environment-variables)
8. [API Endpoints Reference](#api-endpoints-reference)
9. [Customising the AI Agent](#customising-the-ai-agent)
10. [Production Deployment](#production-deployment)
11. [Troubleshooting](#troubleshooting)
12. [Tech Stack](#tech-stack)
13. [Disclaimer](#disclaimer)

---

## Overview

ResQAI is a full-stack Python Flask web application that integrates IBM Watsonx.ai
to deliver AI-driven emergency response tools accessible from any browser.
Every AI response is governed by an `AGENT_INSTRUCTIONS` system prompt that
enforces a safety-first, calm, and factual tone — ensuring the model stays
focused on life-saving guidance and never speculates beyond its scope.

**Live URL after local deployment:** `http://127.0.0.1:5000`

---

## Features

| Module | Route | Description |
|---|---|---|
| Home | `/` | Landing page with platform overview and quick navigation |
| AI Emergency Assistant | `/assistant` | Real-time chat with IBM Granite for any emergency scenario |
| First Aid Assistant | `/first-aid` | AI-generated step-by-step first aid + CPR / bleeding / choking reference cards |
| SOS Generator | `/sos` | MAYDAY message builder, Morse code display, Web Audio playback, distress signal guide |
| Emergency Checklist | `/checklist` | Interactive preparedness checklists for 7 disaster types with progress tracking |
| AI Incident Report | `/incident-report` | 3-step form → IBM Granite composes a professional, print-ready report with report ID |
| Emergency Contacts | `/contacts` | Region-filtered directory (7 regions, 80+ contacts) with live search and copy-to-clipboard |
| About | `/about` | Platform info, tech stack, AI pipeline diagram, safety principles, and FAQ |

---

## Project Structure

```
resqai/
├── app.py                  # Flask app, Watsonx.ai integration, all routes & API endpoints
├── requirements.txt        # Python dependencies with pinned versions
├── .env.example            # Template — copy to .env and fill in credentials
├── README.md               # This file
│
├── templates/              # Jinja2 HTML templates
│   ├── base.html           # Shared navbar, footer, Bootstrap 5 imports
│   ├── index.html          # Home page
│   ├── assistant.html      # AI Emergency Assistant (chat UI)
│   ├── first_aid.html      # First Aid Assistant
│   ├── sos.html            # SOS Generator
│   ├── checklist.html      # Emergency Checklist
│   ├── incident_report.html# AI Incident Report Generator
│   ├── contacts.html       # Emergency Contacts Directory
│   └── about.html          # About page
│
└── static/
    ├── css/
    │   └── style.css       # Global design system — all resq-* component styles
    └── js/
        └── main.js         # Navbar scroll, toast helper, back-to-top, Bootstrap tooltip init
```

---

## Prerequisites

Ensure the following are installed on your machine before starting:

| Requirement | Minimum Version | Check |
|---|---|---|
| Python | 3.10+ | `python --version` |
| pip | 23+ | `pip --version` |
| Git | any | `git --version` |
| IBM Cloud Account | — | [cloud.ibm.com](https://cloud.ibm.com) |
| IBM Watsonx.ai project | — | [watsonx.ai](https://www.ibm.com/watsonx) |

---

## IBM Cloud Setup

You need two values from IBM Cloud before the app can call the AI.

### Step 1 — Create an IBM Cloud API Key

1. Log in to [IBM Cloud](https://cloud.ibm.com).
2. Click your profile avatar (top right) → **"Manage" → "Access (IAM)"**.
3. In the left sidebar select **"API keys"**.
4. Click **"Create an IBM Cloud API key"**.
5. Give it a name (e.g., `resqai-key`) and click **Create**.
6. **Copy the key immediately** — it is shown only once.

### Step 2 — Get your Watsonx.ai Project ID

1. Go to [watsonx.ai](https://www.ibm.com/watsonx) and open your project
   (or create one via **"New project"**).
2. Open the project, click the **"Manage"** tab.
3. Under **"General"**, copy the **Project ID** (UUID format).

### Step 3 — Note your Regional URL

| IBM Cloud Region | Watsonx.ai URL |
|---|---|
| US South (Dallas) | `https://us-south.ml.cloud.ibm.com` *(default)* |
| EU (Frankfurt) | `https://eu-de.ml.cloud.ibm.com` |
| AP (Tokyo) | `https://jp-tok.ml.cloud.ibm.com` |
| UK (London) | `https://eu-gb.ml.cloud.ibm.com` |

---

## Local Deployment

Follow these steps exactly, in order.

### 1 — Clone the repository

```bash
git clone https://github.com/Gayatri-user/ResQAI_IBM-project
cd resqai
```

Or if you already have the project folder:

```bash
cd resqai
```

### 2 — Create a Python virtual environment

```bash
# Create the environment
python -m venv venv

# Activate on macOS / Linux
source venv/bin/activate

# Activate on Windows (Command Prompt)
venv\Scripts\activate.bat

# Activate on Windows (PowerShell)
venv\Scripts\Activate.ps1
```

You should see `(venv)` prepended to your terminal prompt.

### 3 — Install dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `Flask==3.0.3` — web framework
- `python-dotenv==1.0.1` — `.env` file loader
- `ibm-watsonx-ai==1.1.2` — IBM Watsonx.ai Python SDK
- `requests==2.32.3` — HTTP library
- `gunicorn==22.0.0` — production WSGI server

### 4 — Configure environment variables

```bash
# Copy the example file
cp .env.example .env
```

Open `.env` in your editor and fill in your credentials:

```env
IBM_API_KEY=your_actual_ibm_cloud_api_key
WATSONX_PROJECT_ID=your_actual_project_id_uuid
WATSONX_URL=https://us-south.ml.cloud.ibm.com

FLASK_SECRET_KEY=pick-any-long-random-string-here
FLASK_DEBUG=False
```

> ⚠️ **Never commit `.env` to version control.** It is already listed in `.gitignore`.
> Share credentials with teammates via a secrets manager, not via email or chat.

### 5 — Run the development server

```bash
python app.py
```

Expected output:

```
 * Running on http://0.0.0.0:5000
 * Debug mode: off
```

Open your browser at **[http://127.0.0.1:5000](http://127.0.0.1:5000)**.

### 6 — Verify the AI is working

1. Navigate to **AI Assistant** (`/assistant`).
2. Type `"Someone is having a heart attack, what do I do?"` and press **Send**.
3. You should receive a numbered first-aid response from IBM Granite within a few seconds.

If you see `⚠️ AI service error:` in the response, check your credentials
in `.env` and consult the [Troubleshooting](#troubleshooting) section.

---

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `IBM_API_KEY` | ✅ | IBM Cloud API key with Watsonx.ai access |
| `WATSONX_PROJECT_ID` | ✅ | UUID of your Watsonx.ai project |
| `WATSONX_URL` | ✅ | Regional endpoint (default: `https://us-south.ml.cloud.ibm.com`) |
| `FLASK_SECRET_KEY` | ✅ | Random string used to sign Flask sessions |
| `FLASK_DEBUG` | ❌ | `True` for hot reload during development; always `False` in production |

---

## API Endpoints Reference

All endpoints accept and return `application/json`.

### `POST /api/chat`
AI Emergency Assistant — general emergency chat.

```json
// Request
{ "message": "Someone is choking, what do I do?" }

// Response
{ "reply": "1. Ask 'Are you choking?'..." }
```

---

### `POST /api/first-aid`
First Aid guidance for a described medical situation.

```json
// Request
{ "situation": "A person has a deep wound with heavy bleeding" }

// Response
{ "guidance": "1. Call 911 immediately..." }
```

---

### `POST /api/generate-report`
AI Incident Report generation.

```json
// Request
{
  "incident_type": "Fire / Explosion",
  "location": "123 Main St, Building B",
  "date_time": "2024-11-15T14:30",
  "description": "A fire broke out in the server room...",
  "injuries": "2 minor burns",
  "actions_taken": "Called 911, evacuated building"
}

// Response
{ "report": "INCIDENT SUMMARY\n..." }
```

---

### `POST /api/sos-message`
Generate a broadcast-ready MAYDAY SOS message.

```json
// Request
{
  "name": "Jane Doe",
  "location": "Trail 5, Rocky Mountain Park, GPS 40.3572° N",
  "situation": "Hiker with broken leg, unable to move",
  "people_count": "2"
}

// Response
{ "sos_message": "MAYDAY MAYDAY MAYDAY..." }
```

---

## Customising the AI Agent

Open [`app.py`](app.py) and find the `AGENT_INSTRUCTIONS` constant near the top.
This string is prepended to **every** prompt sent to IBM Granite and controls:

| Section | Controls |
|---|---|
| `TONE & STYLE` | Response format, sentence length, use of numbered steps |
| `SAFETY RULES` | 911-first protocol, no-diagnosis rule, no-speculation rule |
| `SCOPE` | What topics the model will and will not engage with |

**Example — add a language preference:**

```python
AGENT_INSTRUCTIONS = """
You are ResQAI ...
Always respond in simple English at a Grade 8 reading level.
...
"""
```

**Example — add a jurisdiction:**

```python
AGENT_INSTRUCTIONS = """
...
When referencing emergency numbers, use 999 (UK) as the primary number.
...
"""
```

Changes take effect immediately on the next request — no restart required
when using the development server with `FLASK_DEBUG=True`.

---

## Production Deployment

### Option A — Gunicorn (any Linux server / VPS)

```bash
# Activate your virtualenv first
source venv/bin/activate

# 4 worker processes, bind to all interfaces on port 5000
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

Pair with **nginx** as a reverse proxy:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass         http://127.0.0.1:5000;
        proxy_set_header   Host $host;
        proxy_set_header   X-Real-IP $remote_addr;
        proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

### Option B — IBM Cloud Code Engine

```bash
# Build and push a container image, then:
ibmcloud ce application create \
  --name resqai \
  --image icr.io/your-namespace/resqai:latest \
  --env-from-secret resqai-secrets \
  --port 5000
```

### Option C — IBM Cloud Foundry

```bash
# Create a manifest.yml in the resqai/ directory:
cat > manifest.yml << EOF
applications:
  - name: resqai
    memory: 512M
    instances: 1
    command: gunicorn -w 2 -b 0.0.0.0:\$PORT app:app
    buildpacks:
      - python_buildpack
EOF

ibmcloud cf push
```

Set environment variables in the IBM Cloud dashboard or with:

```bash
ibmcloud cf set-env resqai IBM_API_KEY your_key_here
ibmcloud cf set-env resqai WATSONX_PROJECT_ID your_project_id
ibmcloud cf set-env resqai WATSONX_URL https://us-south.ml.cloud.ibm.com
ibmcloud cf set-env resqai FLASK_SECRET_KEY your_secret_key
ibmcloud cf restage resqai
```

### Production security checklist

- [ ] `FLASK_DEBUG=False` in production
- [ ] `FLASK_SECRET_KEY` is a long, random, unique string
- [ ] `.env` is not committed to version control
- [ ] HTTPS is enforced via reverse proxy or platform TLS
- [ ] IBM Cloud API key has the **minimum required IAM permissions**

---

## Troubleshooting

### `⚠️ AI service error: 401 Unauthorized`
Your `IBM_API_KEY` is invalid or expired.
1. Log in to IBM Cloud → IAM → API keys.
2. Generate a new key and update `.env`.

### `⚠️ AI service error: 404 Not Found / model not available`
The model ID `ibm/granite-13b-chat-v2` may not be available in your region or plan.
1. Log in to Watsonx.ai → Foundation models → verify the model is listed.
2. Update `model_id` in `app.py → get_model()` to a model available in your account.

### `⚠️ AI service error: 403 Forbidden`
Your `WATSONX_PROJECT_ID` is wrong or your API key does not have access to the project.
1. Open your Watsonx.ai project → Manage tab → copy the exact UUID.
2. Ensure your IBM Cloud user has the **Editor** or **Manager** role on the project.

### `ModuleNotFoundError: No module named 'ibm_watsonx_ai'`
The virtual environment is not activated, or `pip install` was not run.
```bash
source venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

### `Address already in use` (port 5000)
Another process is using port 5000 (e.g., AirPlay on macOS).
```bash
python app.py   # will fail
# Run on a different port:
flask run --port 5001
```

### `jinja2.exceptions.TemplateNotFound`
Flask cannot find a template. Ensure you are running `python app.py` from
**inside** the `resqai/` directory, not from its parent.
```bash
cd resqai
python app.py
```

---

## Tech Stack

| Layer | Technology | Version |
|---|---|---|
| AI Platform | IBM Watsonx.ai | — |
| Foundation Model | IBM Granite 13B Chat v2 | `ibm/granite-13b-chat-v2` |
| AI SDK | ibm-watsonx-ai | 1.1.2 |
| Backend | Python Flask | 3.0.3 |
| WSGI Server | Gunicorn | 22.0.0 |
| Config management | python-dotenv | 1.0.1 |
| Frontend framework | Bootstrap | 5.3.3 |
| Icons | Bootstrap Icons | 1.11.3 |
| Language | Python | 3.10+ |

---

## Disclaimer

ResQAI is an AI-assisted informational tool. It does **not** replace professional
emergency services, trained medical personnel, or official disaster management
authorities.

**In any life-threatening emergency, call 911 (or your local emergency number)
immediately.**

AI responses may contain errors. Always use your judgment and follow guidance
from trained professionals. The developers of ResQAI assume no liability for
actions taken based on AI-generated content.
>>>>>>> cf462f3 (Initial commit: Add ResQAI project files and app.json)
