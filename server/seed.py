# server/seed.py
from server.app import create_app
from server.models import db, Guest, Episode, Appearance

app = create_app()

with app.app_context():
    print("🌱 Seeding database...")

    # Optional: Clear old data
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()

    # Add sample guests
    g1 = Guest(name="John Doe", occupation="Comedian")
    g2 = Guest(name="Jane Smith", occupation="Actor")

    # Add sample episodes
    e1 = Episode(date="2025-06-01", number=1)
    e2 = Episode(date="2025-06-02", number=2)

    # Add appearances
    a1 = Appearance(rating=4, guest=g1, episode=e1)
    a2 = Appearance(rating=5, guest=g2, episode=e2)

    db.session.add_all([g1, g2, e1, e2, a1, a2])
    db.session.commit()

    print("✅ Done seeding!")
