from flask import Flask, jsonify, request, render_template
import pandas as pd

app = Flask(__name__)

# Dummy data for popular_df
popular_data = {
    'Book-Title': ['Dummy Book 1', 'Dummy Book 2', 'Dummy Book 3'],
    'Book-Author': ['Author A', 'Author B', 'Author C'],
    'Image-URL-M': [
        'https://via.placeholder.com/150x200.png?text=Dummy+Book+1',
        'https://via.placeholder.com/150x200.png?text=Dummy+Book+2',
        'https://via.placeholder.com/150x200.png?text=Dummy+Book+3'
    ],
    'num_ratings': [100, 200, 150],
    'avg_rating': [4.5, 3.8, 4.2]
}
popular_df = pd.DataFrame(popular_data)

# Dummy data for pt
pt_data = {
    'index': ['Dummy Book 1', 'Dummy Book 2', 'Dummy Book 3']
}
pt = pd.DataFrame(pt_data)
pt.set_index('index', inplace=True)

# Dummy data for books
books_data = {
    'Book-Title': ['Dummy Book 1', 'Dummy Book 2', 'Dummy Book 3']
}
books = pd.DataFrame(books_data)

# Dummy data for similarity_scores
similarity_scores_data = [
    [0.9, 0.5, 0.3],
    [0.5, 0.9, 0.7],
    [0.3, 0.7, 0.9]
]
similarity_scores = pd.DataFrame(similarity_scores_data)

@app.route('/')
def index():
    return render_template('index.html', popular_df=popular_df)

@app.route('/api/popular_books', methods=['GET'])
def get_popular():
    # Iterate over popular_df and create a list of dictionaries containing book details
    books_list = []
    for index, row in popular_df.iterrows():
        book_details = {
            'title': row['Book-Title'],
            'author': row['Book-Author'],
            'image': row['Image-URL-M'],
            'votes': row['num_ratings'],
            'rating': row['avg_rating']
        }
        books_list.append(book_details)

    # Return the list of dictionaries as JSON
    return jsonify(books_list)

@app.route('/api/similarity_scores', methods=['GET'])
def get_similarity_scores():
    # Convert the similarity_scores DataFrame to a list of lists
    scores_list = similarity_scores.values.tolist()

    # Return the list of lists as JSON
    return jsonify(scores_list)


if __name__ == '__main__':
    app.run(debug=True)
