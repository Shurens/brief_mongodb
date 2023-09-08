from mongo_conection import *
from publication import Publication

class Data :
    def get_unique_authors(self):
        client = MongoAccess.connexion()
        authors = client.publis.distinct('authors')
        MongoAccess.deconnexion()
        return authors
    
    def get_publication_by_author(self, author):
        client = MongoAccess.connexion()
        publications = client.publis.find({'authors': author})
        publis = [Publication(pub) for pub in publications]
        MongoAccess.deconnexion()
        return publis
    
    def get_publications_by_date(self, date):
        client = MongoAccess.connexion()
        publications = client.publis.find({'year': {'$gte': int(date)}}).sort([('year'),('title')])
        publis = [Publication(pub) for pub in publications]
        MongoAccess.deconnexion()
        return publis

    def add_publication(self, publication_data):
        client = MongoAccess.connexion()
        client.publis.insert_one(publication_data)
        MongoAccess.deconnexion()