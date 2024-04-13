# Using flask to make an API
# Import necessary libraries and functions
from flask import Flask, jsonify, request
from textblob import TextBlob 

# Creating a Flask app
app = Flask(__name__)

# On the terminal type: curl http://127.0.0.1:5080/
# Returns "hello world" when we use GET.
# Returns the data that we send when we use POST.
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = "hello world"
        return jsonify({'data': data})

# A simple function to calculate the square of a number
# The number to be squared is sent in the URL when we use GET
# On the terminal type: curl http://127.0.0.1:5080/home/10
# This returns 100 (square of 10)
@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        
        text = request.json['text']  # Assuming the data is sent in JSON format
        blob = TextBlob(text)
        sentiment = blob.sentiment

        if sentiment.polarity > 0:
            sentiment_category = 'Positive'
        elif sentiment.polarity < 0:
            sentiment_category = 'Negative'
        else:
            sentiment_category = 'Neutral'
        
        # Create a JSON response with the sentiment analysis results
        response = {
            'sentiment': sentiment_category,
            'polarity': sentiment.polarity,
            'subjectivity': sentiment.subjectivity
        }

        return jsonify(response)

# Driver function
if __name__ == '__main__':
    # Run the app on port 5080
    app.run(debug=True, port=5080)
