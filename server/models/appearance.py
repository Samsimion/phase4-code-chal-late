from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates
from server.models import db
from server.models.serializer_mixin import SerializerMixin

class Appearance(db.Model, SerializerMixin):
    __tablename__ = 'appearances'
    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_between_1_and_5'),
    )

    serialize_rules = ('-guest.appearances', '-episode.appearances')

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))

    guest = db.relationship('Guest', back_populates='appearances')
    episode = db.relationship('Episode', back_populates='appearances')

    @validates('rating')
    def validate_rating(self, key, value):
        if not 1 <= value <= 5:
            raise ValueError("Rating must be between 1 and 5")
        return value
