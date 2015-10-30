from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(140), index=True, unique=True)
    hangmanstats = db.relationship('HangmanStats', backref='author', lazy='dynamic')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __ref__(self):
        return '<User %r>' % (self.nickname)


class HangmanStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category = db.Column(db.String(140), index=True, unique=True)
    matches = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    lost = db.Column(db.Integer)

    def __ref__(self):
        return '<Stats %r>' % (self.wins)
