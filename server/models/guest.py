from server.models import db
from server.models.serializer_mixin import SerializerMixin

class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'
    serialize_rules = ('-appearances.guest',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String)

    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete')
