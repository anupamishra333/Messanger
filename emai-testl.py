import email
import smtplib
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
import tweepy
from twilio.base.exceptions import TwilioRestException
from twilio.rest import TwilioRestClient

print (".......... Welcome..........")

print("Enter your email details")
your_mailAdd = input("Your email id \n")
pass_adr = getpass.getpass()


print ("Enter SMS details")

ACCOUNT_SID = input("Your account id\n")
AUTH_TOKEN = input("Your authentication token\n")
fromNum = input("Your number\n")

print("Enter Twitter account details")

ACCESS_TOKEN = input("Your access_token\n");
ACCESS_SECRET = getpass.getpass("Your access token secret\n");
CONSUMER_KEY = input("Your consumer key\n");
CONSUMER_SECRET = getpass.getpass("YOur consumer secret");

exit_input = input("To exit type EXIT, else press any key\n")

while(exit_input != 'EXIT' and exit_input != 'exit'):
	print ("Email - [1]   SMS - [2]  Twitter - [3]")
	number = int(input("Select any one above\n"))
	if(number == 1):
		rec_adr = input("Enter receiver's email\n")
		msg= MIMEMultipart()
		subj=input("Subject:")
		msg['From']=your_mailAdd
		msg['To']=rec_adr
		msg['Subject']=subj
			
		print ("Enter body of email")
		body = input("Text you want to enter: ")
		
		msg.attach(MIMEText(body,'plain'))
		
		inp_att = input("Do you want to attach any file? y/n")
		if(inp_att == 'y'):
			strings = input("Enter file address\n")
			if(strings != ''):
				attachment = open(strings,'rb')
				part = MIMEBase('application','octet-stream')
				part.set_payload((attachment).read())
				encoders.encode_base64(part)
				part.add_header('Content-Disposition',"attachment; filename = %s" % strings)
				msg.attach(part)

		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(your_mailAdd,pass_adr)
		text = msg.as_string()
		server.sendmail(your_mailAdd,rec_adr,text)
		server.quit()

	elif(number == 2):
		client = TwilioRestClient(ACCOUNT_SID,AUTH_TOKEN)

		ToNum = input("Enter the number you want to send SMS \n");
		bodytext = input("Enter text you want to enter\n")
		try:
			client.messages.create( to = '+91'+ToNum, from_ = '+' + fromNum, body = bodytext)
		except TwilioRestException as e:
			if(e.code == 21212):
				fromNum = input("Enter your correct no")
			elif(e.code == 21608):
				print("Verify the no ")
			elif(e.code == 20003):
				ACCOUNT_SID = input("Enter correct acc SID")
				AUTH_TOKEN = input("Enter correct acc token")
			else:
				print ("Error occured.. Try again!")

	elif(number == 3):
		auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET);
		auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET);
		print ("Enter your tweet\n")
		tweet= input("write a post:");
		status = tweepy.API(auth).update_status(status=tweet);
			
	exit_input = input("To exit type EXIT, else press any key\n")

print("THank you for using Messenger! :) ");
