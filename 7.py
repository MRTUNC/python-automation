from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5.QtCore import pyqtSlot
import time
import os
import sys
import datetime
import sqlite3
import serial
import subprocess
from sutmatik2a import Ui_Form
import smtplib
import ssl

#
#
# bu kodlar okey gelenveri değişkenini talip et
#
#
#


global sira
sira=0
global deneme
deneme=0
global sicaklik
sicaklik="0"
global seriport
global vsut
vsut=0.0
global ld
ld=0
global kalann
kalann=0
global verilen
verilen =0

global pp
pp=1
global gsay
gsay=0
global sicaksayac
sicaksayac=0
global config
config=0
global sifre
sifre=0
def sport():
    #
    try:
        global seriport
        seriport=serial.Serial(port="COM3",baudrate=9600,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE,parity=serial.PARITY_NONE)
        seriport.close()
        if seriport.is_open!=True:
            seriport.open()
        seriport.write(b'trtrtxkxaa')
    except:
        print("seri haberlesme hatasi")

sport()


def veritabaniolustur():
  con=sqlite3.connect("sicaklikverisi.db")
  cursor=con.cursor()
  cursor.execute("create table if not exists durum(sira text,zaman text,sicaklik text,kalan text,verilen text)")
  con.commit()
  con.close()
def veritabaninadegerekle():
  global saat
  global dakika
  global saniye
  
  zaman=datetime.datetime.now()
  yil=zaman.year
  ay=zaman.month
  gun=zaman.day
  saat=zaman.hour
  dakika=zaman.minute
  saniye=zaman.second
  global sira
  
  dosya=open("s.txt")
  sirano=dosya.readlines()
  siradegeri=sirano[0]
  sira=int(siradegeri)
  dosya.close()
  sira=sira+1
  sira=str(sira)

  
  global zaman2
  zaman2=str(yil)+":"+str(ay)+":"+str(gun)+"-"+str(saat)+":"+str(dakika)
  
  con=sqlite3.connect("sicaklikverisi.db")
  cursor=con.cursor()
  cursor.execute("insert into durum('sira','zaman','sicaklik','kalan','verilen') values('"+str(sira)+"','"+str(zaman2)+"','"+str(sicaklik)+"','"+str(kalann)+"','"+str(verilen)+"')")
  con.commit()
  con.close()
  dosya=open("s.txt","w")
  dosya.write(str(sira))
  dosya.close()

veritabaniolustur()
veritabaninadegerekle()




class serii(QThread):
    gelenveri=pyqtSignal(str) # int ve str degiskenler tnaımlanırken signalde
    
    
    def run(self):
        self.inn=0
        while(True):
            ui.label7.setText(str(zaman2))
            time.sleep(0.3)
            try:
                
                gelen=seriport.readline().decode("utf8")
            except:
                print("seri okuma hatasi")
                seriport.close()
                sport()
                gelen="yok"
            global inn
            self.inn=self.inn+1
       
            self.gelenveri.emit(str(gelen))
            gelen2= gelen
            if(gelen!=""):
                pass
                #
                #print("g.:>>>"+str(gelen))
            if(self.inn>15):
                if(pp==1):
                    #
                    tiktok="trtrtxkxaa"
                    seriport.write(tiktok.encode())
                    self.inn=0
                    #print("ping")
                else:
                    print("ping engelli")
                self.inn=0
                
            

            










            
class ping(QThread):
    # veri tabanına degerler eklenecek yer
    
   


  
  
    def run(self):
        #
        veritabaniolustur()
        while(True):
            veritabaninadegerekle()
            for b in range (7):
                
                for c in range(60):
              #
                    time.sleep(1)
                    
    
            




  


            


