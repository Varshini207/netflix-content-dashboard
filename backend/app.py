from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # This allows your React app to talk to this API
df = pd.read_csv(r"C:\Users\Varsh\Desktop\netflix-dashboard\data\netflix_titles.csv")

@app.route('/api/genre-data')
def get_genre_data():
    # Split genres and count them
    genres = df['listed_in'].str.split(', ').explode().value_counts().reset_index()
    genres.columns = ['genre', 'count']
    return genres.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True, port=5000)