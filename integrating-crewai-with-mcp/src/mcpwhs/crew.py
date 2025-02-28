from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from mcpwhs.tools.mcp_tools import get_mcprun_tools

mcpx_tools = get_mcprun_tools()

@CrewBase
class PIAIC():
    """PIAIC crew powered by Gemini API integration"""

    # Paths to your YAML configuration files
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def zookeeper(self) -> Agent:
        return Agent(
            config=self.agents_config['zookeeper'],
            verbose=True
        )
    
    @agent
    def social_media_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['social_media_manager'],
            verbose=True,
            tools=mcpx_tools  # Agent gets access to mcp.run (Gemini-powered) tools
        )

    @task
    def write_interesting_stories_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_interesting_stories_task']
        )

    @task
    def publish_blog_posts_task(self) -> Task:
        return Task(
            config=self.tasks_config['publish_blog_posts_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PIAIC crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
