# 📚 Audible Kitap Veri Toplama Botu / Audible Book Scraper

Bu proje, **Audible** üzerinden kitap bilgilerini otomatik olarak çekmek için geliştirilmiş bir Python web scraping aracıdır. `requests` ve `BeautifulSoup` kütüphanelerini kullanarak kitap başlığı, yazar, anlatan, uzunluk, yayın tarihi, dil ve kullanıcı puanı gibi bilgileri toplar. Toplanan veriler daha sonra otomatik olarak **CSV formatında kaydedilir**.

---

## 🇹🇷 Özellikler (Türkçe)

- 🔍 Anahtar kelime ile arama yapar  
- 🎧 Anlatıcı bilgilerini toplar  
- 📖 Kitap süresi, çıkış tarihi ve dili kaydeder  
- ⭐ Kullanıcı puanlarını çeker  
- 💾 Verileri **CSV** dosyasına otomatik kaydeder  
- 🧩 Esnek sınıf tasarımı sayesinde kolay geliştirilebilir  

### 🛠 Kullanılan Teknolojiler
- Python
- Requests
- BeautifulSoup (bs4)
- CSV

---

## 🇪🇸 Features (English)

- 🔍 Searches Audible by keyword  
- 🎧 Retrieves narrator information  
- 📖 Collects book length, release date & language  
- ⭐ Fetches user ratings  
- 💾 Automatically saves results into a **CSV** file  
- 🧩 Flexible OOP-based class design for easy expansion  

### 🛠 Technologies Used
- Python
- Requests
- BeautifulSoup (bs4)
- CSV

---

## 🚀 Nasıl Kullanılır? / How to Run?

```bash
pip install requests bs4
python main.py
```

Kod içindeki şu satırı değiştirerek farklı aramalar yapabilirsiniz:

```python
scraper = Scraper(search_query="book", node="18573211011")
```

Node parametresi isteğe bağlıdır.

---

## 📁 Çıktı / Output

Oluşturulan `books.csv` dosyası şu sütunları içerir:

| Title | Author | Narrated | Length | ReleaseDate | Language | Rating |
|--------|---------|-----------|---------|----------------|-----------|----------|

---

## 🧑‍💻 Katkı / Contribution

Her türlü katkıya açığız! PR göndermekten çekinmeyin.

---

## 📜 Lisans / License

Bu proje MIT Lisansı ile korunmaktadır.

---

### ⭐ Eğer bu projeyi beğendiysen yıldız vermeyi unutma!  
**Thanks for supporting! 🙌**

