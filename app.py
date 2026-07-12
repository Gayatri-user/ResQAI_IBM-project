import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "resqai-default-secret-key")

# ---------------------------------------------------------------------------
# Agent Instructions — disaster management scope, safety rules, response style
# ---------------------------------------------------------------------------
AGENT_INSTRUCTIONS = """
You are ResQAI, an intelligent disaster response and rescue coordination assistant powered by IBM Watsonx.ai Granite.

ROLE:
- You assist emergency managers, first responders, and affected civilians during natural and man-made disasters.
- Your expertise covers: disaster preparedness, evacuation planning, search and rescue coordination, resource management, shelter operations, flood/earthquake/wildfire/hurricane response, and post-disaster recovery.

TONE & STYLE:
- Always respond in a calm, authoritative, and clear tone.
- Use short sentences and numbered steps for procedural guidance.
- Prioritize life-safety information above all else.
- Be concise — disasters require fast, actionable answers.

SAFETY RULES:
- ALWAYS advise users to follow official emergency management authority directives.
- ALWAYS advise contacting official emergency services (911 or local equivalent) when there is immediate danger to life.
- Never speculate about casualty numbers or structural safety — direct users to official assessments.
- Do not provide guidance that could interfere with professional rescue operations.
- Remind users that AI guidance supplements but never replaces trained emergency responders and official disaster management authorities.

SCOPE — you ONLY assist with:
- Natural disaster response: earthquakes, floods, hurricanes, tornadoes, wildfires, tsunamis, landslides
- Man-made disaster response: industrial accidents, hazmat spills, structural collapses, power grid failures
- Evacuation planning and route guidance
- Search and rescue coordination
- Emergency shelter and resource logistics
- Disaster preparedness and community resilience
- SOS signalling and distress communication
- Incident documentation and situation reporting
- Post-disaster recovery guidance

OUT OF SCOPE — you do NOT assist with:
- Non-emergency topics, politics, entertainment, or anything outside disaster management
- Standalone medical advice (advise contacting EMS for all medical concerns)

Begin every response with a brief acknowledgment of the situation if urgency is implied.
"""

# ---------------------------------------------------------------------------
# Watsonx.ai Model Initialization
# ---------------------------------------------------------------------------
def get_model() -> ModelInference:
    """Return a configured Watsonx.ai Granite model instance."""
    credentials = Credentials(
        api_key=os.getenv("IBM_API_KEY"),
        url=os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com"),
    )
    params = {
        GenParams.MAX_NEW_TOKENS: 1024,
        GenParams.MIN_NEW_TOKENS: 10,
        GenParams.TEMPERATURE: 0.3,
        GenParams.TOP_P: 0.9,
        GenParams.REPETITION_PENALTY: 1.1,
        GenParams.STOP_SEQUENCES: ["Human:", "User:"],
    }
    return ModelInference(
        model_id="mistralai/mistral-small-3-1-24b-instruct-2503",
        credentials=credentials,
        project_id=os.getenv("WATSONX_PROJECT_ID"),
        params=params,
    )


def query_watsonx(prompt: str) -> str:
    """Send a prompt to Watsonx.ai and return the generated text."""
    try:
        model = get_model()
        full_prompt = f"{AGENT_INSTRUCTIONS}\n\nUser: {prompt}\n\nResQAI:"
        response = model.generate_text(prompt=full_prompt)
        return response.strip()
    except Exception as exc:
        return f"⚠️ AI service error: {str(exc)}. Please check your IBM credentials in the .env file."


# ---------------------------------------------------------------------------
# Routes — Pages
# ---------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/assistant")
def assistant():
    return render_template("assistant.html")


@app.route("/evacuation")
def evacuation():
    return render_template("evacuation.html")


@app.route("/sos")
def sos():
    return render_template("sos.html")


@app.route("/checklist")
def checklist():
    return render_template("checklist.html")


@app.route("/incident-report")
def incident_report():
    return render_template("incident_report.html")


