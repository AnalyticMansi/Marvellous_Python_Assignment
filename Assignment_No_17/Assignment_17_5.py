import time
import schedule
import datetime

def MySchecule():
    print("Current time :-",datetime.datetime.now())


    fobj = open("Marvellous.txt","a")
    fobj.write("Current time :- " + current_time + "\n")
    fobj.close()

def main():

    print("Inside the main function")

    schedule.every(5).minutes.do(MySchecule)

    
    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ =="__main__":
    main()