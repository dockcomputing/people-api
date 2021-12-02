import os
from config import db
from models import Person

PEOPLE = [
    {"fname": "Dock", "lname": "Leong"},
    {"fname": "Taylor", "lname": "Swift"},
    {"fname": "Tom", "lname": "Cruise"},
]

if os.path.exists('people.db'):
    os.remove('people.db')

# Create database
db.create_all()

for person in PEOPLE:
    p = Person(lname=person['lname'], fname=person['fname'])
    db.session.add(p)

db.session.commit()