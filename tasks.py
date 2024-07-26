from crewai import Task
from datetime import datetime
import os




class AIResearchPaperTask:

    def __init__(self):
        self.current_date = datetime.today().strftime("%Y-%m-%d")

    def Research_Task(self,agent):
        return Task(
            description=(
             """1. Prioratize the latest trends on the topic {topic} for the past 365 days from this
                   day{self.current_date} 
                2. Research about the format {format} and develop a detailed content outline including research paper
                   according to it
                3. Find the relevant images  like graphs, flowcharts, tables etc and it's URL.
                4. Plan the {no_of_pages} pages of research paper according to the article and 
                   placement of images in the paper
                5. Include SEO keywords and relevant data or sources
                6. Consider suitable equations and formulas.
                7. Consider this additional information: {additional_info}"""

            ),
            expected_output="A comprehensive content plan document formatted as markdown "
                    "with an outline, audience analysis, "
                    "SEO keywords, images description, and resources. ",
            
            agent = agent

        )
    
    def Writer_Task(self,agent,context):
        return Task(
            description=(
                """1.From the content recieved from Researcher Agent,write the content, guidelines and outline
                     for the research paper from the findings of Researcher Agent.
                   2. Ensure that the content is relevant to the topic of the research paper.
                   3. Ensure it satisfies the guidelines of the research paper.
                   4. Provide details to fit in  {no_of_pages} pages for the research paper.
                   5. {additional_info} must be satisfied"""
            ),
            expected_output="""A comprehensive content plan document formatted as markdown detailing the format,SEO keywords
            and sources of selected articles""",
            agent= agent,
            async_execution=True,
            context= context,


        )
    
    def Image_selecter_Task(self,agent,context):
        return Task(
            description=(
                """1. Select the appropriate images and its urls from the findings of Researcher Agent
                   2. Ensure that the images are relevant to the topic of the research paper.
                   3. Ensure it satisfies the guidelines of the research paper.
                   """
            ),
            expected_output=""" A comprehensive content image plan document formatted as markdown
              detailing images and its sources. Explanation of uses and importance of Images should be included""",
            agent=agent,
            context=context,
            async_execution=True
        )
        
    def Editor_Task(self,agent,context):
        return Task(
            description=(
                """1.Combine the content plan document by selecting the details 
                of Writer Agent and Image details from Image Selecter Agent. 
                2. Maintain the writing style of Writer Agent and include suggested image details
                from Image Selecter Agent.
                3. After combining if there is any grammer or format error, correct it"""
            ),
            expected_output="""A comprehensive content plan document formatted as markdown
            with an outline, audience analysis, SEO keywords, images description, and resources. """,
            agent=agent,
            context=context,
            async_execution=False
        )

        
        
    