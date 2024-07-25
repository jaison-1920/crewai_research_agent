from crewai import Task
from datetime import datetime

class AIResearchPaperTask:

    def __init__(self):
        self.current_date = datetime.today().strftime("%Y-%m-%d")

    def Research_Task(self,agent):
        return Task(
            description=(
             """1. Prioratize the latest trends on the topic {topic} for the past 365 days from this day{self.current_date} 
                2. Research about the format {format} and develop a detailed content outline including research paper according to it
                3. Find the relevant images  like graphs, flowcharts, tables etc and it's URL.
                4. Plan the number of pages according to the article and placement of images in the paper
                5. Include SEO keywords and relevant data or sources"""
            ),
            expected_output="A comprehensive content plan document formatted as markdown "
                    "with an outline, audience analysis, "
                    "SEO keywords, images description, and resources. ",
            agent = agent

        )