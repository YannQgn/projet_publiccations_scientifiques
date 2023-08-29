from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://root:example@localhost:27017/')
db = client['DBLP']
collection = db['publis']

@app.route('/')
def index():
    publications = collection.find()
    return render_template('index.html', publications=publications)

# Ajoutez d'autres routes pour les filtres, détails de publication, etc.

if __name__ == '__main__':
    app.run(debug=True)
