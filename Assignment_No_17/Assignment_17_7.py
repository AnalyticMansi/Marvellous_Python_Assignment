import schedule
import time
import datetime

def backup_file():
    
    f1 = open("data.txt", "r")
    data = f1.read()
    f1.close()

    
    f2 = open("backup_data.txt", "w")
    f2.write(data)
    f2.close()

    
    log = open("backup_log.txt", "a")
    log.write(str(datetime.datetime.now()) + " - Backup completed\n")
    log.close()

def main():
    
    schedule.every(1).hours.do(backup_file)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
