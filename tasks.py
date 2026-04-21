from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

##REsearch task
research_task = Task(
    description=("identify the viedo{topic}."
    "get detailed information about the viedo from the channel."
),
    expected_output='A comprehensive # paragraph long report based on the {topic} of viedo content',
    tools=[yt_tool],
    
    agent=blog_researcher
)

##writing task
writing_task = Task(
    description=(
        "get the info from the youtube channel on the topic{topic}."),
    expected_output='Summarize the info from the youtube channel viedo on the topic{topic} and create the content for the blog',
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'
    )