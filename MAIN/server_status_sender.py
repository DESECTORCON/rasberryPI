from rasberryPI.MailSender.SendMail_ras import MailSenderAPP, MailReaderAPP
import re
from multiprocessing.dummy import Pool as ThreadPool

MASTER_EMAIL = 'choeminjun@naver.com'

mailreader = MailReaderAPP(my_email='SE.servicesemail.com@gmail.com', my_password=input('give_value   '), )
mailsender = MailSenderAPP(my_email='SE.servicesemail.com@gmail.com', my_password=input('give_value   '), )

# mailsender.__loggerSetup__()
# mailsender.connect_to_server()
# statuc = mailsender.EmailSender(['choeminjun@naver.com'], 'Hey')
# mailsender.end_connection()
# print(statuc)

# mailsender = MailReaderAPP(my_email='SE.servicesemail.com@gmail.com', my_password=input('give_value   '), )
# mailsender.__loggerSetup__()
# mailsender.connect_to_server()
# statuc = mailsender.read_latest_mail_and_command()
# mailsender.end_connection()
# print(statuc)

# helper functions
def has_numbers(inputString):
     return any(char.isdigit() for char in inputString)

def getting_reademail():
    while True:
        mailreader.__loggerSetup__()
        mailreader.connect_to_server()
        statuc = mailreader.read_latest_mail_and_command()
        mailreader.end_connection()
        for i in statuc:
            if 'shutdown' in i['Body']:
                break

            elif 'change duration' in i['Body']:
                if has_numbers(i['Body']):
                    numbers = re.findall(r'\d+', i['Body'])

                    if len(numbers) > 1:
                        mailsender.__loggerSetup__()
                        mailsender.connect_to_server()
                        statuc = mailsender.EmailSender(['choeminjun@naver.com'],
                                                        'Please send one number (only minutes) ext(100)')
                        mailsender.end_connection()
                        print(statuc)



