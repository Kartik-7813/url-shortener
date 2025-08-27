from .extensions import db
from datetime import datetime
import string
from random import choices

class Link(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)
    views = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()

    def generate_short_url(self):

        characters = string.ascii_letters + string.digits
        short_url = ''.join(choices(characters, k=10))
        link = self.query.filter_by(short_url=short_url).first()
        if link:
            return self.generate_short_url()
        
        return short_url
    
   
