
from crewai import Task
from agents.research_agent import research_agent

research_task = Task(
    description="Research a medical topic using trusted sources.",
    expected_output="Factual medical summary.",
    agent=research_agent
)
