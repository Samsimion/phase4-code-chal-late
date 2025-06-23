from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError
from server.models.appearance import Appearance
from server.models import db

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    try:
        new = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        db.session.add(new)
        db.session.commit()
        return jsonify(id=new.id, rating=new.rating), 201

    except (ValueError, IntegrityError) as e:
        db.session.rollback()
        return jsonify(error=str(e)), 400

@appearance_bp.route('/appearances', methods=['GET'])
def get_appearances():
    appearances = Appearance.query.all()
    return jsonify([a.to_dict() for a in appearances])
