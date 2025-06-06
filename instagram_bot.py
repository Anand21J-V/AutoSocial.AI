from instagrapi import Client
import os
from dotenv import load_dotenv

load_dotenv()

cl = Client()
cl.login(os.getenv("INSTAGRAM_USERNAME"), os.getenv("INSTAGRAM_PASSWORD"))

def post_reel(video_path, caption):
    cl.clip_upload(
        video_path,
        caption=caption,
        thumbnail=None
    )
