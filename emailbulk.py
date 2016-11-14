import smtplib
import os
import csv
import getpass

import datetime

server = smtplib.SMTP('smtp.gmail.com', 587)
csv_file = ""
x = os.listdir(os.getcwd())
print x
for i in x:
    if str(i).endswith(".csv"):
        csv_file = str(i)
        break

print csv_file
receivers_list = []
with open(csv_file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        for i in row:
            if not i == '':
                receivers_list.append(str(i))

print(receivers_list)

email = raw_input("Enter your EMAIL address: ")
password = getpass.getpass("Enter your password: ")
subject = raw_input("Enter the subject of the message: ")
mssg = raw_input("Please Enter the message you want to send: ")
msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % \
      (email, "test99", subject, datetime.date.today().strftime("%B %d, %Y"), mssg)
try:
    server.starttls()
    server.login(email, password)
    server.sendmail(email, receivers_list, mssg)
    server.quit()
    print("Successful")
except:
    print("Unable to connect")
