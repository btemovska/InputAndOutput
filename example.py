import shelve

books = shelve.open("book")
books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled_eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"]["soup"])  # ['tin of soup']
print(books["recipes"]["scrambled_eggs"])  # ['eggs', 'butter', 'milk']
print(books["maintenance"]["loose"])  # ['gaffer tape']

books.close()
