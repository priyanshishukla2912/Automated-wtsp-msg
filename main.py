"""twilio
   datetime module
   time modue
   1- twilio client setup
   2-user inputs
   3- scheduling logics
   4- send msgs
"""
#installing required libraries
from twilio.rest import Client
from datetime import datetime , timedelta
import time
# twilio credentials
account_sid = 'AC76a71cdXXXXXXXXXXXXXXXXXXX'
auth_token =  '83974dcXXXXXXXXXXXXXXXXXXXXX'

client =  Client(account_sid , auth_token)

#defining  send msg function

def send_whatsapp_message(recipient_number , message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155XXXXXX' ,   
            body = message_body ,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! message sid{message.sid}')
    except Exception as e:
         print(f'An error occurred: {e}')

#taking user input

name = input("Enter the recipient name: ")
recipient_number = input("Enter the WhatsApp number with country code (e.g., +911234567890): ")
message_body = input(f"enter the msg you want to send to{name}:")

date_str = input("Enter the date to send the message(YYYY-MM-DD)")
time_str = input("Enter the time to send the message(HH:MM in 24 hour format):")

 #string parse time
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")

current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past. please enter a future date and time')
else:
    print(f'message scheduled to be sent to {name} at {schedule_datetime}.')

    time.sleep(delay_seconds)

    send_whatsapp_message(recipient_number, message_body )
