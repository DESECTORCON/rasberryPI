import smtplib, logging, datetime, imaplib
import email
AUTH_EMAIL_SENDER = 'choeminjun@naver.com'

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
        self.mailSever = imaplib.IMAP4_SSL("smtp.gmail.com", 993)


    @staticmethod
    def __loggerSetup__():
        logging.basicConfig(filename='logging.txt', level=logging.DEBUG)
        logging.debug('--------------MailReaderAPP----------------')

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
            logging.info('Trying to connect to gmail sever...')
            self.mailSever.login(self.myEmail, self.myPassword)
            logging.info('selecting inbox...')
            self.mailSever.list()
            self.mailSever.select('inbox')

            unread_emails = []
            logging.info('getting unseen emails...')
            result, data = self.mailSever.uid('search', None, "UNSEEN")  # (ALL/UNSEEN)
            i = len(data[0].split())

            for x in range(i):
                logging.info('Decoding unseen email' + str(x))
                latest_email_uid = data[0].split()[x]
                result, email_data = self.mailSever.uid('fetch', latest_email_uid, '(RFC822)')
                # result, email_data = conn.store(num,'-FLAGS','\\Seen')
                # this might work to set flag to seen, if it doesn't already
                raw_email = email_data[0][1]
                raw_email_string = raw_email.decode('utf-8')
                email_message = email.message_from_string(raw_email_string)

                # Header Details
                date_tuple = email.utils.parsedate_tz(email_message['Date'])
                if date_tuple:
                    local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
                    local_message_date = "%s" % (str(local_date.strftime("%a, %d %b %Y %H:%M:%S")))
                email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
                email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
                subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))

                # Body details
                logging.info('getting body details...')
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain":
                        logging.info('getting body details of '+ str(part))
                        body = part.get_payload(decode=True)
                        unread_emails.append({'Body': body.decode('utf-8'), 'sender': email_from})
                    else:
                        continue
            try:
                logging.info('returning resaults...')
                unread_email_ = []
                for i in unread_emails:
                    if i['sender'] == '최민준 <choeminjun@naver.com>':
                        unread_email_.append(i)

                return unread_email_
            except:
                return None

        except Exception as E:
            logging.error('Error while finding latest email' + str(E))
            return 'Sever email read error:' + str(E)

    def end_connection(self):
        self.mailSever.close()
        logging.info('-----------Program Exited-------------')

