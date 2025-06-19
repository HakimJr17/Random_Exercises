Books = {
    "River Between": {"author": "Kaimenyi Muna", "genre": "Drama"}, 
    "Think Big": {"author": "Robert Carson", "genre": "Motivational"},
    "Alchemist": {"author": "Dan Juma", "genre": "Fictional"},
    "Walmart": {"author": "Sam Walton", "genre": "Biography"}
    }

print(Books["River Between"]["genre"])

for book_title, details in Books.items():
    genre = details["genre"]
    print(f"'{book_title}' is a {genre} book.")