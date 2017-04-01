#encoding=utf-8
import urllib
import urllib2
import cookielib

def Getcookie(url,user,password):
    #登陆页面，可以通过抓包工具分析获得，如fiddler，wireshark
    login_page = url #"http://misweb.mstarsemi.com.tw/login.php"
    try:
        #获得一个cookieJar实例
        cj = cookielib.CookieJar()
        #cookieJar作为参数，获得一个opener的实例
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        #伪装成一个正常的浏览器，避免有些web服务器拒绝访问。
        opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
        #生成Post数据，含有登陆用户名密码。
        data = urllib.urlencode({"username":user,"password":password})
        #以post的方法访问登陆页面，访问之后cookieJar会自定保存cookie
        opener.open(login_page,data)
        return opener
    except Exception,e:
        print str(e)

def Getdata(opener,url,device_id):
    values = {"customer":"skyworth","device_id":device_id,"reason":"debug"}
    data = urllib.urlencode(values)
    op = opener.open(url,data)
    data = op.read()
    return data

def Chip2num(chip):
    num = {
        "A7p"       : "3",
        "muji"      : "14",
        "maserita"  : "25",
        "938"       : "25",
        "maxim"     : "31",
        "838"       : "31",
        "mustang"   : "32",
        "mooney"    : "36",
        "648"       : "36",
        "mainz"     : "38"
        }
    return num.get(chip)
