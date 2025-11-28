
# 📚 Audible Book Scraper

This project is a **Python-based web scraping tool** designed to automatically extract audiobook details from **Audible**. Using `requests` and `BeautifulSoup`, it collects information such as **title, author, narrator, length, release date, language, and user rating**. The scraped data is then saved in **CSV format** for easy analysis.

## Features

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

## How to Run?

```bash
pip install requests bs4
python main.py
```

```python
scraper = Scraper(search_query="book", node="18573211011")
```

---

## 📁Output

The generated books.csv file contains the following columns:

| Title | Author | Narrated | Length | ReleaseDate | Language | Rating |
|--------|---------|-----------|---------|----------------|-----------|----------|

---

## 🧑‍💻 Contribution

We welcome all contributions! Feel free to submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

### ⭐ If you like this project, don’t forget to give it a star!



