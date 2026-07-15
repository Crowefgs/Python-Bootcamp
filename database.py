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

# SQL komutumuzu Python üzerinden çalıştırıyoruz
cursor.execute("SELECT * FROM students")

# Gelen tüm sonuçları alıp bir değişkene atıyoruz
ogrenciler = cursor.fetchall()

# Sonuçları satır satır ekrana yazdırmak için bir döngü kuruyoruz
for ogrenci in ogrenciler:
    print(ogrenci)
"""
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


# Öğrenci ekleme işlemini bir fonksiyona (kutucuya) hapsediyoruz
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

ogrenci_guncelleme(10, 25)