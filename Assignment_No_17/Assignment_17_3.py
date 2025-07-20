import time
import schedule
import datetime

def MyProgram():

    print("DO PROGRAMMING ................")

def main():

    print("Inside main functions")

    schedule.every(30).minutes.do(MyProgram)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()