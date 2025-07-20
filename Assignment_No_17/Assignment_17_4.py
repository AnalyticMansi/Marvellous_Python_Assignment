import time
import schedule

def MyDay():
    print("Namskar")

def main():

    print("Inside Main fucntion ")

    schedule.every().day.at("09:00").(MyDay)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()