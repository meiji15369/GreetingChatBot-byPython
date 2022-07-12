import datetime
import os
import pya3rt
# Windows環境で必要な設定※
import locale
locale.setlocale(locale.LC_ALL, '') 
import jtalk

def send_message(message):
    apikey = "API" 
    client = pya3rt.TalkClient(apikey)
    reply_message = client.talk(message)
    print(reply)
    return reply_message['results'][0]['reply']

path ='C:\\kadai pro\\pychat\\greeting\\user.txt'
if not os.path.exists(path):
    #jtalk.jtalk(u'ユーザー名を教えてね')
    #user = input("ユーザー名> ")
    user = 'ur name'
    f=open(path, 'x')
    f.write(user)
    encount =1
    jtalk.jtalk(user + "さんですね！"+"よろしくおねがいします")
else:
    f = open(path,'r')
    #user=f.readline()#名前取得
    #user=user.replace("\n","")
    user = 'ur name'
    #encount=int(f.readlines())+ 1 #あった回数
    #log=datetime.datetime.strptime(f.readlines()[2]) #最後の会話時間
    f.close()
    
    #if encount <=10:
    jtalk.jtalk(user +"おかえりなさい!")
    print(user + "さん！"+"おかえりなさい!")
    """""
    else :
        jtalk.jtalk(user + "だ!"+"おかえり!")
    #if (datetime.datetime.now - log)>=datetime(0000,0,0,0,1):
        #jtalk.jtalk("久しぶり!"+"待ってたよ")"""

w=open(path,'w')
#w.writelines(user)[0]
w.write(user +"\n")
w.close

while True :
    #jtalk.jtalk(u'聞きたいことはありますか？')
    user_uttr = input("入力> ")
    #if user_uttr == "何時" in user_uttr  or "時刻"in user_uttr or "時間"in user_uttr:
    if "何時" in user_uttr  or "時刻"in user_uttr or "時間"in user_uttr or "じかん"in user_uttr:
        jtalk.jtalk("現在時刻ですね！")
        jtalk.say_datetime()
    elif user_uttr=="おやすみ" or user_uttr=="おわり":
        jtalk.jtalk("お話してくれてありがとう。おやすみネ")
        #w.write(user +"\n")
        #w.write(str(encount) +"\n")
        #w.write(str(datetime.detetime.now()))
        #w.writelines(encount +1)[1]
        #w.writelines(datetime.datetime.now())[2]
        
        break
    elif "について教えて" in user_uttr or "ついて調べて" in user_uttr:
        sep = 'について教えて'
        t = user_uttr.split(sep)
        r=t[0]
        #jtalk.jtalk("今調べてるから少し待ってネ")
        a=jtalk.wikipediaSearch(r)
        a=a.replace("\n","")
        print("「"+a +"」"+"のことだよ")
        jtalk.jtalk(a + "のことだよ")
        #print("すみません、わかりません。")
        #break
    else:
        reply = send_message("こんにちわ")
        #reply = "こんにちわ"
        print(reply)
        jtalk.jtalk(reply)