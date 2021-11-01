import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *
import datetime
import email
import imaplib
import mailbox

screen = Tk()

screen.resizable( width = False, height = False )
screen.geometry( '410x230' )
screen.title( 'Spam to mail' )

# Fucntion
def send_mail( event ):
	L = login.get()
	P = password.get()
	U = url.get()
	To = toaddr.get()
	T = topic.get()
	M = mess.get()
	N = number.get()

	for value in range(int(N)):
		msg = MIMEMultipart()

		msg['Subject'] = T
		msg['From'] = L
		body = M
		msg.attach(MIMEText(body, 'plain'))

		server = root.SMTP_SSL(U, 465)
		server.login(L, P)
		server.sendmail(L, To, msg.as_string())
		server.quit()

		value += 1
		


def accept_mail():
    L = login.get()
    P = password.get()
    U = url.get()

    mail = imaplib.IMAP4_SSL(U, 993)
    mail.login(L, P)
    mail.list()
    mail.select('inbox')
    result, data = mail.uid('search', None, "UNSEEN")
    i = len(data[0].split())

    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')

        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)

        date_tuple = email.utils.parsedate_tz(email_message['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            local_message_date = "%s" % (str(local_date.strftime("%a, %d %b %Y %H:%M:%S")))
        email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
        email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
        subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))

        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                file_name = "email_" + str(x) + ".txt"
                output_file = open(file_name, 'w')
                output_file.write("From: %s\nTo: %s\nDate: %s\nSubject: %s\n\nBody: \n\n%s" % (
                    email_from, email_to, local_message_date, subject, body.decode('utf-8')))
                output_file.close()
            else:
                continue






# Events
Tlogin = Label( text = 'Login:', font = 'Consolas' )
login = Entry( screen, font = 'Consolas' )

Tpassword = Label( text = 'Password:', font = 'Consolas' )
password = Entry( screen, font = 'Consolas', show = '*' )

Turl = Label( text = 'URL:', font = 'Consolas' )
url = Entry( screen, font = 'Consolas' )

Ttoaddr = Label( text = 'Кому:', font = 'Consolas' )
toaddr = Entry( screen, font = 'Consolas' )

Ttopic = Label( text = 'Topic message:', font = 'Consolas' )
topic = Entry( screen, font = 'Consolas' )

Tmess = Label( text = 'Message:', font = 'Consolas' )
mess = Entry( screen, font = 'Consolas' )

Tnumber = Label( text = 'Number of message:', font = 'Consolas' )
number = Entry( screen, font = 'Consolas' )

enter1 = Button( text = 'Send', font = 'Consolas', width = 18 )
enter2 = Button( text = 'Accept', font = 'Consolas', width = 18, command = accept_mail)



# Packers
Tlogin.grid( row = 0, column = 0, sticky = W, padx = 1, pady = 1 )
login.grid( row = 0, column = 1, padx = 1, pady = 1 )

Tpassword.grid( row = 1, column = 0, sticky = W, padx = 1, pady = 1 )
password.grid( row = 1, column = 1, padx = 1, pady = 1 )

Turl.grid( row = 2, column = 0, sticky = W, padx = 1, pady = 1 )
url.grid( row = 2, column = 1, padx = 1, pady = 1 )

Ttoaddr.grid( row = 3, column = 0, sticky = W, padx = 1, pady = 1 )
toaddr.grid( row = 3, column = 1, padx = 1, pady = 1 )

Ttopic.grid( row = 4, column = 0, sticky = W, padx = 1, pady = 1 )
topic.grid( row = 4, column = 1, padx = 1, pady = 1 )

Tmess.grid( row = 5, column = 0, sticky = W, padx = 1, pady = 1 )
mess.grid( row = 5, column = 1, padx = 1, pady = 1 )

Tnumber.grid( row = 6, column = 0, sticky = W, padx = 1, pady = 1 )
number.grid( row = 6, column = 1, padx = 1, pady = 1 )

enter1.grid( row = 7, column = 0, padx = 1, pady = 1 )
enter2.grid( row = 7, column = 1, padx = 1, pady = 1)


# Bind
enter1.bind( '<Button-1>', send_mail )
enter2.bind( '<Button-2>', )


# The end
screen.mainloop()