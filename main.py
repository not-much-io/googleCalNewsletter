from sendMail import Mailer
from time import sleep

if __name__ == '__main__':

    for i in range(100):
        newMail = Mailer("Make a repo!", "Sent by this evil script: https://github.com/not-much-io/googleCalNewsletter")
        newMail.send_mail()
        print("Sent email nr. " + str(i))
        sleep(15)
    print("Done!")





