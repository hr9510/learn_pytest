import pytest

# @pytest.fixture(autouse=True, scope="module")
# def setUp_and_teardown():
#     print("Launch Browser")
#     print("Open application URL in the browser")
#     yield
    # print("Logout from application")
    # print("Close the browser")



################################# USING HOOK FUNCTION (WORKS SAME AS FIXTURES)
############## FOR SESSION 
# def pytest_sessionstart(session):
#     print("SESSION SETUP")

# def pytest_sessionfinish(session):
#     print("SESSION TEARDOWN")   

# ############## FOR PACKAGE 

# @pytest.fixture(scope="session", autouse=True)
# def package_setup():
#     print("Package Setup")
#     yield
#     print("Package Teardown")

################### CREATING FIXTURE IN CONFTEST.PY AND USE IT IN THE TEST
@pytest.fixture(scope="class")
def fixture_setup_and_teardown(request):
    driver = "i'm the driver"
    print("Fixture Setup")
    request.cls.driver = driver
    yield
    print("Fixture Teardown")



from app import create_app, db
app = create_app()
@pytest.fixture(scope="class")
def init_database():
    with app.app_context():
        db.create_all()  # create tables
        yield db  # return the database object to the test function
        db.session.rollback()
        db.drop_all()  # drop tables after test is done
        db.session.rollback()
        db.session.remove()


@pytest.fixture(scope="function") #creating fixture for flask app testing to reduce redundancy and increase reusability
def client():
    with app.test_client() as client:
        yield client  # here yield is used to return the client object to the test function and then after the test function is executed, it will continue with any code written after yield (if any) for teardown or cleanup purposes.





# from running import app, db
# @pytest.fixture(scope="function")
# def application():
#     with app.test_client():
#         db.create_all()
#         yield application
#         db.session.rollback()
#         db.drop_all()

# TESTING KE PS KHUDKA DB NHI H WO BACKEND KA DB HI USE KR RHA H TO ISKA ALG SE KHA SE LAE DB