# Import Pandas and NumPy
import pandas as pd
from xlsxwriter.utility import xl_rowcol_to_cell

# bilgiler icin bos liste yarat
Ad = []
Soyad = []
Okul_no = []
Matematik_puanı = []
kaldı_gecti = []
harf_notu = []
Matematik_puanii = 0

# başarı durumunu kaydet harf notunu belirle
def not_aralıgı(puan):
    if 90<=puan<=100:
      kaldı_gecti.append("Geçti")
      harf_notu.append("AA")
    elif 85<=puan<=89:
      kaldı_gecti.append("Geçti")
      harf_notu.append("BA")
    elif 80<=puan<=84:
      kaldı_gecti.append("Geçti")
      harf_notu.append("BB")
    elif 75<=puan<=79:
      kaldı_gecti.append("Geçti")
      harf_notu.append("CB")
    elif 65<=puan<=74:
      kaldı_gecti.append("Geçti")
      harf_notu.append("CC")
    elif 60<=puan<=64:
      kaldı_gecti.append("Koşullu")
      harf_notu.append("DC")
    elif 55<=puan<=59:
      kaldı_gecti.append("Kaldı")
      harf_notu.append("DD")
    elif 50<=puan<=54:
      kaldı_gecti.append("Kaldı")
      harf_notu.append("DF")
    elif 0<=puan<=49:
      kaldı_gecti.append("Kaldı")
      harf_notu.append("FF")

# Q girilene kadar Bilgileri iste
while True:
    print("""Çıkmak için "q" ya basınız""")
    Adi = input("Adınızı giriniz: ")
    if Adi == "q":
      break
    Ad.append(Adi)
    Soyadi = input("Soyadınızı giriniz: ")
    Soyad.append(Soyadi)
    Okul_nosu = input("Okul numaranızı giriniz: ")
    Okul_no.append(Okul_nosu)
    Matematik_puanii = int(input("Sınav notunuzu giriniz: "))
    Matematik_puanı.append(Matematik_puanii)
    not_aralıgı(Matematik_puanii)
    
 
# pandas ile girilen öğrenci bilgileriyle data frame oluştur
df = pd.DataFrame({
    "Ad": Ad,
    "Soyad": Soyad,
    "Okul no": Okul_no,
    "Matematik puanı": Matematik_puanı,
    "Harf notu": harf_notu,
    "Başarı Durumu": kaldı_gecti
    })

# excel dosyası oluştur ve bunu xlWriter objesie ata
writer = pd.ExcelWriter("df.xlsx", engine="xlsxwriter")

df.to_excel(
    excel_writer = writer,
    sheet_name = "DF2",
    index = True,
    )
# çıktıyı düzenlemek için xlswiteri kullanıyoruz

workbook = writer.book
worksheet = writer.sheets['DF2']
#Now we have the worksheet object. We can manipulate it 
worksheet.set_zoom(90)
#Set header formating
header_format = workbook.add_format({
        "valign": "vcenter",
        "align": "center",
        "bg_color": "#951F06",
        "bold": True,
        "font_color": "#FFFFFF"
    })
# Adjust the column width.
worksheet.set_column('A:G', 15)
writer.save()
writer.close()
