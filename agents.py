from crewai import Agent


class AIResearchPaperAgent:

    def Research_Agent(self):
        return Agent(
            role="Researcher Agent",
            goal="""Plan and find  accurate ,factual content and required style and relevant images
              for the research paper which is to be prepared on this {topic} """,
            backstory="""You are an expert Researcher and Research paper planner.You are an expert in designing
              research paper for {topic} in format: {format}.You have to design the paper to fit in {no_of_pages} pages.
              You have amazing talent on selecting relevant topics and images. You have an excellent grasp of how a research
              paper layout should look, the number of images and the placement of images in the paper in the  provided format.
              Your work is the foundation of Writer Agent and Image Agent.""",
            # tools=[],
            allow_delegation=True,
            verbose=True,
            max_iter=15,
        )
    
    def Writer_Agent(self):
        return Agent(
            role= "Writer Agent",
            goal="""Write the content, guidelines and outline for the research paper from the findings of 
              Researcher Agent.""",
              backstory="""You have Years of experience of writing research papers. When you get an outline
               You can actually help the customers by providing accurate information according to the 
               outline. You gather all the information from Reseacher Agent and write the needed content
               according to the outline provided by Researcher Agent.""",
               allow_delegation=True,
               verbose=True,
               
        )
    
    def Image_Selecter_Agent(self):
        return Agent(
            role="Image Selecter Agent",
            goal="""To select the appropriate images and its urls from the findings of Researcher Agent""",
            backstory="""You are an expert Image selecter for Research paper. You know what type of images
            are required for the topic {topic},what type of diagrams are required for the research paper on topic
            {topic}. You are selecting the most appropriate images from the findings of Researcher Agent.""",
            allow_delegation=False,
            verbose=True

        )
    
    def Editor_Agent(self):
        return Agent(
            role="Editor Agent",
            goal="""To edit and finalize the content plan document for the research paper including the details 
            from Writer Agent and Image Selecter Agent.""",
            backstory="""You are an expert in editing and finalizing the content plan document for the research paper.
            You take a close look on the details brought my Writer Agent and Image Selecter Agent. Then including 
            relevant articles and image details, you edit the final output of the content plan document.""",
            allow_delegation=False,
            verbose=True
        )