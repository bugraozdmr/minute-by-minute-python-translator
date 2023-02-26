#saatlik-dakikaklık artık ne isterseniz mailinize kelime + anlamı gönderecek program

from smtplib import SMTP
from datetime import datetime

from googletrans import Translator, constants

#simple mail transfer protokolu
#Basit mail göndermek için kullanılır.
try:
    translator = Translator()
    with open(r"C:\Users\bugra\OneDrive\Masaüstü\translate\wordlist.txt","r+",encoding="utf-8") as file:
        lines = file.readlines()


    for line in lines:
        print(line)
        while True:
            print("2.nokta")
            now = datetime.now()
            print(now.second)
            if now.second == 13:
                break

        if line == "":
            print("4.nokta")
            break
        print("dwd")
        translation = translator.translate(line,src="en",dest="tr")
        print("qwdqwdwqdwdwq")
        # mail mesaj bilgisi
        subject = "dakikalık kelime"
        message = "{}\t--\t{}".format(line,translation.text)
        content = "Subject: {0}\n\n{1}".format(subject,message)

        #gönderici hesap bilgileri
        mymail = "your mail"
        password = "yout mail password"        #google uygulama için şifre veriyor !!

        #kime gonderilecek
        sentto = "your mail"

        mail = SMTP("smtp.gmail.com",587)   #google smtp sunucusu
        mail.ehlo()  #maile bağlandı
        mail.starttls() #şifreli gönderdi mesajı
        mail.login(mymail,password)
        mail.sendmail(mymail,sentto,content.encode("utf-8"))  #encode türkçe karakterlerle sıkıntı çıkmaması için yazıldı.
        print("success")

    print("mail gonderme islemi basarılı")
except Exception as e:
    print("hata aldınız ! {}".format(e))
