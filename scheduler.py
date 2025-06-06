import schedule
import time
from main import run_daily_post

# Schedule daily at 10:00 AM
schedule.every().day.at("10:00").do(run_daily_post)

print("Scheduler is running...")
while True:
    schedule.run_pending()
    time.sleep(60)
