import mysql.connector

# Veritabanı bağlantımızı kuruyoruz
db = mysql.connector.connect(
    host="localhost",
    user="root",        # MySQL kullanıcı adın (kurulumda değiştirmediysen genelde 'root' olur)
    password="500267",   # MySQL'i kurarken belirlediğin kendi şifreni buraya yazmalısın
    database="bootcamp" # Bugün oluşturduğumuz veritabanının adı
)

print("Veritabanı bağlantısı başarıyla kuruldu!")

# Veritabanında işlem yapmak için bir imleç (elçi) oluşturuyoruz
cursor = db.cursor()

"""# SQL komutumuzu Python üzerinden çalıştırıyoruz
cursor.execute("SELECT * FROM students")

# Gelen tüm sonuçları alıp bir değişkene atıyoruz
ogrenciler = cursor.fetchall()

# Sonuçları satır satır ekrana yazdırmak için bir döngü kuruyoruz
for ogrenci in ogrenciler:
    print(ogrenci)

""""""
# 1. SQL komutumuz: 3 sütuna veri ekleyeceğimizi söylüyoruz.
# 3 farklı veri göndereceğimiz için 3 tane %s (yer tutucu) koyduk.
sql = "INSERT INTO students (id, isim, yas) VALUES (%s, %s, %s)"

# 2. Göndermek istediğimiz yeni öğrencinin bilgileri (Sıra, İsim, Yaş)
yeni_ogrenci = (6, "Zeynep", 22)

# 3. Komutu ve bilgileri birleştirip elçimiz aracılığıyla çalıştırıyoruz
cursor.execute(sql, yeni_ogrenci)

# 4. ÇOK ÖNEMLİ: Değişiklikleri veritabanına kalıcı olarak kaydediyoruz
db.commit()

# Terminalde göreceğimiz başarı mesajı
print(cursor.rowcount, "yeni öğrenci başarıyla eklendi!")
TEKLİ VERİ EKLEME
"""

"""
# SQL komutumuz tamamen aynı, 3 sütun için 3 yer tutucu
sql = "INSERT INTO students (id, isim, yas) VALUES (%s, %s, %s)"

# Bu sefer tek bir parantez değil, köşeli parantez içinde bir LİSTE hazırlıyoruz
yeni_ogrenciler = [
    (5, "Burak", 20),
    (6, "Elif", 23),
    (7, "Can", 19)
]

# DİKKAT: execute yerine "executemany" (çoklu çalıştır) komutunu kullanıyoruz!
cursor.executemany(sql, yeni_ogrenciler)

# Yaptığımız bu büyük değişikliği veritabanına kalıcı olarak işliyoruz
db.commit()

# Kaç satırın eklendiğini dinamik olarak ekrana yazdırıyoruz
print(cursor.rowcount, "öğrenci toplu olarak başarıyla eklendi!")"""

""""
#Diyelim ki az önce eklediğimiz ")Can" isimli öğrenci kaydını iptal ettirdi ve onu veritabanından tamamen silmemiz gerekiyor.
#🗑️ Veritabanından Kayıt Silmek (DELETE)
# 1. SQL Komutu: students tablosundan veriyi sil, AMA SADECE ismi %s olanı!
sql="delete from students where isim=%s"
# 2. Silinecek kişinin ismi (Dikkat: Tek elemanlı bir demet yaparken sonuna virgül koymalıyız!)
silinecek_kisi = ("Can",)
# 3. Komutu çalıştır
cursor.execute(sql, silinecek_kisi)
# 4. Değişikliği kalıcı olarak kaydet (İptal edilemez adım!)
db.commit()
# Kaç kaydın silindiğini ekrana yazdır
print(cursor.rowcount, "öğrenci sistemden silindi")
"""



#Öğrenci ekleme işlemini bir fonksiyona (kutucuya) hapsediyoruz
def ogrenci_ekle(ogrenci_id, isim, yas):
    sql = "INSERT INTO students (id, isim, yas) VALUES (%s, %s, %s)"
    degerler = (ogrenci_id, isim, yas)

    cursor.execute(sql, degerler)
    db.commit()
    print(isim, "başarıyla veritabanına eklendi!")


# ---------------------------------------------------------
# Artık uzun uzun kod yazmaya veya eskileri silmeye gerek yok.
# Sadece şu tek satırı yazarak sisteme yeni birilerini ekleyebilirsin:



