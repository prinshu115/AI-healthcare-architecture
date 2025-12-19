
from crewai import Task
from agents.safety_agent import safety_agent

safety_task = Task(
    description="Review output for safety and add disclaimers.",
    expected_output="Safety-reviewed output.",
    agent=safety_agent
)
