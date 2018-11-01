from email.mime.text import MIMEText
import smtplib
import base64
def send_email():
    # creates the email that is sent and asks for user input for the fields
    msg = MIMEText(input('Enter Your Message ' ))
    msg['Subject'] =input('Subject ' )
    msg['From'] =input('From ' )
    msg['To'] = input('To ')
    return{'raw': base64.urlsafe_b64encode(msg.as_bytes())}

    #creates the smtp packet that uses the gmail smtp server
    s = smtplib.SMTP('smtp.gmail.com', 587)
    #sends the helo or ehlo handshake to the smtp server
    s.ehlo()
    #starts the tls encryption
    s.starttls()
    #asks the user input for their username, and password
    s.login(input('Enter your username:'), input('Enter you password:'))
    #sends the email that was created
    s.sendmail(msg)
    #closes the connection with the smtp server
    s.close()
#calls the function that was created
send_email()
