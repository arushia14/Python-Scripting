import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['Subject'] =  # Your email subject
email['From'] = # From whoever
email['To'] = # Email id you want to send the email to

email.set_content('THE CONTENT OF YOUR EMAIL')

try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('YOUR EMAIL USED TO SEND', 'PASSWORD TO YOUR EMAIL ID')
        smtp.send_message(email)
        print("all good")
except:
    print("Error logging in")
