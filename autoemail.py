import smtplib #here we are using the smptp library
server=smtplib.SMTP('smtp.gmail.com', 587) #in this line we are using the domain and port
server.starttls()  #here we are using tls security for the email

server.login('vvcetest@gmail.com', 'nbqlqkibnsozfthr') #here we are calling function smtp to login
server.sendmail('vvcetest@gmail.com', 'puneethm79@gmail.com', 'Email test')
                    #sender mail            #reciver mail           #message to the reciver
print("Mail sent Successfully") #this message to check the mail was sent


