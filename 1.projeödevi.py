from operator import index
import pandas as pd
import numpy as np
from openpyxl import Workbook


OgrenciAdi_Soyadi =""
Ogrenci_Notu = 0
Ogrenci_Harf_Durumu ="FF"
Ogrenci_Numarasi=""
Ders_Secenegi=""
Ogrenci_G_Durumu=""
indx = 0
Ogrenci_Sayisi=1
try:  
 print("MSY ÖĞRENCİ NOT SİSTEMİNE HOŞ GELDİNİZ!!!")
 print("----------------------------------------------\n ")
 print("İşlem yapılıcak dersi seçiniz : Matematik(1),Fizik(2),Kimya(3),Biyoloji(4),Coğrafya(5),Türkçe(6),Tarih(7)")
 #bu kısım ders seçiminin yapılıp kontrol edildiği kısım
 Ders_Secenegi= int(input())
 while Ders_Secenegi < 1 or Ders_Secenegi > 7:
   print("Yanlış bir seçim yaptınız lütfen derslerin yanlarındaki rakamlarına bakarak seçim yapınız .... \n")
   print("Ders seçiminiz :") 
   Ders_Secenegi= int(input())


 if Ders_Secenegi == 1: Ders_Secenegi = "Matematik"
 elif Ders_Secenegi == 2: Ders_Secenegi ="Fizik"
 elif Ders_Secenegi == 3: Ders_Secenegi ="Kimya"
 elif Ders_Secenegi == 4: Ders_Secenegi ="Biyoloji"
 elif Ders_Secenegi == 5: Ders_Secenegi ="Coğrafya"
 elif Ders_Secenegi == 6: Ders_Secenegi ="Türkçe"
 elif Ders_Secenegi == 7: Ders_Secenegi ="Tarih"

 #-------------------------------------------------------------


#Girilecek öğrenci not sayısı alınması
 print("Öğrenci Sayısı Giriniz : ")
 Ogrenci_Sayisi=int(input())

 while Ogrenci_Sayisi <=0:
   print("Yanlış bir sayı yazdınız öğrenci sayısı 1 den az olamaz, tekrar giriniz....")
   Ogrenci_Sayisi=int(input())

#----------------------------------------
 sutunad = ['  Öğrecinin Adı Soyadı  ','  Öğrencinin Numarası  ','  Öğrencinin Notu ','  Notun Harf karşılığı  ','  Geçme Durumu  ']
 df = pd.DataFrame(columns=sutunad,index= np.arange(0,Ogrenci_Sayisi))
 while Ogrenci_Sayisi >0:
 
    print("Öğrencinin Adını Soyadını Giriniz : ")
    OgrenciAdi_Soyadi=str(input())

    print("Öğrencinin Numarasını Giriniz : ")
    Ogrenci_Numarasi=str(input())
    
   
    


   #öğrencinin notunun alınıp
    print("Öğrencinin Notunu Giriniz : ")
    Ogrenci_Notu=int(input())
     
    while Ogrenci_Notu <0 or Ogrenci_Notu>100:
      print("Yanlış bir sayı yazdınız öğrencinin notu 0 dan az olamaz ,100 den fazla olamaz, tekrar giriniz....")
      Ogrenci_Notu=int(input())

    if Ogrenci_Notu >= 90 and Ogrenci_Notu<=100:
       Ogrenci_Harf_Durumu  ="AA"
    elif  Ogrenci_Notu < 90 and  Ogrenci_Notu>=85 :
     Ogrenci_Harf_Durumu  ="BA"
    elif  Ogrenci_Notu < 85 and  Ogrenci_Notu>=80:
      Ogrenci_Harf_Durumu  ="BB"
    elif  Ogrenci_Notu < 80 and  Ogrenci_Notu>=75:
      Ogrenci_Harf_Durumu  ="CB"  
    elif  Ogrenci_Notu < 75 and  Ogrenci_Notu>=70:
      Ogrenci_Harf_Durumu  ="CC"
    elif  Ogrenci_Notu < 70 and  Ogrenci_Notu>=65:
     Ogrenci_Harf_Durumu ="DC"
    elif  Ogrenci_Notu < 65 and  Ogrenci_Notu>=60:
     Ogrenci_Harf_Durumu  ="DD"    
    elif  Ogrenci_Notu < 60 and  Ogrenci_Notu>=50:
     Ogrenci_Harf_Durumu ="FD"
    elif Ogrenci_Notu <= 49:
     Ogrenci_Harf_Durumu  ="FF"   
    else: print("Hatalı giriş yaptınız")

    if Ogrenci_Notu >=60:Ogrenci_G_Durumu="Geçti"
    else: Ogrenci_G_Durumu="kaldı"
     #print('Öğrencinin adı : ',OgrenciAdi_Soyadi, ' numarası: ',Ogrenci_Numarasi, ' notu :',Ogrenci_Notu,' harfi : ',Ogrenci_Harf_Durumu,'Geçme durumu :',Ogrenci_G_Durumu)
 
 
 #df = pd.DataFrame([["Öğrencinin Adı Soyadı",OgrenciAdi_Soyadi],["Öğrencinin Numarası",Ogrenci_Numarasi],["Öğrencinin Notu",Ogrenci_Notu],["Notun Harf Karşılığı",Ogrenci_Harf_Durumu],["Öğrencinin Geçme Durumu",Ogrenci_G_Durumu],["Öğrencinin Dersi",Ders_Secenegi]])
 #df =pd.DataFrame(columns=["Öğrencinin Adı Soyadı","Öğrencinin numarası"],data=[OgrenciAdi_Soyadi,Ogrenci_Numarasi])
 
    df.loc[-1] =[OgrenciAdi_Soyadi,Ogrenci_Numarasi,Ogrenci_Notu,Ogrenci_Harf_Durumu,Ogrenci_G_Durumu]

    df.index = df.index + 1  # shifting index
    df = df.sort_index()  # sorting by index
 
    Ogrenci_Sayisi-=1
 

    dosya = df.to_excel('öğrencilerinNotları.xlsx',sheet_name=Ders_Secenegi,index=False,)

except:
   print("Yanlış bir biçimde girdi girdiniz...")