@app.route("/resources")
def resources():
    return render_template("resources.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


@app.route("/about")
def about():
    return render_template("about.html")


# ---------------------------------------------------------------------------
# Routes — API Endpoints
# ---------------------------------------------------------------------------
@app.route("/api/chat", methods=["POST"])
def api_chat():
    """AI Disaster Response Assistant chat endpoint."""
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Message is required."}), 400
    reply = query_watsonx(user_message)
    return jsonify({"reply": reply})


@app.route("/api/evacuation-plan", methods=["POST"])
def api_evacuation_plan():
    """Generate an AI evacuation plan for a disaster scenario."""
    data = request.get_json(silent=True) or {}
    disaster_type = data.get("disaster_type", "").strip()
    location = data.get("location", "").strip()
    population = data.get("population", "").strip()
    special_needs = data.get("special_needs", "None").strip()

    if not disaster_type or not location:
        return jsonify({"error": "Disaster type and location are required."}), 400

    prompt = (
        f"Generate a detailed evacuation plan for the following disaster scenario:\n"
        f"- Disaster Type: {disaster_type}\n"
        f"- Affected Location: {location}\n"
        f"- Estimated Population: {population}\n"
        f"- Special Needs Considerations: {special_needs}\n\n"
        "Format the plan with numbered steps covering: immediate actions, evacuation routes, "
        "assembly points, transportation, communication, and special populations. "
        "Start with the most urgent life-safety actions."
    )
    plan = query_watsonx(prompt)
    return jsonify({"plan": plan})


@app.route("/api/generate-report", methods=["POST"])
def api_generate_report():
    """AI Disaster Incident Report generation endpoint."""
    data = request.get_json(silent=True) or {}
    incident_type = data.get("incident_type", "").strip()
    location = data.get("location", "").strip()
    date_time = data.get("date_time", "").strip()
    description = data.get("description", "").strip()
    casualties = data.get("casualties", "None reported").strip()
    actions_taken = data.get("actions_taken", "None").strip()

    if not description:
        return jsonify({"error": "Incident description is required."}), 400

    prompt = (
        f"Generate a professional disaster incident report based on the following details:\n"
        f"- Disaster/Incident Type: {incident_type}\n"
        f"- Location: {location}\n"
        f"- Date/Time: {date_time}\n"
        f"- Description: {description}\n"
        f"- Casualties / Displaced Persons: {casualties}\n"
        f"- Response Actions Taken: {actions_taken}\n\n"
        "Format the report with sections: SITUATION SUMMARY, INCIDENT DETAILS, "
        "AFFECTED POPULATION, RESPONSE ACTIONS TAKEN, RESOURCE NEEDS, and RECOMMENDATIONS."
    )
    report = query_watsonx(prompt)
    return jsonify({"report": report})


@app.route("/api/sos-message", methods=["POST"])
def api_sos_message():
    """Generate a structured SOS distress message for disaster rescue teams."""
    data = request.get_json(silent=True) or {}
    name = data.get("name", "Unknown").strip()
    location = data.get("location", "Unknown location").strip()
    situation = data.get("situation", "").strip()
    people_count = data.get("people_count", "1").strip()

    prompt = (
        f"Create a concise emergency SOS distress message for rescue coordination:\n"
        f"- Person's Name: {name}\n"
        f"- Location: {location}\n"
        f"- Disaster Situation: {situation}\n"
        f"- Number of People Requiring Rescue: {people_count}\n\n"
        "Format the SOS message to be broadcast-ready for rescue teams. "
        "Include a MAYDAY header, GPS/location details, nature of disaster, injuries if any, "
        "and immediate needs. Keep it under 100 words."
    )
    sos_text = query_watsonx(prompt)
    return jsonify({"sos_message": sos_text})


@app.route("/api/resource-plan", methods=["POST"])
def api_resource_plan():
    """Generate an AI disaster resource and shelter management plan."""
    data = request.get_json(silent=True) or {}
    disaster_type = data.get("disaster_type", "").strip()
    affected_count = data.get("affected_count", "").strip()
    duration_days = data.get("duration_days", "3").strip()
    available_resources = data.get("available_resources", "None specified").strip()

    if not disaster_type:
        return jsonify({"error": "Disaster type is required."}), 400

    prompt = (
        f"Generate a disaster resource and shelter management plan for the following:\n"
        f"- Disaster Type: {disaster_type}\n"
        f"- Estimated Affected Population: {affected_count}\n"
        f"- Planning Duration: {duration_days} days\n"
        f"- Available Resources: {available_resources}\n\n"
        "Cover: emergency shelter capacity, food and water distribution, medical triage referral, "
        "communication equipment, search and rescue resources, logistics and supply chain, "
        "and volunteer coordination. Format as numbered sections."
    )
    plan = query_watsonx(prompt)
    return jsonify({"plan": plan})


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)
