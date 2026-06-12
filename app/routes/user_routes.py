from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.schemas.user_schema import UserRegisterSchema, ValidationError
from app.services.user_services import UserService
from app.repositories.user_repository import UserRepository

main_bp = Blueprint("main_bp", __name__)

@main_bp.get("/")
def home():
    return "Hello, World!"

@main_bp.get("/check_auth")
@jwt_required()
def check_auth():
    user_name = get_jwt_identity()
    return jsonify({"message": f"You {user_name} are authenticated!"}), 200





@main_bp.post("/register_user")
def register():
    repo = UserRepository() # Create an instance of UserRepository
    data = request.get_json() # Receive data from request body
    try:
        validate_schema = UserRegisterSchema(**data)#validate data using pydantic schema
    except ValidationError as e:
        error_msgs = [err['msg'] for err in e.errors()]#show error message if validation fails
        return jsonify({"message": error_msgs[0]}), 400
    
    username = data.get("username")#get username password from data
    password = data.get("password")
            
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    result, error, status = UserService(repo).register_user(username, password)

    if error:
        return jsonify({"message": error}), status

    return jsonify({"message": result}), status

@main_bp.get("/get_user")
def get_user():
    repo = UserRepository()
    result, error, status = UserService(repo).get_users()
    if error:
        return jsonify({"message": error}), status
    return jsonify({"message": result}), status

    

@main_bp.put("/update_user/<int:user_id>")
def update_user(user_id):
    data = request.get_json()

    repo = UserRepository()
    result , error, status = UserService(repo).update_user(user_id, data.get("username"), data.get("password"))
    if error:
        return jsonify({"message": error}), status
    return jsonify({"message": result}), status
   
@main_bp.delete("/delete_user/<int:user_id>")
def delete_user(user_id):
    data = request.get_json()

    repo = UserRepository()
    result , error, status = UserService(repo).delete_user(user_id)
    if error:
        return jsonify({"message": error}), status
    return jsonify({"message": result}), status

@main_bp.post("/login")
def login():
    data = request.get_json()
    repo = UserRepository()
    result, error, status = UserService(repo).login_user(data.get("username"), data.get("password"))
    if error:
        return jsonify({"message": error}), status
    return jsonify({"message": result["message"], "access_token": result["access_token"]}), status

@main_bp.post("/logout")
def logout():
    # Normally logout client-side token clear karta hai, server-side session clear kar sakte hain
    return jsonify({"message": "Logged out successfully"}), 200