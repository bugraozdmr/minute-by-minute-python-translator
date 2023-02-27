#saatlik-dakikaklık artık ne isterseniz mailinize kelime + anlamı gönderecek program

from smtplib import SMTP
from datetime import datetime

from googletrans import Translator, constants

#simple mail transfer protokolu
#Basit mail göndermek için kullanılır.
try:
    translator = Translator()
    with open(r"your path","r+",encoding="utf-8") as file:
        lines = file.readlines()


    for line in lines:
        if "\n" in line:
            line = line[:-1]
        
        while True:
            
            now = datetime.now()
            print(now.second)
            if now.second == 13:
                break

        if line == "":
            
            break
        
        translation = translator.translate(line,src="en",dest="tr")
        
        # mail mesaj bilgisi
        subject = "dakikalık kelime"
        message = "{}\t--\t{}".format(line,translation.text)
        content = "Subject: {0}\n\n{1}".format(subject,message)

        #gönderici hesap bilgileri
        mymail = "your mail"
        password = "your application mail password"        #google uygulama için şifre veriyor !!

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
