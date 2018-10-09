 
import smtplib      
from email.mime.text import MIMEText
from email.utils import formataddr
 
mail_server = "smtp.163.com"    
port = "25" 
 
sender = "comp9321assntest@163.com"     # account
sender_passw = "comp9321assntest"         # password
receiver = "lang5119297@gmail.com"      # receiver email
mail_msg = "This is a test."
msg = MIMEText(mail_msg, "plain", "utf-8")      # content, replace plain with html when send html content
msg['From'] = formataddr(["Sender", sender])      # sender info
msg['To'] = formataddr(["receiver", receiver])      # receiver info
msg['Subject'] = "Subject-Test"       # subject
 
def sendMail(mail_server, port, sender,sender_passw, receiver):
    try:
        mail = smtplib.SMTP(mail_server, port)  # or SMTP_SSL()
        mail.login(sender, sender_passw)   
        mail.sendmail(sender, [receiver], msg.as_string() )   # when receiver as list, group send
        mail.quit()
        print("Send Successfully!")
    except:
        mail.quit()
        print("Bad news....")
 
sendMail(mail_server, port, sender, sender_passw, receiver)
