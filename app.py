from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def extract_article_title(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1').text
        return title
    except Exception as e:
        return f"Error extracting title: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    article_title = None

    if request.method == 'POST':
        # Get the article URL submitted by the user
        article_url = request.form['article_url']

        # Process the article URL and extract the title
        article_title = extract_article_title(article_url)

    # If it's a GET request or an error occurred, just render the template
    return render_template('index.html', article_title=article_title)

if __name__ == '__main__':
    app.run(debug=True)

