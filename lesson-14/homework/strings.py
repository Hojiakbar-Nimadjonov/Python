#JSON Analysis (students.json)
import json

with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for student in data["students"]:
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Major: {student['major']}\n")
{
  "students": [
    {"name": "Ali", "age": 20, "major": "Computer Science"},
    {"name": "Zarina", "age": 22, "major": "Economics"}
  ]
}

#Weather API (Tashkent example)
import requests

API_KEY = 'your_api_key_here'
city = 'Tashkent'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print("City:", data['name'])
print("Temperature:", data['main']['temp'], "°C")
print("Humidity:", data['main']['humidity'], "%")
print("Weather:", data['weather'][0]['description'])

#Modify JSON (books.json)
import json

def load_books():
    with open("books.json", "r", encoding='utf-8') as f:
        return json.load(f)

def save_books(books):
    with open("books.json", "w", encoding='utf-8') as f:
        json.dump(books, f, indent=4)

def add_book(title, author):
    books = load_books()
    books["books"].append({"title": title, "author": author})
    save_books(books)

def update_book(old_title, new_title):
    books = load_books()
    for book in books["books"]:
        if book["title"] == old_title:
            book["title"] = new_title
    save_books(books)

def delete_book(title):
    books = load_books()
    books["books"] = [b for b in books["books"] if b["title"] != title]
    save_books(books)

# Example usage:
add_book("New Book", "Some Author")
update_book("New Book", "Updated Book")
delete_book("Updated Book")
{
  "books": [
    {"title": "1984", "author": "George Orwell"},
    {"title": "Dune", "author": "Frank Herbert"}
  ]
}

#Movie Recommendation System (OMDb API)
import requests
import random

API_KEY = 'your_omdb_api_key'
genre = input("Enter a genre (e.g. Action, Comedy, Drama): ")

# Sample movie titles by genre (you can expand this list)
movies_by_genre = {
    "Action": ["Mad Max", "John Wick", "Gladiator"],
    "Comedy": ["The Mask", "Superbad", "The Hangover"],
    "Drama": ["The Godfather", "Forrest Gump", "Fight Club"]
}

movie = random.choice(movies_by_genre.get(genre, []))

url = f"http://www.omdbapi.com/?t={movie}&apikey={API_KEY}"
response = requests.get(url)
data = response.json()

if data['Response'] == 'True':
    print("Title:", data['Title'])
    print("Year:", data['Year'])
    print("Genre:", data['Genre'])
    print("Plot:", data['Plot'])
else:
    print("Movie not found.")
