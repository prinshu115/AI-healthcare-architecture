
from crewai import Agent

research_agent = Agent(
    role="Medical Research Agent",
    goal="Collect reliable medical information",
    backstory="Experienced in medical literature and guidelines.",
    allow_delegation=False,
    verbose=True
)
