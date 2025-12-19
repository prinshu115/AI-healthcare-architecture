
from crew import healthcare_crew

if __name__ == "__main__":
    print("Running agentic healthcare workflow...")
    output = healthcare_crew.kickoff()
    print(output)
