import pytest
from unittest.mock import Mock, patch, MagicMock


# @pytest.mark.skip("test_sample_2")
# def test_sample_2():
#     print("test_sample_2")

# class Test_3:

#     def test_login_with_valid_credentials_2(self):
#         print("Testing_test_login_with_valid_credentials")
#     def test_login_with_valid_email_and_invalid_password_2(self):
#         print("Testing_test_login_with_valid_email_and_invalid_password")

# def test_hook_3():
#     print("test_hook_3")


################### CREATING FIXTURE IN CONFTEST.PY AND USE IT IN THE TEST

@pytest.mark.usefixtures("fixture_setup_and_teardown")

class Test_ficture_2:

    def test_fixture_3(self):
        driver = "i'm the driver"
        print("test_fixture_3")
        assert driver == self.driver
    
    def test_fixture_4(self):
        driver = "i'm the driver"
        print("test_fixture_4")
        assert driver == self.driver

#############################################################################################################
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Monkeypatch : replace existing real thing.
# Mock : create fake object from scratch.

def make_payment(service, amount):
    print(service.charge(amount), "make_payment_test")
    return service.charge(amount)


@pytest.mark.hello
def test_make_payment():
    fake_service = Mock()

    fake_service.charge.return_value = "success"

    result = make_payment(fake_service, 500)

    fake_service.charge.assert_called_with(500)
    assert result == "success" 

# 0.Mock()
# 1.return_value
# 2.assert_called_with
# 3.side_effect

@pytest.mark.hello
def test_payment_failure():
    fake_service = Mock()

    fake_service.charge.side_effect = Exception("Payment failed")

    with pytest.raises(Exception):
        make_payment(fake_service, 100)
    # fake_service.charge.assert_called_with(500)

def get_name():
    return "John Doe"

def test_get_name():
    fake_get_name = Mock(return_value="Jane Doe")
     
    result = fake_get_name()

    assert result == "Jane Doe"

######################################### PATCH
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# What does patch do? : Temporarily replace a real thing with fake thing during test.
# INTERNALLY HUM MOCK KA USE NHI KR SKTE WO EXTERNALLY FAKE CHEEZE BANATA HAI JISSE HUM TEST ME USE KR SAKTE HAIN. MOCK KA USE KARKE HUM REAL OBJECT KO REPLACE KAR SAKTE HAIN APNE FAKE OBJECT SE EXTERNALLY.
# BUT INTERNALLY HUM MOCK KA USE NHI KR SAKTE HAIN KYUNKI MOCK EK EXTERNAL CHEEZE HAI JO REAL CHEEZE KO REPLACE KARTA HAI TEST KE DAURAN SO PATCH KA USE KRTE H INTERNALLY

# Mock : "I create fake object and give it to code."

# Patch : "I replace object that code creates/uses internally."


# from email_service import EmailService
class EmailService():
    def __init__(self):
        self.sent_emails = []

    def send(self, email):
        self.sent_emails.append(email)
        return False

def register_user(email):
    email_service = EmailService()

    result = email_service.send(email)
    if result:
        return "User Registered"
    else:
        return "Failed to register user"

class FakeEmailService:
    def send(self, email):
        print("FAKE email sent", "Fake Email Service")

@pytest.mark.newMark
def test_register_user(mocker):
    mocker.patch("test_sample_2.EmailService.send", return_value=True)
    result = register_user("test@gmail.com")
    print(result, "Test Register User with Patch")
    assert result == "User Registered"

    # with patch.object(EmailService, "send", return_value=True):
    # with patch("test_sample_2.EmailService.send", return_value=True):
     
    # with patch("test_sample_2.EmailService") as MockEmailService:
    #     mock_instance = MockEmailService.return_value

    #     mock_instance.send.return_value = True

        # result = register_user("test@gmail.com")
        # assert result == "User Registered"

        # mock_instance.send.assert_called_once_with("test@gmail.com")

    # with patch("test_sample_2.EmailService", FakeEmailService):

    #     result = register_user("test@gmail.com")

    #     assert result == "User Registered"

################################# patch.object()
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Normal patch : Replace whole class/object.
# patch.object : Replace specific method/attribute inside object as per requirements.

