from rasberryPI.MailSender.SendMail_ras import MailSenderAPP
mailsender = MailSenderAPP(my_email='SE.servicesemail.com@gmail.com', my_password=input('give_value   '), )
mailsender.__loggerSetup__()
statuc = mailsender.EmailSender(['choeminjun@naver.com'], 'Hey')
print(statuc)
