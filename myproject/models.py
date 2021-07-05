# Models.py : our top level model. we're using only 1 model class. it contains all the tables class that we need
# to create and the relationship that needs to be present.
# set up db inside __init__.py file under myproject folder
from myproject import db

# Model class : our tables collection
class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner',backref='owner', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"The puppy name is {self.name} and owner name is {self.owner.name}"
        else:
            return f" The puppy name is {self.name} and has no owner yet"

# Model Class : Owner table
class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    # def __repr__(self):
    #    return f"The puppy name is {self.name} and owner is {self.puppy_id}"
