import schedule
import time
import datetime

def MySchedule():

    print("Jay Ganesh......",datetime.datetime.now())

def main():

    print("Inside automation script")

    schedule.every(2).seconds.do(MySchedule)

    print("Application is in waiting state : ")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()