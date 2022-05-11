from app import db
from datetime import datetime
from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager()
login_manager.init_app()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password_hash=db.Column(db.String(20),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self): 
        return f'{self.username}: {self.email}: {self.date_created}'

    @property
    def password(self):
        raise AttributeError("You can't read the password")

    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)    

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)   

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(20),nullable=False)
    post=db.Column(db.text())
    comment=db.Column(db.relationship('Comment',backref='pitch',lazy='dynamic'))
    upvote=db.Column(db.relationship('Upvote',backref='pitch',lazy='dynamic'))
    downvote=db.Column(db.relationship('Downvote',backref='pitch',lazy='dynamic'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Pitch{self.post}'  
    
class Comment(db.Model):
    __tablename__ = 'comments'

    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.Text(),nullable=False)
    user_id=db.column(db.Integer,db.ForeignKey('user.id'))
    pitch_id=db.column(db.Integer,db.ForeignKey('pitches.id'),nullable=False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments=Comment.query.filter_by(id=id).all()
        return comments   

    def __repr__(self):
        return f'Pitch{self.comment}'       

class Upvote(db.Model):
    __tablename__='upvotes'

    id=db.Column(db.Integer,primary_key=True)
    user_id=db.column(db.Integer,db.ForeignKey('user.id'))
    pitch_id=db.column(db.Integer,db.ForeignKey('pitches.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        downvote=Upvote.query.filter_by(pitch_id=id).all()
        return upvote    

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}' 
class Downvote(db.Model):
    __tablename__='downvotes'

    id=db.Column(db.Integer,primary_key=True)
    user_id=db.column(db.Integer,db.ForeignKey('user.id'))
    pitch_id=db.column(db.Integer,db.ForeignKey('pitches.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls,id):
        downvote=Downvote.query.filter_by(pitch_id=id).all()
        return downvote    

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'  