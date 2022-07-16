#Import Pandas and NumPy
import pandas as pd

# bilgiler icin bos liste yarat
Ad = []
Soyad = []
Okul_no = []
Matematik_puanı = []
kaldı_gecti = []
Matematik_puanii = 0

def harf_notu(puan):
    if 90<=puan<=100:
      print("Tebrikler, AA ile geçtiniz.")
      kaldı_gecti.append("AA")
    elif 85<=puan<=89:
      print("Tebrikler, BA ile geçtiniz")
      kaldı_gecti.append("BA")
    elif 80<=puan<=84:
      print("Tebrikler, BB ile geçtiniz")
      kaldı_gecti.append("BB")
    elif 75<=puan<=79:
      print("Tebrikler, CB ile geçtiniz")
      kaldı_gecti.append("CB")
    elif 65<=puan<=74:
      print("Tebrikler, CC ile geçtiniz")
      kaldı_gecti.append("CC")
    elif 60<=puan<=64:
      print("Tebrikler, DC ile koşullu geçtiniz")
      kaldı_gecti.append("DC")
    elif 55<=puan<=59:
      print("Tebrikler, DD ile koşullu geçtiniz")
      kaldı_gecti.append("DD")
    elif 50<=puan<=54:
      print("Üzgünüz, dersten geçemediniz")
      kaldı_gecti.append("kaldı")
    elif 0<=puan<=49:
      print("Üzgünüz, dersten geçemediniz")
      kaldı_gecti.append("kaldı")


for i in range(2):
    Adi = input("Adınızı giriniz: ")
    Ad.append(Adi)
    Soyadi = input("Soyadınızı giriniz: ")
    Soyad.append(Soyadi)
    Okul_nosu = input("Okul numaranızı giriniz: ")
    Okul_no.append(Okul_nosu)
    Matematik_puanii = int(input("Sınav notunuzu giriniz: "))
    Matematik_puanı.append(Matematik_puanii)
    harf_notu(Matematik_puanii)
    
    # sınav notu dogru girilene kadar input iste
 
#data = [["Ad","Soyad", "Okul_no", "Matematik_puanı"],[Ad,Soyad, Okul_no, Matematik_puanı]]

df = pd.DataFrame({
    "Ad": Ad,
    "Soyad": Soyad,
    "Okul_no": Okul_no,
    "Matematik_puanı": Matematik_puanı,
    "harf notu": kaldı_gecti
    })
xlWriterDf = pd.ExcelWriter("df.xlsx")
df.to_excel(
    excel_writer = xlWriterDf,
    sheet_name = "DF2",
    index = True,
    )
xlWriterDf.close()
