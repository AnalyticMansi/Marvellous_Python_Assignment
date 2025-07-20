import time
import schedule
import datetime

def MySchecule():

    print("Inside MySchedule Function :-",datetime.datetime.now())

def main():

    print("Inside the main function :- ")
    print("Current time is :-",datetime.datetime.now())

    schedule.every(1).minute.do(MySchecule)

    print("End of automation script ")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ =="__main__":
    main()