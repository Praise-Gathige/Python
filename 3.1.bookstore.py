filename = 'library.txt'

# 1. The Extraction Function
def load_library(filename):
    books = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) == 3:
                title, price_str, genre = parts
                try:
                    price = float(price_str)

                    books.append({
                        'title': title,
                        'price': price,
                        'genre': genre
                    })
                except ValueError:
                    continue
    return books


# 2. The Logic Function
def organize_by_genre(books):
    genre_dict = {}
    for book in books:
        genre = book['genre']
        title = book['title']
        
        if genre not in genre_dict:
            genre_dict[genre] = []
        genre_dict[genre].append(title)
    return genre_dict


# 3. Execution Block

cleaned_data = load_library(filename)

organized_data = organize_by_genre(cleaned_data)

with open('summary.txt', 'w') as summary_file:
    for genre, titles in organized_data.items():
        summary_file.write(f"{genre}\n")
        for title in titles:
            summary_file.write(f"- {title}\n")
        summary_file.write("\n")

total_value = 0.0
for book in cleaned_data:
    total_value += book['price']

print(f"Total Collection Value: ${total_value:.2f}")
