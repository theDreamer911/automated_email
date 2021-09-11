#################################################
################### MODULE ######################
#################################################
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
#################################################

####################################
########## INFORMATION #############
####################################
SENDER = 'XXXXXXXXXXXXXXX@gmail.com'
PASSWORD = 'XXXXXXXXXXXXXXXXXXXXXX'
RECIPIENT = input("Recipient Email: ")
####################################

#########################################
############### MESSAGE #################
#########################################
SUBJECT = input("Title of email: ")
message = input("Your Message: ")
MESSAGE = f"""
{message}
"""
#########################################


##########################################
############ EMAIL FORMAT ################
##########################################
msg = MIMEMultipart()
msg['From'] = f'"{SENDER.split("@")[0].title()}" <{SENDER}>'
msg['To'] = RECIPIENT
msg['Subject'] = SUBJECT
msg.attach(MIMEText(MESSAGE))
##########################################


##############################################################
###################### SENDING EMAIL #########################
##############################################################
try:
    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.ehlo()
    mail_server.login(SENDER, PASSWORD)
    mail_server.sendmail(SENDER, RECIPIENT, msg.as_string())
    mail_server.close()
    print("Email Sent!")
except:
    print("Something Went Wrong...")
##############################################################
