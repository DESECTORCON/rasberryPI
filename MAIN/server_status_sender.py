from rasberryPI.MailSender.SendMail_ras import MailSenderAPP, MailReaderAPP
# mailsender = MailSenderAPP(my_email='SE.servicesemail.com@gmail.com', my_password=input('give_value   '), )
# mailsender.__loggerSetup__()
# mailsender.connect_to_server()
# statuc = mailsender.EmailSender(['choeminjun@naver.com'], 'Hey')
# mailsender.end_connection()
# print(statuc)

mailsender = MailReaderAPP(my_email='SE.servicesemail.com@gmail.com', my_password=input('give_value   '), )
mailsender.__loggerSetup__()
mailsender.connect_to_server()
statuc = mailsender.read_latest_mail_and_command()
# mailsender.end_connection()
print(statuc)
