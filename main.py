import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.audible.com/search?keywords=book&node=18573211011"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

class Scraper:
    BASE_URL = "https://www.audible.com"
    def __init__(self, search_query, node=None):
        self.search_query = search_query
        self.node = node
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        self.placeholder()

    def placeholder(self):
        self.books_list = []
        self.authors_list = []
        self.narrated_list = []
        self.length = []
        self.release_date = []
        self.language = []
        self.rating = []
        self.alfabe = [
    'a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p',
    'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z',
    'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P',
    'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z',
    'q', 'w', 'x',
    'Q', 'W', 'X','$'
]
        self.book_dict = {}
    def fetch_books(self):
        params = {
            "keywords":self.search_query,
        }
        if self.node:
            params["node"] = self.node

        response = requests.get(f"{self.BASE_URL}/search", headers=headers, params=params, timeout=10)
        response.raise_for_status()

        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        self.books = soup.find_all(name="div", class_="bc-col-responsive bc-col-9")

    def book_titles(self):
        for book in self.books:
            for a_tag in book.find_all(name="a", class_="bc-link"):
                href = a_tag.get("href")
                text = a_tag.get_text(strip=True)
                if "Product" in href:
                    if text != "":
                        self.books_list.append(text)

    def book_authors(self):
        for book in self.books:
            for span_tag in book.find_all(name="span", class_="bc-text"):
                text = span_tag.get_text(strip=True)
                if "By:" in text:
                    text = text.split("By:")[1]
                    self.authors_list.append(text)

    def book_narrated(self):
        for book in self.books:
            for span_tag in book.find_all(name="span", class_="bc-text"):
                text = span_tag.get_text(strip=True)
                if "Narrated by:" in text:
                    text = text.replace("Narrated by:", "").strip()
                    self.narrated_list.append(text)

    def book_length(self):
        for book in self.books:
            for span_tag in book.find_all(name="span", class_="bc-text"):
                text = span_tag.get_text(strip=True)
                if "Length:" in text:
                    text = text.split("Length:")[1].lstrip()
                    self.length.append(text)

    def book_release_date(self):
        for book in self.books:
            for span_tag in book.find_all(name="span", class_="bc-text"):
                text = span_tag.get_text(strip=True)
                if "Release date:" in text:
                    text = text.rsplit("Release date:")[1].lstrip()
                    self.release_date.append(text)

    def book_language(self):
        for book in self.books:
            for span_tag in book.find_all(name="span", class_="bc-text"):
                text = span_tag.get_text(strip=True)
                if "Language:" in text:
                    text = text.split("Language:")[1].lstrip()
                    self.language.append(text)

    def book_ratings(self):
        for book in self.books:
            for span_tag in book.find_all(name="span", class_="bc-text"):
                text = span_tag.get_text(strip=True)
                if "Not rated" in text:
                    self.rating.append("Not rated yet")

                if "." in text and "..." not in text:
                    if not any(char in self.alfabe for char in text):
                        self.rating.append(text)

    def book_dictionary(self):
        for i in range(len(self.books_list)):
            self.book_dict[i] = {
                "Title": self.books_list[i],
                "Author": self.authors_list[i],
                "Narrated": self.narrated_list[i],
                "Length": self.length[i],
                "ReleaseDate": self.release_date[i],
                "Language": self.language[i],
                "Rating": self.rating[i],
            }

    def csv(self):
        with open("books.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = ["Title", "Author", "Narrated", "Length", "ReleaseDate", "Language", "Rating"], delimiter=";")
            writer.writeheader()
            writer.writerows(self.book_dict.values())

    def run(self):
        self.fetch_books()
        self.book_titles()
        self.book_authors()
        self.book_narrated()
        self.book_length()
        self.book_release_date()
        self.book_language()
        self.book_ratings()
        self.book_dictionary()
        self.csv()
scraper = Scraper(search_query="book", node="18573211011")
data = scraper.run()
