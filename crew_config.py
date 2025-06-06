from crewai import Crew, Agent, Task
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
# 
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(api_key=groq_api_key, model_name="llama-3.3-70b-versatile")

# Agents
script_writer = Agent(
    role='Script Writer',
    goal='Create engaging Instagram Reels scripts',
    backstory='Expert in short-form social media content with viral instincts',
    verbose=True,
    llm=llm
)

caption_writer = Agent(
    role='Caption Writer',
    goal='Write creative and trendy captions for Instagram Reels',
    backstory='Social media specialist with a focus on audience engagement',
    verbose=True,
    llm=llm
)

# Tasks
script_task = Task(
    description='Write a short 15-second Instagram Reel script for the topic of the day: {topic}',
    expected_output='Short, punchy script in bullet form',
    agent=script_writer
)

caption_task = Task(
    description='Generate a catchy caption with hashtags for the video script provided',
    expected_output='Instagram caption in less than 2200 characters',
    agent=caption_writer
)

crew = Crew(
    agents=[script_writer, caption_writer],
    tasks=[script_task, caption_task],
    verbose=True
)
