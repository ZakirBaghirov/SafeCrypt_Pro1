# 🛡️ SafeCrypt Pro • Güvenli Şifreleme Uygulaması

**SafeCrypt Pro**, metin veya dosya verilerini şifrelemek, şifrelerini çözmek ve güvenliğini sağlamak için geliştirilen bir masaüstü uygulamasıdır. Uygulama, günümüzde yaygın olarak kullanılan iki güçlü kriptografik yaklaşımı temel alır:

- **SHA-512 (Secure Hash Algorithm)**: Verinin özetini (parmak izi) çıkarır.
- **ECC (Elliptic Curve Cryptography)**: Veriyi güvenli şekilde şifreler ve şifre çözer.

---

## 📸 Ekran Görüntüleri ve Açıklamalar

### 🏠 Ana Sayfa
![Ana Sayfa](https://github.com/user-attachments/assets/4fa5e448-e4e4-4cee-95f9-b52cec106dd0)

> Uygulamanın giriş ekranı. Kullanıcılar buradan SHA-512 ve ECC sayfalarına geçiş yapabilir. Üst çubukta "Ana Sayfa", "İletişim" gibi bağlantılar yer alır. Sol üstte geliştirici adı sabit durur.

---

### 🔐 SHA-512 Özeti Oluşturma (Hashing)

Hashing, bir verinin **benzersiz dijital parmak izini** oluşturan işlem türüdür. Verinin içeriği değiştiğinde özet de tamamen değişir.

#### 1. Metinle SHA-512
![SHA Metin](https://github.com/user-attachments/assets/af3a628b-5453-4bc4-bbfc-cc2751750e87)

> Kullanıcıdan alınan metin, SHA-512 algoritması ile işlenerek dijital özet değeri (hash) oluşturulur. Bu işlem genellikle dosya bütünlüğünü kontrol etmekte kullanılır.

#### 2. Dosyayla SHA-512
![SHA Dosya](https://github.com/user-attachments/assets/8bb9f30c-0090-42dc-8345-d68bd092c244)

> "Dosya Seç" butonu ile bir dosya seçildiğinde, SHA-512 hash algoritması kullanılarak o dosyanın özet değeri hesaplanır.

#### 3. Özet Doğrulama
![SHA Doğrulama](https://github.com/user-attachments/assets/b2613047-d6c5-4157-98ef-488fcde10ea2)

> Girilen hash ile dosya içeriğinden hesaplanan hash karşılaştırılır. Eğer aynıysa dosya değişmemiştir ve güvenlidir.

---

### 🔐 ECC ile Şifreleme ve Şifre Çözme

ECC (Eliptik Eğri Kriptografisi), veri güvenliği için modern ve hafif bir algoritmadır. RSA'ya kıyasla daha kısa anahtarlarla aynı güvenlik seviyesini sağlar.

#### 1. ECC ile Şifreleme
![ECC Şifreleme](https://github.com/user-attachments/assets/8a01f152-ba7f-4654-babb-f019db3fe1f6)

> Kullanıcının girdiği metin, ECC algoritması kullanılarak şifrelenir. Bu işlem sonunda çıktı olarak hem şifreli veri hem de anahtarlar üretilir.

#### 2. ECC ile Şifre Çözme
![ECC Şifre Çözme](https://github.com/user-attachments/assets/d95e036c-ffa8-4a92-b724-7c16c71b5f1b)

> Önceden şifrelenmiş veri ve anahtarlar kullanılarak şifresi çözülür ve orijinal metin tekrar elde edilir.

---

### 📞 İletişim Sayfası
![İletişim](https://github.com/user-attachments/assets/39b6b577-67e5-4c64-b4ba-4ea48598dcd3)

> Geliştirici ile iletişim kurmak isteyen kullanıcılar için LinkedIn, Instagram ve E-posta bağlantılarını içeren bir iletişim ekranı yer almaktadır.

---

## 💡 Temel Kavramlar (Kısaca Açıklama)

| Terim | Anlamı |
|------|--------|
| **Şifreleme (Encryption)** | Bir metni, yalnızca yetkili kişilerin okuyabileceği şekilde dönüştürme işlemidir. |
| **Şifre Çözme (Decryption)** | Şifrelenmiş veriyi orijinal haline döndürme işlemidir. |
| **Hash / Özetleme** | Verinin içerik değişikliğini tespit etmek için kullanılan, sabit uzunlukta bir parmak izi üretme işlemidir. |
| **SHA-512** | 512-bit uzunluğunda, geri döndürülemez bir veri özeti oluşturan algoritmadır. |
| **ECC** | Hafif ve güvenli şifreleme sağlayan modern eliptik eğri tabanlı algoritmadır. |

---

## 🔧 Özellikler

- ✅ ECC ile güvenli şifreleme ve çözme  
- ✅ SHA-512 ile dosya ve metin özetleme  
- ✅ Ana sayfa ve iletişim sekmeleri  
- ✅ Şık neon efektli koyu arayüz  
- ✅ Geri dönüş butonları ve kolay kullanım  
- ✅ Dosya seçimi, metin girişleri ve bilgi kutuları  

---

## ⚙️ Kullanılan Teknolojiler

- Python 3  
- PyQt5 (arayüz oluşturmak için)  
- hashlib (SHA-512 özetleme için)  
- pycryptodome (ECC algoritması için)

---

## 🛠️ Kurulum

### 1. Projeyi Klonlayın:
```bash
git clone https://github.com/ZakirBaghirov/safecrypt_pro.git
cd safecrypt_pro