class PaymentService:
    def charge(self, amount):
        print("REAL payment happening", "Payment Service")
        return "success"


def make_payment_2():
    service = PaymentService()
    return service.charge(500)

def test_make_payment_2():
    with patch.object(PaymentService, "charge", return_value="fake success"):
        result = make_payment_2()
        assert result == "fake success"


##################################MagicMock
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Mock + supports Python magic methods automatically.
# Good for:
# iterable objects
# list-like behavior
# dict-like behavior
# context managers

######################## Mock
# Basic fake object.
# Good for:
# services
# methods
# API calls

def test_magic_mock():
    fake_service = MagicMock()

    fake_service.__len__.return_value = 5

    result = len(fake_service)
    print("length of fake_service using magic mock : ", result, "Test Magic Mock")
    assert result == 5


##################################Flask API Testing
##################################Testing Database with Flask + SQLAlchemy
##################################Testing Flask CRUD APIs with Database
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# “Check whether backend API behaves correctly.”
# Not UI.
# Not frontend.
# Backend logic.

# Backend engineers test:

# success
# failure
# edge cases
# invalid input
# missing fields
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\

@pytest.mark.integration
class Test_Basic_app:
    def test_home(self, client, init_database):
        response = client.get("/")
        print(response.get_data(as_text=True), "Test Home")
        assert response.status_code == 200
        assert response.get_data(as_text=True) == "Hello, World!"

    def test_register(self, client, init_database):
        response = client.post("/register_user",
                            json={
                                "username": "testuser",
                                "password": "testpass"
                            })
        print(response.get_json(), "Test Register")
        assert response.status_code == 201
        assert response.get_json() == {"message": "User testuser registered successfully"}

    def test_register_failure_user_exist(self, client, init_database):
        response = client.post("/register_user",
                            json={
                                "username": "testuser",
                                "password": "testpass"
                            })
        print(response.get_json(), "Test Register Failure ###########################")
        # assert response.status_code == 400
        # assert response.get_json() == {"message": "User already exists"}

    def test_register_failure_missing_fields(self, client, init_database):
        response = client.post("/register_user",
                            json={
                                "username": "testuser"
                            })
        print(response.get_json(), "Test Register Fail Missing requiredure")
        assert response.status_code == 400
        assert response.get_json() == {"message": "Field required"}

    def test_get_user(self, client, init_database):
        
        response = client.get("/get_user")
        print(response.get_json(), "Test Get User ###########################")
        # assert response.status_code == 200
        # assert response.get_json() == {"message": [{"id": 1, "username": "testuser"}]}



    def test_update_user(self, client, init_database):
        response = client.put("/update_user/1",
                            json={
                                "username": "updateduser",
                                "password": "testpass"
                            })
        print(response.get_json(), "Test Update User ###########################")
        # assert response.status_code == 200
        # assert response.get_json() == {"message": "User updateduser updated successfully"}

    def test_update_user_failure(self, client, init_database):
        response = client.put("/update_user/2",
                            json={
                                "username": "updateduser",
                                "password": "testpass"
                            })
        print(response.get_json(), "Test Update User Failure")
        assert response.status_code == 404
        assert response.get_json() == {"message": "User not Found"}

    def test_login(self, client, init_database):
        response = client.post("/login",
                            json={
                                "username": "updateduser",
                                "password": "testpass"
                            })
        print(response.get_json(), "Test Login ###########################")
        # assert response.status_code == 200
        # assert response.get_json()["message"] == "Logged in as updateduser"

    def test_login_failure_wrong_pass(self, client, init_database):
        response = client.post("/login",
                            json={
                                "username": "updateduser",
                                "password": "wrongpass"
                            })
        print(response.get_json(), "Test Login Failure - Wrong Password ###########################")
        # assert response.status_code == 401
        # assert response.get_json() == {"message": "Invalid credentials"}

    def test_login_failure_no_user(self, client, init_database):
        response = client.post("/login",
                            json={
                                "username": "nonexistentuser",
                                "password": "wrongpass"
                            })
        print(response.get_json(), "Test Login Failure - No User")
        assert response.status_code == 404
        assert response.get_json() == {"message": "User not Found"}

    def test_logout(self, client, init_database):
        response = client.post("/logout")
        print(response.get_json(), "Test Logout")
        assert response.status_code == 200
        assert response.get_json() == {"message": "Logged out successfully"}

    def test_delete_user(self, client, init_database):
        response = client.delete("/delete_user/1",
                            json={
                                "username": "testuser",
                                "password": "testpass"
                            })
        print(response.get_json(), "Test Delete User ###########################")
        # assert response.status_code == 200
        # assert response.get_json() == {"message": "User updateduser deleted successfully"}

    def test_delete_user_failure(self, client, init_database):
        response = client.delete("/delete_user/2",
                            json={
                                "username": "testuser",
                                "password": "testpass"
                            })
        print(response.get_json(), "Test Delete User Failure")
        assert response.status_code == 404
        assert response.get_json() == {"message": "User not Found"}

    def test_get_user_failure(self, client, init_database):
        
        response = client.get("/get_user")
        print(response.get_json(), "Test Get User Failure")
        assert response.status_code == 404
        assert response.get_json() == {"message": "No users found"}
   

