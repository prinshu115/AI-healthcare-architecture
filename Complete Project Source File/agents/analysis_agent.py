
from crewai import Agent

analysis_agent = Agent(
    role="Clinical Analysis Agent",
    goal="Analyze and structure medical findings",
    backstory="Transforms research into clear clinical insights.",
    allow_delegation=False,
    verbose=True
)
