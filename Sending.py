import smtplib
import os

# checking to see if its true and its working correctly with the current working directory
out = os.path.isdir("C:\\Users")
print(out)

# Once its good then asking the user if he/she wants a copy of his/her character sheet by email.
print("Do you want to receive a copy of your DND charecter sheet by email?")
response = input("Yes or No? ").lower()


# the DND maker`'s email
theCreator = "theCreatorDNDmaker@uccs.edu"

if response == "yes":
    print("Please provide your UCCS email?")
    email = input('Email: ')
    password = input('Password: ')

    sent_from = theCreator
    to = [email] # A list of emails to send to
    subject = "Copy of your DND sheet"
    body = "Enjoy the game with your new character made"

    email_message = f"From: {sent_from}\nTo: {','.join(to)}\nSubject: {subject}\n{body}"

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(email, password)
        server.sendmail(sent_from, to, email_message)
        server.close()

        print("Email sent!")
    except:
        print("Something went wrong...")

elif response == "no":
    print("Then good day to you Sir/Madam!")
else:
    print("I didn't understand that. Good day to you Sir/Madam!")