# Beginner: SQLite memory DB

# Intermediate: separate PostgreSQL test DB

# Advanced: transaction rollback strategy + containers


##################################JWT Authentication Testing
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@pytest.mark.Auth()
class Test_Authentication:
    def test_auth(self, client, init_database):
        
        response = client.post("/register_user",
                            json={
                                "username": "testuser",
                                "password": "testpass"
                            })
        print(response.get_json(), "Test Register")
        assert response.status_code == 201
        assert response.get_json() == {"message": "User testuser registered successfully"}

        response = client.post("/login",
                            json={
                                "username": "testuser",
                                "password": "testpass"
                            })
        print(response.get_json(), "Test Login")
        assert response.status_code == 200
        token = response.get_json()["access_token"]
        assert token is not None

        auth_response = client.get("/check_auth", headers={"Authorization": f"Bearer {token}"})
        print(auth_response.get_json(), "Test Check Auth")
        assert auth_response.status_code == 200
        assert auth_response.get_json() == {"message": "You testuser are authenticated!"}


    def test_auth_failure(self, client, init_database):
        response = client.post("/login",
                            json={
                                "username": "testuser",
                                "password": "testpass"
                            })
        print(response.get_json(), "Test Login Failure - Wrong Password ###########################")
        # assert response.status_code == 200
        # token = response.get_json()["access_token"]
        # assert token is not None

        # EDITING TOKEN TO GIVE FAKE JWT ACCESS TOKEN

        token = "this is a fake token"
        auth_response = client.get("/check_auth", headers={"Authorization": f"Bearer {token}"})
        print(auth_response.get_json(), "Test Check Auth Failure with Fake Token")
        assert auth_response.status_code == 422
        assert auth_response.get_json() == {'msg': "Bad Authorization header. Expected 'Authorization: Bearer <JWT>'"}

##################################Factory Boy + Faker in Real API Testing
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# currently we have to give all data manually in the test but with factory boy + faker we can generate fake data automatically and use it in our tests.
# In real backend projects:
# hundreds of tests
# repeated object creation
# duplicate emails
# messy setup
# Tests become ugly. SO THATS WHY WE USE FACTORY BOY + FAKER

# project/
#     app.py
#     models.py

#     tests/
#         conftest.py
#         factories/
#             user_factory.py
#         test_auth.py

@pytest.mark.Integration()
class Test_Factory:
    def test_register_with_factory(self, client, init_database):
        from tests.factories.user_factory import UserFactory

        user = UserFactory.create()# for create only one user
        # user = UserFactory.build()# for create only one user without saving in database
        user = UserFactory.create_batch(50)#for create multiple users in a batch

        response = client.post("/register_user",
                            json={
                                "username": user[0].username+"1",
                                "password": user[0].password
                            })
        print(response.get_json(), "Test Register with Factory")
        assert response.status_code == 201
        assert response.get_json() == {"message": f"User {user[0].username}1 registered successfully"}


####################################Service Layer Testing
####################################Repository Layer Testing
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# What is Repository?
# A repository is a layer whose job is database access.

