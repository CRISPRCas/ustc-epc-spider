import json
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr, parseaddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def SendEmail(sender, pswd, server, receiver, msg):
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = _format_addr('EPC-BOT <%s>' % sender)  # 发送者
    message['To'] = receiver    # 接收者
    message['Subject'] = Header("EPC选课通知", 'utf-8')

    try:
        smtp = smtplib.SMTP_SSL(server, 465)
        smtp.login(sender, pswd)
        smtp.sendmail(sender, receiver, message.as_string())
        smtp.quit()
    except:
        smtp.connect(server, 25)
        smtp.login(sender, pswd)
        smtp.sendmail(sender, receiver, message.as_string())
        smtp.quit()
        return False
    return True

if __name__=='__main__':
	json_str = ''
	with open('config.json') as f:
		json_str = f.read()
	js = json.loads(json_str)

	mailsender = js['sender.user']
	mailpswd = js['sender.passwd']
	mailserver = js['sender.mailserver']
	mailreceiver = js['receiver.user']

	if SendEmail(sender=mailsender, pswd=mailpswd, server=mailserver, receiver=mailreceiver, msg='TEST!'):
		print('ok.')
	else:
		print('Not ok.')
