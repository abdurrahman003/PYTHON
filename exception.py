import smtplib
import getpass
s=smtplib.SMPT('smtp.gmail.com','587')
s.starttls()
sender='superabdur3@gmail.com'
receiver='abishekabi673@gmail.com'
msg="get lost stupid fellow"
p=getpass.getpass()
s.login(sender,p)
s.sendmail(sender,receiver,msg
print("message sent successfully")
s.quit()