# class UserRepository:
#     @staticmethod
#     def add_user(user):
#         db.session.add(user)
#         db.session.commit()

#     @staticmethod
#     def get_user_by_username(username):
#         return User.query.filter_by(username=username).first()
    
#     @staticmethod
#     def get_all_users():
#         return User.query.all()#isse sara data aaega
#     #it's latest version of getting all users, earlier it was User.query.all() but now we are using db.session.get() method to get all users.

#     @staticmethod
#     def get_user_by_id(user_id):
#         return db.session.get(User, user_id)


from app.services.user_services import UserService

@pytest.fixture(scope="function") #USING THIS FIXTURE IN SERVICE LAYER TESTING TO CREATE A FAKE REPOSITORY FOR ALL TESTS IN THE MODULE, SO THAT WE CAN USE THE SAME FAKE REPOSITORY IN ALL TESTS AND AVOID DUPLICATE CODE OF CREATING FAKE REPOSITORY IN EACH TEST.   
def fake_repo():
    return Mock()

class FakeUser:
    def __init__(
        self,
        id,
        username,
        password
    ):
        self.id = id
        self.username = username
        self.password = password

@pytest.mark.service()
class Test_Service_Layer_Again:

    def test_register_user_success(self, fake_repo):
        fake_repo.get_user_by_username.return_value = None
        service = UserService(fake_repo)
        result, error, status = service.register_user(
            "serviceuser",
            "servicepass"
        )
        assert status == 201
        assert error is None
        fake_repo.add_user.assert_called_once()


    def test_register_user_already_exists(self, fake_repo):
        fake_repo.get_user_by_username.return_value = (
            FakeUser(
                1,
                "serviceuser",
                "servicepass"
            )
        )
        service = UserService(fake_repo)
        result, error, status = service.register_user(
            "serviceuser",
            "servicepass"
        )
        assert status == 400
        assert error == "User already exists"
        # fake_repo.add_user.assert_not_called()

    
    def test_login_success(self, fake_repo):
        fake_repo.get_user_by_username.return_value = (
            FakeUser(
                1,
                "serviceuser",
                "servicepass"
            )
        )
        with patch("app.services.user_services.create_access_token", return_value="fake jwt token"):
            service = UserService(fake_repo)
            result, error, status = service.login_user(
                "serviceuser",
                "servicepass"
            )
            assert status == 200
            assert error is None
            assert result["message"] == (
                "Logged in as serviceuser"
            )


    def test_login_wrong_password(self, fake_repo):
        fake_repo.get_user_by_username.return_value = (
            FakeUser(
                1,
                "serviceuser",
                "correctpass"
            )
        )
        service = UserService(fake_repo)
        result, error, status = service.login_user(
            "serviceuser",
            "wrongpass"
        )
        assert status == 401
        assert error == "Invalid credentials"


    def test_login_user_not_found(self, fake_repo):
        fake_repo.get_user_by_username.return_value = None
        service = UserService(fake_repo)
        result, error, status = service.login_user(
            "serviceuser",
            "servicepass"
        )
        assert status == 404
        assert error == "User not Found"


    def test_get_user_success(self, fake_repo):
        fake_repo.get_all_users.return_value = [
            FakeUser(
                id=1, 
                username="serviceuser",
                password="servicepass"
            )
        ]
        service = UserService(fake_repo)
        result, error, status = service.get_users()
        assert status == 200
        assert error is None
        assert result == [{"id": 1, "username": "serviceuser"}]


    def test_get_user_not_found(self, fake_repo):
        fake_repo.get_all_users.return_value = None
        service = UserService(fake_repo)
        result, error, status = service.get_users()
        assert status == 404
        assert error == "No users found"
        assert result is None


    def test_update_user_success(self, fake_repo):
        fake_repo.get_user_by_id.return_value = FakeUser(
                        id=1,
                        username="serviceuser",
                        password="servicepass"
                    )
        service = UserService(fake_repo)
        result, error, status = service.update_user(1, "updateduser", "updatedpass")
        assert status == 200
        assert error is None
        assert result == "User updateduser updated successfully"
            
        
    def test_update_user_not_found(self, fake_repo):
        fake_repo.get_user_by_id.return_value = None
        service = UserService(fake_repo)
        result, error, status = service.update_user(1, "updateduser", "updatedpass")
        assert status == 404
        assert error == "User not Found"
        assert result is None


    def test_delete_user_success(self, fake_repo):
        fake_repo.get_user_by_id.return_value = FakeUser(id=1, username="serviceuser", password="servicepass")
        service = UserService(fake_repo)
        result, error, status = service.delete_user(1)
        assert status == 200
        assert error is None
        assert result == "User serviceuser deleted successfully"


    def test_delete_user_not_found(self):
        fake_repo = Mock()
        fake_repo.get_user_by_id.return_value = None
        service = UserService(fake_repo)
        result, error, status = service.delete_user(1)
        assert status == 404
        assert error == "User not Found"
        assert result is None
        

