from app.models.user import User
from app.extensions.extensions import db
from app.models.user import User

class UserRepository:
    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def get_all_users():
        return User.query.all()#isse sara data aaega
    #it's latest version of getting all users, earlier it was User.query.all() but now we are using db.session.get() method to get all users.

    @staticmethod
    def get_user_by_id(user_id):
        
        return db.session.get(User, user_id)
    
    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()

    @staticmethod
    def save(user):
        db.session.commit()