import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *

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

	for value in range( int( N ) ):
		msg = MIMEMultipart()

		msg[ 'Subject' ] = T
		msg[ 'From' ] = L
		body = M
		msg.attach( MIMEText( body, 'plain' ) )

		server = root.SMTP_SSL( U, 465 )
		server.login( L, P )
		server.sendmail( L, To, msg.as_string() )
		server.quit()

		value += 1
		

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
enter2 = Button( text = 'accept', font = 'Consolas', width = 18 )



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
enter2.bind( '<Button-2>',  )


# The end
screen.mainloop()