# @pytest.mark.service()
# class Test_Service_Layer:#TESTING SERVICE LAYER WITH MOCK REPOSITORY,BUT THIS IS NOT REAL WAY TO IMPLEMENT SERVICE LAYER TESTING

#     user_name = "serviceuser"
#     password = "servicepass"
#     update_user_name = "serviceuser"
#     update_password = "servicepass"

#     def test_register_user_service(self):
#         fake_repo = Mock()

#         fake_repo.register_user.return_value = f"User {self.user_name} registered successfully", None, 201

#         result, error, status = fake_repo.register_user(self.user_name, self.password)

#         print(result, error, status, "Test Register User Service")
#         assert error is None
#         assert status == 201
#         assert result == f"User {self.user_name} registered successfully"

#     def test_login_user_service(self):
#         fake_repo = Mock()

#         fake_repo.login_user.return_value = f"Logged in as {self.user_name}", None, 200

#         result, error, status = fake_repo.login_user(self.user_name, self.password)

#         print(result, error, status, "Test Login User Service")
#         assert error is None
#         assert status == 200
#         assert result == f"Logged in as {self.user_name}"

#     def test_get_user_service(self):
#         fake_repo = Mock()
#         fake_repo.get_user_service.return_value = [{"id": 1, "username": self.user_name}], None, 200

#         result, error, status = fake_repo.get_user_service()

#         print(result, error, status, "Test Get User Service")
#         assert error is None
#         assert status == 200
#         assert result == [{"id": 1, "username": self.user_name}]

#     def test_update_user_service(self):
#         fake_repo = Mock()
#         fake_repo.update_user_service.return_value = f"User {self.update_user_name} updated successfully", None, 200

#         result, error, status = fake_repo.update_user_service(1, self.update_user_name, self.update_password)

#         print(result, error, status, "Test Update User Service")
#         assert error is None
#         assert status == 200
#         assert result == f"User {self.update_user_name} updated successfully"

#     def test_delete_user_service(self):
#         fake_repo = Mock()
#         fake_repo.delete_user_service.return_value = f"User {self.update_user_name} deleted successfully", None, 200

#         result, error, status = fake_repo.delete_user_service(1)

#         print(result, error, status, "Test Delete User Service")
#         assert error is None
#         assert status == 200
#         assert result == f"User {self.update_user_name} deleted successfully"



from app.repositories.user_repository import UserRepository


# tests/

# ├── test_auth_routes.py
# ├── test_auth_service.py
# ├── test_user_routes.py

@pytest.mark.repo()
class Test_Repository_Layer:

# repository ka kaam hi DB access hai.
# Yaha real DB use karna chahiye.
# Mock nahi.
# Repository ko mock karke repository test karna almost useless ho jata hai.

    username="serviceuser1"
    password="servicepass1"
    
    def test_add_user_repository(self, init_database):
        from app.models.user import User

        user = User(username=self.username, password=self.password)
        UserRepository.add_user(user)
        print("Test Add User Repository")

    def test_get_user_by_username_repository(self, init_database):
        result = UserRepository.get_user_by_username(self.username)
        print(result, "Test Get User by Username Repository ###########################")
        # assert result.id == 1
        # assert result.username == self.username
        # assert result.password == self.password

    def test_get_all_user_repository(self, init_database):
        result = UserRepository.get_all_users()
        print(result, "Test Get all User Repository ###########################")
        # assert result[0].username == self.username
        # assert result[0].password == self.password

    def test_get_user_by__id_repository(self, init_database):
        result = UserRepository.get_user_by_id(1)
        print(result, "Test Get User by User_id Repository ###########################")
        # assert result.id == 1
        # assert result.username == self.username
        # assert result.password == self.password

