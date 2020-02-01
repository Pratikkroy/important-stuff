import smtplib
from notify_run import Notify()

def send_mail():
  server = smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login('dev.amlan.99@gmail.com','fzanpwfvxnldiycv')
  subject = "Price of Phillips Trimmer has fallen down below Rs. "+str(dp)
  body = "Hey Amlan! \n The price of Phillips trimmer on AMAZON has fallen down below Rs."+str(dp)+".\n So, hurry up & check the amazon link right now : "+url
  msg = f"Subject: {subject} \n\n {body} "
  server.sendmail(
  'dev.amlan.99@gmail.com',
  'amlansk53@gmail.com',
  msg
  )
  print("HEY AMLAN, EMAIL HAS BEEN SENT SUCCESSFULLY.")
 
  server.quit()
#Now lets send the push notification-------------------------------------------------
def push_notification():
  notify = Notify()
  notify.send(pnmsg)
  print("HEY AMLAN, PUSH NOTIFICATION HAS BEEN SENT SUCCESSFULLY.")
 
  print("Check again after an hour.")