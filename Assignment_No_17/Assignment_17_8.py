import schedule
import time
import datetime

def check_email():
    print(f"{datetime.datetime.now()} - Checking for new emails...")

def main():
    print("Starting email check simulation every 10 seconds...")
    schedule.every(10).seconds.do(check_email)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
