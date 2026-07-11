from app.models.user import User
from app.extensions.extensions import db
from flask import jsonify
from flask_jwt_extended import create_access_token

class UserService:

    def __init__(self, repo):
        self.repo = repo

    def register_user(self, username, password):
        user = self.repo.get_user_by_username(username)

        if user:
            return None, "User already exists", 400

        new_user = User(
            username=username,
            password=password
        )

        self.repo.add_user(new_user)

        return (
            f"User {username} registered successfully",
            None,
            201
        )

    def login_user(self, username, password):

        if not username or not password:
            return (
                None,
                "Username and password are required",
                400
            )

        user = self.repo.get_user_by_username(username)

        if not user:
            return None, "User not Found", 404

        if user.password != password:
            return None, "Invalid credentials", 401

        token = create_access_token(
            identity=username
        )

        return (
            {
                "message": f"Logged in as {user.username}",
                "access_token": token
            },
            None,
            200
        )

    def get_users(self):

        users = self.repo.get_all_users()

        if not users:
            return None, "No users found", 404

        result = [
            {
                "id": u.id,
                "username": u.username
            }
            for u in users
        ]

        return result, None, 200

    def update_user(
        self,
        user_id,
        username,
        password
    ):

        user = self.repo.get_user_by_id(user_id)

        if not user:
            return None, "User not Found", 404

        if username:
            user.username = username

        if password:
            user.password = password

        self.repo.save(user)

        return (
            f"User {user.username} updated successfully",
            None,
            200
        )

    def delete_user(self, user_id):

        user = self.repo.get_user_by_id(user_id)

        if not user:
            return None, "User not Found", 404

        self.repo.delete_user(user)

        return (
            f"User {user.username} deleted successfully",
            None,
            200
        )




    
# class UserService:
#     def __init__(self, repo):
#         self.repo = repo
#     @staticmethod
#     def register_user(self, username, password):
#         result = UserRepository.get_user_by_username(username)
#         if result:
#             return None, "User already exists", 400

#         new_user = User(username=username, password=password)
#         UserRepository.add_user(new_user)
#         return f"User {username} registered successfully",None, 201
    
#     @staticmethod
#     def login_user(username, password):
#         if not username or not password:
#             return None, "Username and password are required", 400
        
#         user = UserRepository.get_user_by_username(username)
#         if not user:
#             return None, "User not Found", 404
#         if user.password != password:
#             return None, "Invalid credentials", 401
        
#         access_token = create_access_token(identity=username)
#         return {"message": f"Logged in as {user.username}", "access_token": access_token}, None, 200

#     @staticmethod
#     def get_user_service():
#         user = UserRepository.get_all_users() # User.query.all() #OLD VERSION
#         if not user:
#             return None, "No users found", 404
#         result = [{"id": u.id, "username": u.username} for u in user]
#         return result, None, 200
    
#     @staticmethod
#     def update_user_service(user_id, new_username, new_password):

#         user = UserRepository.get_user_by_id(user_id) # User.query.get(user_id) #OLD VERSION
#         if not user:
#             return None, "User not Found", 404
#         if new_username:
#             user.username = new_username
#         if new_password:
#             user.password = new_password
#         db.session.commit()
#         return f"User {user.username} updated successfully", None, 200
    
#     @staticmethod
#     def delete_user_service(user_id):
#         user = UserRepository.get_user_by_id(user_id) # User.query.get(user_id) #OLD VERSION
#         if not user:
#             return None, "User not Found", 404
#         db.session.delete(user)
#         db.session.commit()
#         return f"User {user.username} deleted successfully", None, 200



