import smtplib, logging, datetime, imaplib


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


class MailReaderAPP(object):

    def __init__(self, my_email, my_password):
        self.myEmail = my_email
        self.myPassword = my_password
        self.mailSever = imaplib.IMAP4("smtp.gmail.com")
        self.mailSever.select('inbox')

    @staticmethod
    def __loggerSetup__():
        logging.basicConfig(filename='logging.txt', level=logging.DEBUG)

    def connect_to_server(self):
        try:
            logging.info('Trying to connect to gmail sever...')
            # self.mailSever.starttls()
            logging.info('connect to sever:success')
        except Exception as Error:
            logging.error('Cant connect to gmail sever. Error messge:' + str(Error))
            return 'Sever connect Error:' + str(Error)

    def read_latest_mail_and_command(self):
        try:
            type, data = self.mailSever.search(None, 'ALL')
            mail_ids = data[0]

            id_list = mail_ids.split()
            first_email_id = int(id_list[0])
            latest_email_id = int(id_list[-1])

            for i in range(latest_email_id, first_email_id, -1):
                typ, data = self.mailSever.fetch(i, '(RFC822)')

                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = self.myEmail.message_from_string(response_part[1])
                        email_subject = msg['subject']
                        email_from = msg['from']
                        print('From : ' + email_from + '\n')
                        print('Subject : ' + email_subject + '\n')
        except Exception as E:
            logging.error('Error while finding latest email' + str(E))
            return 'Sever email read error:' + str(E)

    def end_connection(self):
        self.mailSever.close()
        logging.info('-----------Program Exited-------------')

