
import datetime
import smtplib
import email
import ssl
"""
Python Script that will automatically send and email or SMS (or both) to your friend on their birthday and wedding aniversary.
"""

friends_list = [
    {'name': 'Jones', 'Email': 'adids@gmail.com', 'birthday': '27-4-2009', 'phone': '234901234561', 'aniversary': '25-4-2021'},
    {'name': 'Agodo', 'Email': 'puma@gmail.com', 'birthday': '25-5-2017', 'phone': '234901234562', 'aniversary': '27-4-2012'},
    {'name': 'Faith', 'Email': 'fubu@gmail.com', 'birthday': '14-3-1995', 'phone': '234901234563', 'aniversary': '22-6-2013'},
    {'name': 'Atama', 'Email': 'nike@gmail.com', 'birthday': '14-1-1995', 'phone': '234901234564', 'aniversary': '7-12-2014'}
]
# storing the email address and password of the sender
receiver = 'Email'
sender = 'nelsonchampion19@gmail.com'
sender_password = 'password@123'

#create a secure connection with email server and through SSL context object
context = ssl.create_default_context()

try:
    
    # create the SMTP connection
    server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=context)

    # loop through my friend's list
    for friend in friends_list:

        today = datetime.date.today()

        # get the person's birthday
        day,month,_=friend['birthday'].split('-')

        # checking if today is one of my friends birthday
        if day == str(today.day) and month == str(today.month):

            # login to the email account and sending the email
            message = (f"Hi {friend['name']},n\ wish you more fruitful years ahead as you celebrate your birtday")
            server.login(sender, sender_password)
            server.sendmail(sender, receiver, message)   
            print("Email sent!")

except:
        print('something went wrong ...')

# script to send wedding anniversary email to friends
for friend in friends_list: 

    today = datetime.date.today()

    # get the person's aniversary
    day, month, _=friend['aniversary'].split('-')

    # checking if today is one of my friends aniversary
    if day == str(today.day) and month == str(today.month):

        # login to the email account and sending the email
        message = (f"Hi {friend['name']},\n On this special day, we wish you happy aniversary")
        server.login(sender, sender_password)
        server.sendmail(sender, receiver, message)   
        print ("Email sent!")
    else:
        print('something went wrong ...')