from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
  {
    'id': 1,
    'title': 'Senhor dos Aneis',
    'author': 'J.R.R Tolkien'
  },
  {
    'id': 2,
    'title': 'Harry Potter e a Pedra Filosofal',
    'author': 'J.K Howling'
  },
  {
    'id': 3,
    'title': 'Habitos Atomicos',
    'author': 'James Clear'
  },
]


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/livros', methods=['GET'])
def get_books():
  return jsonify(books)

@app.route('/livros/<int:id>', methods=['GET'])
def get_books_by_id(id):
  for book in books:
    if book.get('id') == id:
       return jsonify(book)
    
@app.route('/livros/<int:id>', methods=['PUT'])
def edit_book_by_id(id):
   edited_book = request.get_json()
   for index,book in enumerate(books):
      if book.get('id') == id:
        books[index].update(edited_book)
        return jsonify(books[index])

@app.route('/livros', methods=['POST'])
def make_new_book():
  new_book = request.get_json()
  books.append(new_book)

@app.route('/livros/<int:id>', methods=['DELETE'])
def delete_book(id):
  for index, book in enumerate(books):
    if book.get('id') == id:
      del books[index]
  return jsonify(books)

app.run(port=5000, host='localhost', debug=True)