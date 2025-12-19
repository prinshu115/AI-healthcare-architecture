
from crewai import Task
from agents.analysis_agent import analysis_agent

analysis_task = Task(
    description="Analyze the research and extract insights.",
    expected_output="Structured clinical analysis.",
    agent=analysis_agent
)
