from crewai import Agent


class AIResearchPaperAgent:

    def planner_agent(self):
        return Agent(
            role="Research Paper Planner Agent",
            goal="""Plan accurate and factual content and required style and relevant images
              for the research paper which is to be prepared on this {topic} """,
            backstory=""" You are an experienced researcher and expert in Research paper 
            writing in the field of Artificial Intelligence.You are now working on developing the research paper on
            the topic {topic}.You plan the total layout of the content of the research paper. You design the 
            paper such that the range of pages it needed, amount of past data available based on
            the topic {topic},relevant images and its number and the writing style of the research  paper.""",
            # tools=[],
            allow_delegation=False,
            verbose=True
        )