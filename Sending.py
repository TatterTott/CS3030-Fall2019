import smtplib
import os

# checking to see if its true and its working correctly with the current working directory
out = os.path.isdir("C:\\Users")
print(out)

# Once its good then asking the user if he/she wants a copy of his/her character sheet by email.
print("Do you want to receive a copy of your DND charecter sheet by email?")
user = int(input())

# Here are my list of possible answers
Yes = {'yes', 'YES', 'Yes'}
No = {'no', "NO", 'No'}

# the DND maker's email
theCreator = ('theCreatorDNDmaker@uccs.edu')

if Yes:
    print("Please provide your UCCS email?")
    user.email = input()
    user.password = input()

    sent_from = theCreator
    to = user.email
    Subject = "Copy of your DND sheet"
    body = "Enjoy the game with your new character made"

    email_message = """\
    From: %s
    To: %s
    Subject: %s
    %s
    """ % (sent_from, ", ".join(to), Subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user.email, user.password)
        server.sendmail(sent_from, to, email_message)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')

else: No
print("Then good day to you Sir/Madam!")
