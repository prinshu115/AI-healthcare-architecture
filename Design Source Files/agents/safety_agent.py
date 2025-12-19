
from crewai import Agent

safety_agent = Agent(
    role="Safety Agent",
    goal="Ensure outputs are conservative and safe",
    backstory="Focuses on risk, disclaimers, and compliance.",
    allow_delegation=False,
    verbose=True
)
