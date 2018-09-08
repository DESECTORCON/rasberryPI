import smtplib, logging, datetime


class MailSenderAPP(object):

    def __init__(self, my_email, my_password):
        self.myEmail = my_email
        self.myPassword = my_password
        self.mailSever = smtplib.SMTP("smtp.gmail.com", 587)
        # Emailsuq = email
        # self.Subject = subject

    @staticmethod
    def __loggerSetup__():
        logging.basicConfig(filename='logging.txt', level=logging.DEBUG)

    def connect_to_server(self):
        try:
            logging.info('Trying to connect to gmail sever...')

            self.mailSever.ehlo()
            self.mailSever.starttls()
            logging.info('connect to sever:success')
        except Exception as Error:
            logging.error('Cant connect to gmail sever. Error messge:' + str(Error))
            return 'Sever connect Error:' + str(Error)

    def EmailSender(self, Emailsuq, subject):
        logging.info('--------Program Starting at:%s.-------------' % (datetime.datetime.now()))
        if type(Emailsuq).__name__  != 'list':
            logging.error('Emailsuq have to be a list ,like this: ["blah@blah.com"]')
            return 'Emailsuq have to be a list Error' + str(type(Emailsuq))

        try:
            logging.info('Trying to login With Email and password...')
            self.mailSever.login(self.myEmail, self.myPassword)
            logging.info('logining to gmail sever:success')
        except Exception as Error:
            logging.error('Cant login to gmail sever. Error messge:' + str(Error))
            return 'Login Error:' + str(Error)


        try:
            logging.info('Sending mail to %s...' % (Emailsuq))
            Email_number = 0
            for email in Emailsuq:
                self.mailSever.sendmail(self.myEmail, email, subject)
                Email_number += 1
            logging.info('Sending mail to %s:success' % (Emailsuq))
        except Exception as Error:
            logging.info('Cant Send mail to %s. Error messge:'+str(Error))
            return 'Mail sending Error:' + str(Error)


        return True

    def end_connection(self):
        self.mailSever.close()
        logging.info('-----------Program Exited-------------')

#
#
# def main(my_email, my_password, email=[], subject='Subject:SE\nTyto alab'):
#     MailSenderAPP.__loggerSetup__()
#     status = MailSenderAPP(my_email, my_password, email, subject).EmailSender()
#
#     return status
