##################### Extra Hard Starting Project ######################
import pandas as pd
from datetime import datetime
import random
import pytz
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

smtp_server = "smtp.gmail.com"
smtp_port = 587
my_email = "sampagaellejun.dev@gmail.com"
my_password = "mble fntc ttyl cvlw" # You can get this on google app password
receiver_email = "kuzikun6@gmail.com"

PLACEHOLDER = "[Name]"
TIMEZONE = pytz.timezone("Asia/Manila")

with open("greetings1.txt", "r") as file1, open("greetings2.txt", "r") as file2, open("greetings3.txt", "r") as file3:
    greetings1 = file1.read()
    greetings2 = file2.read()
    greetings3 = file3.read()

    all_greetings = [greetings1, greetings2, greetings3]
    get_letter_randomly = random.choice(all_greetings)

df = pd.read_csv('birthdays.csv')


date_now = datetime.now()
get_month = date_now.strftime("%m")
get_day = date_now.strftime("%d")
# print(f"month: {get_month}")
# print(f"day: {get_day}")

get_names = df['name']
for name in get_names:
    stripped_name = name.strip()
    new_letter = get_letter_randomly.replace(PLACEHOLDER, stripped_name)


def send_email():
    try:
        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = receiver_email
        msg['Subject'] = "It's your birthday!"

        msg.attach(MIMEText(new_letter, 'plain'))
        connection = smtplib.SMTP(smtp_server, smtp_port, timeout=30)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(my_email, receiver_email, msg.as_string())
        connection.close()
    except Exception as error:
        print(f"Failed to send an email: {error}")

    else:
        print("Email sent successfully!")


for index, row in df.iterrows():
    # print(row['month'])
        if row['month'] == int(get_month) and row['day'] == int(get_day) :
            send_email()













# 1. Update the birthdays.csv



# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




