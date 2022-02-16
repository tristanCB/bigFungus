from bigFungusWeb import db
import pprint
pp = pprint.PrettyPrinter(indent=2)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Autocalves(db.Model):
    __tablename__   = 'kijiji_'                
    date_scrapped   = db.Column(db.DateTime(), unique=False)
    price           = db.Column(db.Float(), unique=False)
    img_href        = db.Column(db.String(120), unique=False)
    img_alt         = db.Column(db.String(120), unique=False)
    link            = db.Column(db.String(250), primary_key=True)
    item_type       = db.Column(db.String(250), unique=False)

    def __repr__(self):
        return f'{pprint.pformat(self.__dict__)}'

class Logger(db.Model):
    __tablename__   = 'activity_'
    date_accessed   = db.Column(db.DateTime(), unique=False)
    ip              = db.Column(db.String(120), unique=False)
    id              = db.Column(db.Integer(), autoincrement=True, primary_key=True)

    def __repr__(self):
        return f'Connecting IP > {self.ip!r}'
    
class Recipes(db.Model):
    __tablename__   = 'recipes_'
    id              = db.Column(db.Integer, primary_key=True)
    date_scrapped   = db.Column(db.DateTime(), unique=False)
    title           = db.Column(db.String(255), unique=True, nullable=False)
    website         = db.Column(db.String(255), unique=False, nullable=False)
    img_href        = db.Column(db.String(255), unique=True, nullable=False)
    link            = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return f'{pprint.pformat(self.__dict__)}'