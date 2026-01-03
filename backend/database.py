from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class SearchResult(db.Model):
    __tablename__ = 'search_results'
    
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(200), nullable=False)
    store = db.Column(db.String(50), nullable=False)
    product_name = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    url = db.Column(db.Text, nullable=False)
    scraped_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<ShearchResult {self.product_name} - €{self.price}>'