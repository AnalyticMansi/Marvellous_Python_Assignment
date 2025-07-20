import time
import schedule

def MyDayStart():

    print("Lunch Time !")

def MyDayEnd():

    print("Wrap up work....")


def main():

    print("Inside main function")

    schedule.every().day.at("13:00").(MyDayStart)
    schedule.evry().day.at("18:00").(MyDayEnd)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()