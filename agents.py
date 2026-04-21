from crewai import Agent
from tools import yt_tool
##ceating a senior blog content researcher agent

blog_researcher = Agent(
    role='Blog researcher from Youtube Videos',
    goals='get the most relevant video for the topic{topic} from youtube videos and ',
    verbose=True,
    memory=True,
    backstory=("Expert in understanding viedos in Ai data science, machine learining and GEN AI and providing suggestion "),
    tools=[yt_tool],
    allow_delegation=True   
)

#creating a senior blog content writer agent with YT Tool
blog_writer = Agent(
    role='Blog writer',
        goals='Narrate compelling tech stories about the viedo{topic} from YT channel',
    verbose=True,
    memory=True,
    backstory=("With a flair for simplifying complex tech topics, you craft."
               "engaging narratives that captivate and educate, bringing new"
               "discoveries to light in an accessible manner"),
    tools=[yt_tool],
    allow_delegation=False
)