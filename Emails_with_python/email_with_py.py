import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['Subject'] = "This is sent using Python!"
email['From'] = "arushiagarwalstar@gmail.com"
email['To'] = 'arushiagarwal14@gmail.com'

email.set_content('This is a sample email')

try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('arry.animaget@gmail.com', 'mithi014')
        smtp.send_message(email)
        print("all good")
except:
    print("Ooopss problem!!")