from crewai import Agent


class AIResearchPaperAgent:

    def Research_Agent(self):
        return Agent(
            role="Researcher Agent",
            goal="""Plan and find  accurate ,factual content and required style and relevant images
              for the research paper which is to be prepared on this {topic} """,
            backstory="""You are an expert Researcher and Research paper planner.You are an expert in designing
              research paper for {topic} in format: {format}. You have amazing talent on selecting relevant
              topics and images. You have an excellent grasp of how a research paper layout should look, the number of 
              images and the placement of images in the paper in the  provided format.""",
            # tools=[],
            allow_delegation=False,
            verbose=True,
            max_iter=15
        )
    
    def Writer_Agent(self):
        return Agent(
            role= "Writer Agent",
            goal=""
        )