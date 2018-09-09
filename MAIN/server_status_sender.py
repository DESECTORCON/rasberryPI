from rasberryPI.MailSender.SendMail_ras import MailSenderAPP, MailReaderAPP
import re, requests
import threading
import time

MASTER_EMAIL = 'choeminjun@naver.com'
MAIL_SEND_DURATION = 1
RUNSTATUS = True

PASSWORD = input()
mailreader = MailReaderAPP(my_email='SE.servicesemail.com@gmail.com', my_password=PASSWORD, )
mailsender = MailSenderAPP(my_email='SE.servicesemail.com@gmail.com', my_password=PASSWORD, )
mailreader.__loggerSetup__()
mailsender.__loggerSetup__()
mailsender.connect_to_server()
mailreader.connect_to_server()

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
def has_numbers(input_string): return any(char.isdigit() for char in input_string)

def get_status(ip):
    res = requests.get("http://" + ip + "/sys/info/get/to__/esa_key_/20fefskdnfWwefwejfjwo¥")
    return res.json()

def send_status():
    status = get_status('167.99.66.234:5000')
    mailsender.EmailSender(['choeminjun@naver.com'], '''
    server status: 167.99.66.234:5000
    cpu_percent: %s
    cpu_count: %s
    disk_usage: %s
    ram(avaible/in bytes): %s
    ''' % (str(status['cpu']), str(status['cpu_count']), str(status['disk_usage']), str(status['ram'])))


def getting_reademail():
    global MAIL_SEND_DURATION, MASTER_EMAIL, RUNSTATUS

    while RUNSTATUS:
        statuc = mailreader.read_latest_mail_and_command()
        print(statuc)
        print(MAIL_SEND_DURATION)
        for i in statuc:
            if 'shutdown' in i['Body']:
                mailreader.end_connection()
                RUNSTATUS = False

                mailsender.EmailSender([MASTER_EMAIL],
                                       'Please send one number (only minutes) ext(100)')
                break

            elif 'change duration' in i['Body']:
                if has_numbers(i['Body']):
                    numbers = re.findall(r'\d+', i['Body'])

                    if len(numbers) > 1:
                        mailsender.EmailSender([MASTER_EMAIL],
                                                'Please send one number (only minutes) ext(100)')
                        continue
                    else:
                        MAIL_SEND_DURATION = int(numbers[0])
                        continue
                else:
                     continue

            elif 'send now' in i['Body']:
                send_status()
    time.sleep(1)


def sender_mail():
    global MAIL_SEND_DURATION, MASTER_EMAIL, RUNSTATUS

    while RUNSTATUS:
        send_status()
        time.sleep(MAIL_SEND_DURATION * 60)

def main():
    threads = []
    t = threading.Thread(target=sender_mail)
    t2 = threading.Thread(target=getting_reademail)
    threads.append(t)
    threads.append(t2)
    t.start()
    t2.start()


if __name__ == '__main__':
    main()
