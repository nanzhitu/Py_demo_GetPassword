#encoding=utf-8
import ConfigParser
import re


DevicdId_file = open('DeviceID.txt')
try:
    DevicdId_lines = DevicdId_file.readlines()
finally:
    DevicdId_file.close()
print len(DevicdId_lines)
print DevicdId_lines


config = ConfigParser.ConfigParser()
config_file = open('config.ini')
try:
    config.readfp(config_file)
finally:
    config_file.close()

username = config.get("Default","username")
password = config.get("Default","password")
device_num = int(config.get("Default","device_num"))
chip = config.get("Default","chip")
config.set("Default","device_num",len(DevicdId_lines))

config_file = open('config.ini','w')
try:
    config.write(config_file)
finally:
    config_file.close()


temp = re.split(':',chip)
print username
print password
print device_num
print chip, temp,len(temp)




deviceId_list = []
for i,line in enumerate(DevicdId_lines):
    if i >= device_num:
        print i, line[:-2]
        deviceId_list.append(line[:-2])
print deviceId_list


password_list = ['1111','2222','3333','4444','5555','6666']
if len(deviceId_list) > 0:
    Password_file = open('Password.txt','a+')
    try:
        for i,j in enumerate(deviceId_list):
            Password_file.write(j+' '+password_list[i]+'\n')
    finally:
        Password_file.close()
else:
    print "nothing update!"
