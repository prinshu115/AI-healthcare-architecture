
from crewai import Crew, Process
from agents.research_agent import research_agent
from agents.analysis_agent import analysis_agent
from agents.safety_agent import safety_agent
from tasks.research_task import research_task
from tasks.analysis_task import analysis_task
from tasks.safety_task import safety_task

healthcare_crew = Crew(
    agents=[research_agent, analysis_agent, safety_agent],
    tasks=[research_task, analysis_task, safety_task],
    process=Process.sequential,
    verbose=True
)
