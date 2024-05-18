from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)

with open('popular.pkl', 'rb') as f:
    popular_df = pickle.load(f)

with open('pt.pkl', 'rb') as f:
    pt = pickle.load(f)

with open('books.pkl', 'rb') as f:
    books = pickle.load(f)

with open('similarity_scores.pkl', 'rb') as f:
    similarity_scores = pickle.load(f)

@app.route('/api/popular_books', methods=['GET'])
def get_popular_books():
    books_data = [{
        'book_name': book['Book-Title'],
        'author': book['Book-Author'],
        'image': book['Image-URL-M'],
        'votes': book['num_ratings'],
        'rating': book['avg_rating']
    } for book in popular_df]
    return jsonify(books_data)

@app.route('/api/recommend_books', methods=['POST'])
def recommend_books():
    user_input = request.json.get('user_input')
    try:
        index = list(pt.index).index(user_input)
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

        data = []
        for i in similar_items:
            temp_df = [book for book in books if book['Book-Title'] == pt.index[i[0]]]
            if temp_df:
                item = {
                    'book_name': temp_df[0]['Book-Title'],
                    'author': temp_df[0]['Book-Author'],
                    'image': temp_df[0]['Image-URL-M']
                }
                data.append(item)

        return jsonify(data)
    except ValueError:
        return jsonify([]), 404

if __name__ == '__main__':
    app.run(port=5000)
