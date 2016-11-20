import smtplib

class MailSenderAPP():

    def __init__(self, my_email, my_password, email=[], subject='Subject:SE\nTyto alab'):
        self.myEmail = my_email
        self.myPassword = my_password
        self.Emailsuq = email
        self.Subject = subject

    def EmailSender(self):
        mailSever = smtplib.SMTP("smtp.gmail.com", 587)
        mailSever.ehlo()
        mailSever.starttls()
        mailSever.login(self.myEmail, self.myPassword)
        for email in self.Emailsuq:
            mailSever.sendmail(self.myEmail, email, self.Subject)

        mailSever.close()
        return True


MailSenderAPP('choeminjun5627@gmail.com', input('password:'), \
            ['choeminjun@naver.com', 'jckcj@naver.com'], 'Subject:hello\nHello?').EmailSender()