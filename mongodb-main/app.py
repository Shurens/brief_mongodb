from flask import Flask, render_template, request, redirect, url_for
from mongo_data import Data



app = Flask(__name__)


@app.route('/')
def index():
    data = Data()
    authors = data.get_unique_authors()
    return render_template('index.html', authors=authors)

@app.route('/search', methods=['GET'])
def search():
    author = request.args.get('author')

    data = Data()
    publications = data.get_publication_by_author(author)
    
    return render_template('publication.html', publications=publications)

@app.route('/date', methods=['GET'])
def date():
    date = request.args.get('date')
    data = Data()
    publications = data.get_publications_by_date(date)

    return render_template('date.html', publications=publications, search_date=date)

@app.route('/add_publication', methods=['POST'])
def add_publication():
    title = request.form.get('title')
    authors = request.form.get('author')
    year = request.form.get('year')

    data = Data()
    publication_data = {
        'title': title,
        'authors': authors,
        'year': year,
    }
    data.add_publication(publication_data)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)































