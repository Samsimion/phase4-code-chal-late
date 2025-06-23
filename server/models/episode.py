from server.models import db
from server.models.serializer_mixin import SerializerMixin

class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'
    serialize_rules = ('-appearances.episode',)

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete')
