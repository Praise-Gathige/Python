# The Simple Logger

while True:
    activity = input("What happened today? (type 'quit' to exit): ")
    if activity == "quit":
        break
    else:
        with open("diary.txt", "a") as file:
           file.write(activity + "\n")



#Boss Challenge: Timestamped Logs

import datetime
while True:
    activity = input("What happened today? (type 'quit' to exit): ")
    if activity == "quit":
        break
    else:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        with open("diary.txt", "a") as file:
            file.write(timestamp + " " + activity + "\n")