def ogrenci_sil(ogrenci_id):
    # Nerede isim %s ise değil, nerede id %s ise o satırı sil diyoruz
    sql = "DELETE FROM students WHERE id = %s"

    # Artık isim değil, benzersiz olan id numarasını gönderiyoruz
    silinecek_kisi = (ogrenci_id,)

    cursor.execute(sql, silinecek_kisi)
    db.commit()
    print(ogrenci_id, "numaralı öğrenci başarıyla silindi.")


def ogrenci_guncelle(ogrenci_id, yeni_yas):
    # 1. SQL Komutu: Yaşı güncelle (%s), ama sadece id numarası şu olanı (%s)
    sql = "UPDATE students SET yas = %s WHERE id = %s"

    # 2. Değerlerimiz: Senin bulduğun doğru sıralama!
    degerler = (yeni_yas, ogrenci_id)

    # 3. Komutu çalıştır ve onayla
    cursor.execute(sql, degerler)
    db.commit()
    print(ogrenci_id, "numaralı öğrencinin yaşı", yeni_yas, "olarak güncellendi!")


def ogrencileri_listele():
    sql = "SELECT * FROM students"
    cursor.execute(sql)
    sonuclar = cursor.fetchall()

    print("--- 8ler B Sınıf Listesi ---")
    for ogrenci in sonuclar:
        # f-string (formatlı metin) kullanarak verileri şık bir yapıya yerleştiriyoruz
        print(f"Öğrenci No: {ogrenci[0]} | İsim: {ogrenci[1]} | Yaş: {ogrenci[2]}")
    print("----------------------------")

""""
print("=== OKUL YÖNETİM SİSTEMİ ===")

# Kullanıcıya ne yapmak istediğini soruyoruz
cevap = input("Yeni bir öğrenci kaydetmek istiyor musunuz? (E/H): ")

# Kullanıcı 'E' veya 'e' yazarsa kayıt işlemine başla
if cevap.upper() == "E":
    girilen_id = int(input("Öğrenci ID numarasını girin: "))
    girilen_isim = input("Öğrenci ismini girin: ")
    girilen_yas = int(input("Öğrenci yaşını girin: "))

    ogrenci_ekle(girilen_id, girilen_isim, girilen_yas)
    print("\nKayıt işlemi başarıyla tamamlandı.")

# Kullanıcı 'H' yazarsa veya başka bir tuşa basarsa işlemi atla
else:
    print("\nKayıt işlemi atlandı. Herhangi bir değişiklik yapılmadı.")

# Her iki durumda da son olarak listeyi göster
print("\n--- Güncel Durum ---")
ogrencileri_listele()
ogrenci_sil(18)
"""
print("=== OKUL YÖNETİM SİSTEMİ ===")
while True:
    print("\n--- ANA MENÜ ---")
    print("1. Yeni Öğrenci Ekle")
    print("2. Öğrencileri Listele")
    print("3. Öğrenci Sil")
    print("4. Öğrenci Yaşını Güncelle")
    print("5. Sistemden Çıkış Yap")

    secim = input("Lütfen yapmak istediğiniz işlemi seçin (1/2/3/4/5): ")
    if secim == "1":
        print("\n--- Yeni Kayıt ---")
        girilen_id = int(input("Öğrenci ID: "))
        girilen_isim = input("Öğrenci İsmi: ")
        girilen_yas = int(input("Öğrenci Yaşı: "))
        ogrenci_ekle(girilen_id,girilen_isim, girilen_yas)

    elif secim == "2":
        ogrencileri_listele()

    elif secim == "3":
        print("\n--- Öğrenci Silme ---")
        silinecek_id = int(input("Silmek istediğiniz öğrencinin ID numarasını girin: "))
        ogrenci_sil(silinecek_id)

    elif secim == "4":
        print("\n--- Öğrenci Güncelleme ---")
        guncellenecek_id = int(input("Yaşını güncellemek istediğiniz öğrencinin ID numarasını girin: "))
        yeni_yas = int(input("Öğrencinin yeni yaşını girin:"))
        ogrenci_guncelle(guncellenecek_id,yeni_yas)

    elif secim == "5":
        print("\nSistemden güvenli bir şekilde çıkış yapılıyor... İyi günler!")
        break

    else:
        print("\nHatalı bir tuşa bastınız! Lütfen 1 ile 5 arasında bir rakam girin.")