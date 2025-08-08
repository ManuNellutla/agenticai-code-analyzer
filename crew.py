from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks

class CodeAnalyzerCrew:
    """Main crew for code analysis"""
    
    def __init__(self):
        self.agents = create_agents()
        self.tasks = create_tasks(self.agents)
        self.crew = self._create_crew()
    
    def _create_crew(self):
        return Crew(
            agents=list(self.agents.values()),
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2
        )
    
    def run(self, inputs):
        """Run the code analysis crew"""
        return self.crew.kickoff(inputs=inputs)