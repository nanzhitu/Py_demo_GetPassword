#encoding=utf-8
from misweb import *
from file_parse import *
from HTMLParser import HTMLParser  

class myparser(HTMLParser):
    def __init__(self):  
        HTMLParser.__init__(self)  
        self.tag = None
        self.data = None
    def handle_starttag(self,tag,attrs):  
        if tag == 'td':
           self.tag = tag
    def handle_data(self,data):  
        #处理 a 标签开头的数据
        if self.tag=='td' and len(data.strip())== 32 :
             self.data = data.strip()
    def getData(self):
        return self.data

def isTrue(chip,deviceId):
    if (i_chip == "648"):
        if (len(j_deviceId) == 22):
            return True
        else:
            return False
    elif (i_chip == "838" or i_chip == "938"):
        if (len(j_deviceId) == 12):
            return True
        else:
            return False
    else:
        return True
        
		
DevicdId_file = open('DeviceID.txt')
try:
    DevicdId_lines = DevicdId_file.readlines()
finally:
    DevicdId_file.close()

DevicdId_Lines_Num = len(DevicdId_lines)


config = Config_read('config.ini')
username = config.get("Default","username")
password = config.get("Default","password")
device_num = int(config.get("Default","device_num"))
chip_o = config.get("Default","chip")
chip = re.split(':',chip_o)

config.set("Default","device_num",DevicdId_Lines_Num)
Config_write('config.ini',config)

print username
print password
print device_num
print DevicdId_Lines_Num
print chip

deviceId_list = []
password_list = {}
for i,line in enumerate(DevicdId_lines):
    if i >= device_num:
        print i, line.strip()
        deviceId_list.append(line.strip())

login_url = "http://misweb.mstarsemi.com.tw/login.php"
#username = "rex.hu"
#password = "mstar123"
#device_id = "D3E826B70CCF"
#chip = "938"
url_o = "http://misweb.mstarsemi.com.tw/module/smart_tv_pw/index.php?action=query_pw&pm_no="

opener = Getcookie(login_url,username,password)
for i_chip in chip:
    for j_deviceId in deviceId_list:
        print len(j_deviceId)
        if isTrue(i_chip,j_deviceId):
            #print i_chip + "  " + j_deviceId
            url =url_o + Chip2num(i_chip)
            data = Getdata(opener,url,j_deviceId)
            #print data
            m = myparser()
            m.feed(data)
            password = m.getData()
            if len(password) == 32
            password_list[j_deviceId]=password
        
print password_list


if len(password_list) > 0:
    Password_file = open('Password.txt','a+')
    try:
        for key in password_list:
            Password_file.write(key+' '+password_list[key]+'\n')
    finally:
        Password_file.close()
else:
    print "nothing update!"








