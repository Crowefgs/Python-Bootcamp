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