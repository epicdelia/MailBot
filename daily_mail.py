import datetime
import calendar 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os.path 
import random, os

now = datetime.datetime.now()

today_date = datetime.date.today()

current_year = now.year
cuttent_month = now.month

def get_random_file(path):
	random_filename = random.choice([x for x in os.listdir(path)
	    if os.path.isfile(os.path.join(path, x))])
	return random_filename 	 

path = "/Users/User/Pictures/DailyDose"
gmailUser = 'leilarae.dailydose@gmail.com'
gmailPassword = 'Weekndmakesmewet69'
recipients = ['mihailistov@gmail.com', 'laza6510@mylaurier.ca']
message='Hey babe, here is your daily dose of Vitamin D ;)'

msg = MIMEMultipart()
msg['From'] = gmailUser
msg['To'] = ", ".join(recipients) 
msg['Subject'] = "Daily Delia Dose"
msg.attach(MIMEText(message))

ImgFileName = get_random_file(path)
img_data = file(path + "/" + ImgFileName, 'rb').read()
image = MIMEImage(img_data, 'jpg', name=os.path.basename(ImgFileName))
msg.attach(image)

mailServer = smtplib.SMTP('smtp.gmail.com', 587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(gmailUser, gmailPassword)
mailServer.sendmail(gmailUser, recipients, msg.as_string())
mailServer.close()



