fromAddress = 'toreadl@gmail.com'
toAddress = 'joaovitor.martins@gmail.com'

import socket
import smtplib
from smtplib import SMTP
from email.MIMEText import MIMEText

try:
	smtp = SMTP()
	print("Before connection...")
	smtp.connect('smtp.gmail.com')
	smtp.starttls() 
	smtp.ehlo()
	print("After connection...")
	smtp.login('toreadl@gmail.com', 'codify')
	
	# Open a plain text file for reading.  For this example, assume that
	# the text file contains only ASCII characters.
	# fp = open('textfile.txt', 'rb')
	# Create a text/plain message
	# msg = MIMEText(fp.read())
	# fp.close()
	
	msg = MIMEText("Este eh o conteudo. Motherfucker! Base para o plugin criada!")
	msg['Subject'] = '[ToRead] Daily Reading'
	msg['From'] = 'ToRead Later'
	msg['To'] = toAddress;
	msg['Content-Type'] = 'text/plain';
	smtp.sendmail(fromAddress, toAddress, msg.as_string())
	smtp.quit()
	
except (smtplib.SMTPException, socket.error), arg:
    print "SMTP Server could not send mail", arg