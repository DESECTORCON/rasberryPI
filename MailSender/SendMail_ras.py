import smtplib, logging, datetime


class MailSenderAPP(object):

    def __init__(self, my_email, my_password):
        self.myEmail = my_email
        self.myPassword = my_password
        # Emailsuq = email
        # self.Subject = subject

    @staticmethod
    def __loggerSetup__():
        logging.basicConfig(filename='SendMail_rasLOG.log', level=logging.DEBUG)

    def EmailSender(self, Emailsuq, subject):
        logging.info('--------Program Starting at:%s.-------------' % (datetime.datetime.now()))
        try:
            logging.info('Trying to connect to gmail sever...')
            mailSever = smtplib.SMTP("smtp.gmail.com", 587)
            mailSever.ehlo()
            mailSever.starttls()
            logging.info('connect to sever:success')
        except Exception as Error:
            logging.error('Cant connect to gmail sever. Error messge:' + str(Error))
            return 'Sever connect Error:' + str(Error)

        try:
            logging.info('Trying to login With Email and password...')
            mailSever.login(self.myEmail, self.myPassword)
            logging.info('logining to gmail sever:success')
        except Exception as Error:
            logging.error('Cant login to gmail sever. Error messge:' + str(Error))
            return 'Login Error:' + str(Error)


        try:
            logging.info('Sending mail to %s...' % (Emailsuq))
            Email_number = 0
            for email in Emailsuq:
                mailSever.sendmail(self.myEmail, email, subject)
                Email_number += 1
            logging.info('Sending mail to %s:success' % (Emailsuq))
        except Exception as Error:
            logging.info('Cant Send mail to %s. Error messge:'+str(Error))
            return 'Mail sending Error:' + str(Error)

        mailSever.close()
        logging.info('-----------Program Exited-------------')
        return True
#
#
# def main(my_email, my_password, email=[], subject='Subject:SE\nTyto alab'):
#     MailSenderAPP.__loggerSetup__()
#     status = MailSenderAPP(my_email, my_password, email, subject).EmailSender()
#
#     return status
