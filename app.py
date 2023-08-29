from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient('mongodb://root:example@mongodb:27017/')
db = client['DBLP']
collection = db['publis']

@app.route('/')
def index():
    publications = collection.find()
    return render_template('index.html', publications=publications)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
