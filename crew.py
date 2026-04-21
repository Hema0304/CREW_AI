from crewai import Crew,Process
from agents import blog_researcher, blog_writer

from tasks import research_task, writing_task


##creating a crew
crew=Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

#task execution
result=crew.kickoff(input={'topic':'AI VS ML VS DL VS Data Science'})

print(result)
