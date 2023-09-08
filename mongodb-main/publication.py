class Publication :

    def __init__(self, publication):
        self.id = publication.get('_id')
        self.type = publication.get('type')
        self.title = publication.get('title')
        self.pages = publication.get("pages")
        self.year= publication.get('year')
        self.booktitle = publication.get('booktitle')
        self.url = publication.get('url')
        self.authors = publication.get('authors')
        