# tests/
# ├── test_routes.py
#       Real Client
#       Real DB

# ├── test_service.py
#       Mock Repository

# ├── test_repository.py
#       Real Test DB

# ├── test_models.py
#       Real Test DB

# why we use mock in service layer testing instead of real repository, db?
# Suppose login fails.
# Now where is the bug?
# Service logic
# OR
# Repository query
# OR
# Database setup
# OR
# Fixture issue

@pytest.mark.integration()
def test_testing():
    fake_repo = Mock()

    fake_repo.get_user_by_username.return_value = {
        "user_name": "serviceuser1",
        "password": "servicepass1"
    }

    result = fake_repo.get_user_by_username()
    print(result)

    fake_name = Mock(return_value="John Doe")

    result = fake_name()
    print(result)


####################################Test Coverage
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"Mere tests ne kitna code actually test kiya?"
# Iska answer Coverage deta hai.
# pip install pytest-cov
# pytest --cov=app 
# pytest --cov=app --cov-branch
# pytest --cov=app --cov-report=html
# pytest --cov=app --cov-branch --cov-report=html

####################################Unit Test vs Integration Test vs End-to-End Test
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# 1. Unit Test : DB nahi, API nahi, JWT mock, Sab fake.
# Test
#  ↓
# Service
#  ↓
# Mock Repository

# 2. Integration Test : Sab Real hote h
# Route
#  ↓
# Service
#  ↓
# Repository
#  ↓
# SQLite Test DB

# 3. End-to-End (E2E) Test : Sab Real hote
# Open Website
#  ↓
# Register
#  ↓
# Login
#  ↓
# Create Expense
#  ↓
# Delete Expens

####################################MOCK ADVANCE
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class EmailService_2():
    def send(email):
        if email == "himanshu":
            print("email has been sent")
            return True
        return False

@pytest.mark.register
def test_registering_user():
    register = EmailService_2.send.return_value = True
    print(register)

####################################pytest.mark.parametrize
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def is_even(num):
    return num % 2 == 0

@pytest.mark.even
@pytest.mark.parametrize("number" , [2, 4, 6, 8, 10, 14])
def test_is_even(number):
    result = is_even(number)
    if result :
        print(f"Testing if {number} is even")
    else:
        print(f"Testing if {number} is odd")

    assert result == True


@pytest.mark.even
@pytest.mark.parametrize("a , b, expected" , [(1, 2, 3), (2, 3, 5), (3, 5, 8)])
def test_addition(a, b, expected):
    result = a + b
    assert result == expected

####################################Pytest Markers :- smoke, service, regression etc
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# pytest -m "service or repository"
# pytest -m "service and smoke"
# pytest -m "not slow"
# pytest -m repository

# [pytest] # register markers
# markers =
#     smoke: Smoke tests
#     integration: Integration tests
#     service: Service layer tests
#     repository: Repository tests
#     slow: Slow tests


####################################Important Pytest Plugins
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# pytest-mock
# mocker.patch("app.repositories.auth_repositories.AuthRepository.get_user_by_username", return_value=None)

# pytest-xdist
# pytest -n 4 , 4 cpus workers

#pytest-randomly , runs tests randomly.

#pytest-env, used for environment variables in pytest, we can set environment variables in pytest.ini file and use them in our tests.

#pytest-sugar, used to make pytest output more readable

# pytest-cov

####################################CI/CD Testing with GitHub Actions(continous integration and continuous deployment)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



####################################Test Strategy for a Real Backend Project
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Route Layer : Integration Test
# Service Layer : Unit Test (with mocks.)
# Repository Layer : Integration Test(with test DB.)


####################################Real Backend Test Architecture
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# test_login_success
# test_login_username_required
# test_login_password_required
# test_login_username_and_password_required
# test_login_user_not_found
# test_login_invalid_password
# test_login_returns_access_token
# test_login_repository_failure



