from crew_config import crew
from video_creator import generate_reel
from instagram_bot import post_reel

def run_daily_post():
    topic = "Motivational Tips"  # or pull from trending API
    results = crew.run({"topic": topic})

    script = results[0]['task_output']
    caption = results[1]['task_output']

    print("[INFO] Generating video...")
    video_path = generate_reel(script)

    print("[INFO] Uploading to Instagram...")
    post_reel(video_path, caption)
    print("[SUCCESS] Reel posted successfully!")

if __name__ == "__main__":
    run_daily_post()  # Or use scheduler.py for auto
