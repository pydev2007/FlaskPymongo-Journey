import datetime
import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

# Set MongoDB URI from environment variable
mongo_uri = os.environ.get('MONGO_URI')

# Create Flask app instance and configure MongoDB
app = Flask(__name__)
app.config['MONGO_URI'] = mongo_uri
mongo = PyMongo(app)

# Create sample post data
post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# Define a route to handle requests to the homepage
@app.route('/')
def home():
    # Query the 'posts' collection in the 'mydatabase' database for a post with 'author' field of 'Mike'
    example = mongo.db.posts.find_one({"author": "Mike"})
    
    # Extract the relevant fields from the post data
    author = example['author']
    text = example['text']
    tags = example['tags']
    date = example['date']
    
    # Render the home.html template with the extracted post data as context
    return render_template('home.html', author=author, text=text, tags=tags, date=date)

# Start the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)