class xas():
    
    
    
     

    #
    global deneme
    deneme=0


    def __init__(self): 
        import sys
        global app
        global Form
        global ui
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)

        # ui.label.setText("qwe") # bu onemli yularıdaki kodlara dokunmadan degisiklik yapmak
          # asagidaki kodlar hata almamızı saglar
        sys._excepthook = sys.excepthook 
        def exception_hook(exctype, value, traceback):
            print(exctype, value, traceback)
            sys._excepthook(exctype, value, traceback) 
            sys.exit(1) 
        sys.excepthook = exception_hook
        
        c=open("config.txt","r")
        cveri=c.readline()
        cveri2=cveri.split(":")
        if(config==0):
            ui.lineEdit.setText(str(cveri2[1]))
            ui.lineEdit_2.setText(str(cveri2[3]))
            ui.lineEdit_3.setText(str(cveri2[5]))
        c.close()
        
        # butonlarrr
        ui.pushButton.clicked.connect(self.doldur) # doldur
        ui.pushButton2.clicked.connect(self.iptall) # iptal
        ui.pushButton3.clicked.connect(self.yarim) # yarimlitre
        ui.pushButton4.clicked.connect(self.birlitre) # 1 litre
        ui.pushButton5.clicked.connect(self.ikilitre) # 2 litre
        ui.pushButton6.clicked.connect(self.uclitre) # 3 litre
        ui.pushButton7.clicked.connect(self.dortlitre) # 4 litre
        ui.pushButton_8.clicked.connect(self.beslitre) # 5 litre

        ui.pushButton_2.clicked.connect(self.kaydet) # kaydet fonk
        ui.pushButton_3.clicked.connect(self.tarihayarla) # tarih ayarlar fonk
        ui.pushButton_4.clicked.connect(self.mailayarla) # mail ayarlama kodu
        ui.pushButton_5.clicked.connect(self.kaydetsifre) 


        self.verial()
        Form.show()
        def cik():
            seriport.close()
            
            app.exec_()
            quit()

        sys.exit(cik())
        # def init fonk sonu
    def kaydetsifre(self):
        global sifre
        sifre=0
        c=open("config2.txt","r")
        cd=c.readline()
        c.close()
        
        sifretext=ui.lineEdit_12.text()
        if(sifretext==cd):
            sifre=1
            ui.lineEdit_12.setText("aktif")
        else:
            ui.lineEdit_12.setText("hatali")
            
        
            
            
        
    
    def mailayarla(self):
        self.gondericimail=ui.lineEdit_9.text()
        self.gondericisifre=ui.lineEdit_10.text()
        self.hedefmail=ui.lineEdit_11.text()
        mail=open("mail.txt","w")
        mail.writelines("gonderici:"+str(self.gondericimail)+":")
        mail.writelines("sifre:"+str(self.gondericisifre)+":")
        mail.writelines("hedef:"+str(self.hedefmail)+":")
        mail.close()



    def tarihayarla(self):
        self.dakka=ui.lineEdit_4.text()
        self.saat=ui.lineEdit_5.text()
        self.gun=ui.lineEdit_6.text()
        self.ay=ui.lineEdit_7.text()
        self.yil=ui.lineEdit_8.text()
        #os.system("sh "+"/home/pi/Desktop/new.sh")
        #sudo date -s"2020-03-05 18:28:00"
        ayarstr='-s"2020-03-05 18:28:00"'
        ayarstr='-s"'+str(self.yil)+'-'+str(self.ay)+'-'+str(self.gun)+' '+str(self.saat)+':'+str(self.dakka)+':00"'
        
        os.system("sudo date "+ayarstr)
        time.sleep(1)
        os.system("sudo reboot")
    
    def iptall(self):
        global pp
        pp=0
        seriport.write(b'ppppppcccp')
        time.sleep(1)
        seriport.write(b'ppppppcccp')
        time.sleep(0.3)
        seriport.write(b'ppppppcccp')
        ui.pushButton.setStyleSheet("background-color:blue\n")
        ui.pushButton3.setStyleSheet("background-color:blue\n")
        ui.pushButton4.setStyleSheet("background-color:blue\n")
        ui.pushButton5.setStyleSheet("background-color:blue\n")
        ui.pushButton6.setStyleSheet("background-color:blue\n")
        ui.pushButton7.setStyleSheet("background-color:blue\n")
        ui.pushButton_8.setStyleSheet("background-color:blue\n")
        
        
        
        
        pp=1
        
        


    
    def kaydet(self):
        global pulse
        global tankhacmi
        global karistirmadakika
        global pp
        pp=0
        
        
        pulse=ui.lineEdit.text()
        #ui.label_102.setText(str(pulse))
        
        if(sifre==1):
            
            tankhacmi=ui.lineEdit_3.text()
            ui.lineEdit_12.setText("kaydedildi")
            time.sleep(0.5)
        else:
            c=open("config.txt","r")
            cs=c.readline()
            cs2=cs.split(":")
            tankhacmi=cs2[5]
            c.close()
        ui.lineEdit_12.setText("sifre gir")
            
        #ui.label_104.setText(str(tankhacmi))
        karistirmadakika=ui.lineEdit_2.text()
        #ui.label_103.setText(str(karistirmadakika))
        #maxsicaklik=ui.lineEdit_9.text()
        #minsicaklik=ui.lineEdit_10.text()
        ayarverisi=str(karistirmadakika)+str(pulse)+"ae"+str(tankhacmi)
        seriport.write(ayarverisi.encode())
        dosya2=open("kalan.txt","w")
        dosya2.write(str(tankhacmi))
        dosya2.close()
        
        pp=1

        configverisi="pulse:"+str(pulse)+":karistici:"+str(karistirmadakika)+":sutmiktari:"+str(tankhacmi)+":"
        c=open("config.txt","w")
        c.write(str(configverisi))
        c.close()

        
    
        
        
    
    

    def  yarim(self):
        global litrex
        global ld
        global gsay
        global pp
        pp=0
       
       
        
        gsay=gsay+1
        if(gsay==2):

            litrex="55q1zdyyyy"
            ui.pushButton4.setStyleSheet("background-color:blue\n")
            ui.pushButton5.setStyleSheet("background-color:blue\n")
            ui.pushButton6.setStyleSheet("background-color:blue\n")
            ui.pushButton7.setStyleSheet("background-color:blue\n")
            ui.pushButton_8.setStyleSheet("background-color:blue\n")
            ui.pushButton3.setStyleSheet("background-color:orange\n")
            ld=1
            gsay=0
        elif(gsay==1):
            #print("yarim")
            seriport.write(b'atbkotcggg')
            ui.pushButton3.setStyleSheet("background-color:black\n")
        elif(gsay>2) :
            gsay=0
        pp=1
        vsut=0.5
    def birlitre(self):
        
        global litrex
        global ld
        global gsay
        global pp
        pp=0
       
      
        
        gsay=gsay+1
        if(gsay==2):
            litrex="01w1zdyyyy"
            ui.pushButton4.setStyleSheet("background-color:orange\n")
            

            ui.pushButton3.setStyleSheet("background-color:blue\n")
            #ui.pushButton4.setStyleSheet("background-color:blue\n")
            ui.pushButton5.setStyleSheet("background-color:blue\n")
            ui.pushButton6.setStyleSheet("background-color:blue\n")
            ui.pushButton7.setStyleSheet("background-color:blue\n")
            ui.pushButton_8.setStyleSheet("background-color:blue\n")
            ld=1
            gsay=0
        elif(gsay==1):
            
            seriport.write(b'atbkotcggg')
            ui.pushButton4.setStyleSheet("background-color:black\n")
        elif(gsay>2):
            gsay=0

        vsut=1.0
        pp=1
        
    def ikilitre(self):
        global litrex
        global ld
        global pp
        pp=0
        
       
        
        global gsay

        gsay=gsay+1
        if(gsay==2):
            litrex="02e1zdyyyy"
            
            ui.pushButton5.setStyleSheet("background-color:orange\n")

            ui.pushButton3.setStyleSheet("background-color:blue\n")
            ui.pushButton4.setStyleSheet("background-color:blue\n")
            #ui.pushButton5.setStyleSheet("background-color:blue\n")
            ui.pushButton6.setStyleSheet("background-color:blue\n")
            ui.pushButton7.setStyleSheet("background-color:blue\n")
            ui.pushButton_8.setStyleSheet("background-color:blue\n")
            ld=1
            gsay=0
        elif(gsay==1):
            seriport.write(b'atbkotcggg')
            ui.pushButton5.setStyleSheet("background-color:black\n")
        elif(gsay>2):
            gsay=0
        vsut=2.0
        pp=1
        
    def uclitre(self):
        global litrex
        global ld
        global gsay
        global pp
        pp=0
       
     
        
        gsay=gsay+1
        
        if(gsay==1):
            
            seriport.write(b'atbkotcggg')
            ui.pushButton6.setStyleSheet("background-color:black\n")
        elif(gsay==2):
            
            litrex="03r1zdyyyy"
            
            ui.pushButton6.setStyleSheet("background-color:orange\n")

            ui.pushButton3.setStyleSheet("background-color:blue\n")
            ui.pushButton4.setStyleSheet("background-color:blue\n")
            ui.pushButton5.setStyleSheet("background-color:blue\n")
            #ui.pushButton6.setStyleSheet("background-color:blue\n")
            ui.pushButton7.setStyleSheet("background-color:blue\n")
            ui.pushButton_8.setStyleSheet("background-color:blue\n")
            ld=1
            gsay=0
        elif(gsay>2):
            gsay=0
        vsut=3.0
        pp=1
    def dortlitre(self):
        global litrex
        global ld
        global gsay
        global pp
        pp=0
        
    
        
        gsay=gsay+1
        if(gsay==1):
            
            seriport.write(b'atbkotcggg')
            ui.pushButton7.setStyleSheet("background-color:black\n")

        elif(gsay==2):
            
            litrex="04t1zdyyyy"
            
            ui.pushButton7.setStyleSheet("background-color:orange\n")

            ui.pushButton3.setStyleSheet("background-color:blue\n")
            ui.pushButton4.setStyleSheet("background-color:blue\n")
            ui.pushButton5.setStyleSheet("background-color:blue\n")
            ui.pushButton6.setStyleSheet("background-color:blue\n")
            #ui.pushButton7.setStyleSheet("background-color:blue\n")
            ui.pushButton_8.setStyleSheet("background-color:blue\n")
            ld=1
            gsay=0
        elif(gsay>2):
            gsay=0
        vsut=4.0
        pp=1
    def beslitre(self):
        global litrex
        global ld
        global gsay
        global pp
        pp=0
        
       
        
        gsay=gsay+1
        if(gsay==1):
            
            seriport.write(b'atbkotcggg')
            ui.pushButton_8.setStyleSheet("background-color:black\n")
        elif(gsay==2):
            litrex="05u1zdyyyy"
            
            ui.pushButton_8.setStyleSheet("background-color:orange\n")

            ui.pushButton3.setStyleSheet("background-color:blue\n")
            ui.pushButton4.setStyleSheet("background-color:blue\n")
            ui.pushButton5.setStyleSheet("background-color:blue\n")
            ui.pushButton6.setStyleSheet("background-color:blue\n")
            ui.pushButton7.setStyleSheet("background-color:blue\n")
            #ui.pushButton_8.setStyleSheet("background-color:blue\n")
            ld=1
            gsay=0
        elif(gsay>2):
            gsay=0
        vsut=5.0
        pp=1
        
    def doldur(self):
        global ld
        global pp
        global gsay
        pp=0
        ui.pushButton.setStyleSheet("background-color:red\n")
        
        gsay=0
        try:
            if(ld==1):
                #
                self.litregonder=litrex
                seriport.write(litrex.encode())
                ui.pushButton.setStyleSheet("background-color:blue\n")
                ui.pushButton3.setStyleSheet("background-color:blue\n")
                ui.pushButton4.setStyleSheet("background-color:blue\n")
                ui.pushButton5.setStyleSheet("background-color:blue\n")
                ui.pushButton6.setStyleSheet("background-color:blue\n")
                ui.pushButton7.setStyleSheet("background-color:blue\n")
                ui.pushButton_8.setStyleSheet("background-color:blue\n")
                ld=0
                #os.system('sudo sh /home/pi/Desktop/2/launcher.sh')
                #time.sleep(3)
                #subprocess.run(["sudo","python3","/home/pi/Desktop/2/meleme.py"],capture_output=True)
                
            else:
                ui.label9.setText("secim yap")
                ld=0
        except:
            ui.label9.setText("litre ??")
        pp=1
                
        




    ################################ deger atamalar

    def degerata(self,val):
        global pp
        try:
            #ui.label.setText(str(val))
             #print("val[0]:"+str(val[0]))
                # "xk:sicaklik35:xk"
            global verilen
            global kalann
            if(val[0]=="x" and val[1]=="k"):
              sicaklikverisi=val.split(":")
              #print(sicaklikverisi[2])
              ui.label6.setText(str(sicaklikverisi[1])) # sicaklik labeli
              sicaklikkayit=sicaklikverisi[1].split("=")
              global sicaklik
              sicaklik=str(sicaklikkayit[1])
              sica=sicaklik.split("C")
              
             
              sicak=sica[0]
              
              ksicaklik=float(sicak)
              
              ksicaklik=int(ksicaklik)
              #print("sicaklik:"+str(ksicaklik))
              if(ksicaklik>10):
                  #print("aamma")
                  global sicaksayac
                  #print("sayac:"+str(sicaksayac))
                  sicaksayac=sicaksayac+1
                  if(sicaksayac>5):

                      #print("zza")
                      dosya=open("mail.txt","r")
                      mveri=dosya.readline()
                      mveri2=mveri.split(":")
                      #print(mveri2[1])
                      #print(mveri2[3])
                      #print(mveri2[5])

                      #print(mveri)
                      gmail=mveri2[1]
                      gsifre=mveri2[3]
                      hedef=mveri2[5]
                      s=smtplib.SMTP('smtp.gmail.com',587)
                      s.starttls()
                      s.login(str(gmail),str(gsifre)) # gmail > gonderici  
                      mesaj="sutmatik sicakligi 10 derecenin uzerindedir." #+str(ksicaklik)
                      s.sendmail(str(gmail),str(hedef),mesaj)
                      s.quit()
                      dosya.close()
                      sicaksayac=0
                      print("mail gonderildi")



                  

              
              
              
              #print("ssa"+str(kritiksicaklik))
              
            elif(val[0]=="y" and val[1]=="y"):
                #print("yyyyyyyyyyyyyyyyyyy")
                self.sicaklikdurumu=val.split(":")
                #print("sicaklik durumu>>>"+str(self.sicaklikdurumu[1]))
                ui.label8.setText(str(self.sicaklikdurumu[1]))
            elif (val[0]=="k" and val[1]=="l"):
                #print("kalannnnnnnnnnnnn")
                self.kalan=val.split(":")
                ui.label.setText(str(self.kalan[1]))
                kalann=self.kalan[1]
                


            elif(val[0]=="b" and val[1]=="t"):
                ld=0
                ui.pushButton.setStyleSheet("background-color:blue\n")
                ui.pushButton3.setStyleSheet("background-color:blue\n")
                ui.pushButton4.setStyleSheet("background-color:blue\n")
                ui.pushButton5.setStyleSheet("background-color:blue\n")
                ui.pushButton6.setStyleSheet("background-color:blue\n")
                ui.pushButton7.setStyleSheet("background-color:blue\n")
                ui.pushButton_8.setStyleSheet("background-color:blue\n")



                
                '''
                dosya2=open("kalan.txt")
                kalansut=dosya2.readlines()
                kalandeger=float(kalansut[0])
                kalandeger2=kalandeger-vsut
                ui.label.setText(str(kalandeger2))
                dosya2=open("kalan.txt","w")
                dosya2.write(str(kalandeger2))
                dosya2.close()
                '''
              




                
            elif(val[0]=="l" and val[1]=="t"):
                #print("lt>>>>>>>>>>>>>>>")
                self.verilensut=val.split(":")
                ui.label4.setText(str(self.verilensut[1]))
                verilen=self.verilensut[1]
                
            elif(val[0]=="d" and val[1]=="y"):
                self.yazi=val.split(":")
                ui.label9.setText(str(self.yazi[1]))
                if(val[3]=="S" and val[4]=="E"):
                    
                    pp=1
                
            elif(val[0]=="e" and val[1]=="a"):
                if(val[3]=="k" and val[4]=="k"):
                    self.karistirici=val.split(":")
                    ui.label_103.setText(str(self.karistirici[2]))
                    
                elif(val[3]=="c" and val[4]=="c"):
                    self.ccdegeri=val.split(":")
                    ui.label_102.setText(str(self.ccdegeri[2]))
            elif(val[0]=="l" and val[1]=="t"):
                self.kalansut=val.split(":")
                ui.label4.setText(str(self.kalansut[1]))
            
                


            ### gunluk sicaklik verilerini yazdirma##
            #print("saat"+str(saat))
            #print("dakika"+str(dakika))
            #print(type(saat))
            #print(str(sicaklik))
        except:
           #print("komut bekleniyor")
           val="zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
          


    def verial(self):
        self.thread=serii()
        self.thread.gelenveri.connect(self.degerata)
        self.thread.start()
        print("verial fonksiyonu basladi")

        self.thread2=ping()
        self.thread2.start()


    



if __name__ == "__main__":
  xas()
  pingbasla=xas()
  pingbasla.verial()

  
