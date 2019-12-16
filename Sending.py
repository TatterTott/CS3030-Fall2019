import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def email(pdf):
    #checking to see if its true and its working correctly with the current working directory
    path = os.getcwd()
    filename = os.path.join(path, pdf)

    # Once its good then asking the user if he/she wants a copy of his/her character sheet by email.
    print("Do you want to receive a copy of your DND character sheet by email?")
    response = input("Yes or No? ").lower()

    # the DND maker`'s email
    theCreator = "theCreatorDNDmaker@uccs.edu"

    while True:

        if response == "yes":
            email = input("Please enter your google email address: ")
            password = input("Please enter your email password: ")

            fromaddr = theCreator
            toaddr = email

            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Copy of your DND sheet"
            body = "Enjoy the game with your new character made"

            msg.attach(MIMEText(body, 'plain'))
            attachment = open(filename, "rb")
            mime = MIMEBase('application', 'octet-stream')
            mime.set_payload((attachment).read())
            encoders.encode_base64(mime)
            mime.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(mime)

            try:
                # creates SMTP session
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server .starttls()
                server .login(email, password)
                text = msg.as_string()
                server .sendmail(fromaddr, toaddr, text)
                server .quit()
                print("Email sent!")
                break

            except:
                print("Something went wrong...")
                print("Do you still want to receive a copy of your DND character sheet by email?")
                response = input().lower()

        elif response == "no":
            break

        else:

            while response != "yes" and response != "no":
                print("That input was not valid. Please enter Yes or No:")
                response = input().lower()
