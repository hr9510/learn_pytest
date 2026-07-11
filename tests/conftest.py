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
@pytest.fixture(scope="function")
def fixture_setup_and_teardown(request):
    driver = "i'm the driver"
    print("Fixture Setup")
    request.cls.driver = driver
    yield
    print("Fixture Teardown")





from app import create_app, db


@pytest.fixture(scope="function")
def app():
    """Create and configure a test app."""
    app = create_app()
    
    # Configure test database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Test client for making requests."""
    return app.test_client()

@pytest.fixture
def init_database(app):
    """Initialize database for tests."""
    with app.app_context():
        yield db

# from running import app, db
# @pytest.fixture(scope="function")
# def application():
#     with app.test_client():
#         db.create_all()
#         yield application
#         db.session.rollback()
#         db.drop_all()

# TESTING KE PS KHUDKA DB NHI H WO BACKEND KA DB HI USE KR RHA H TO ISKA ALG SE KHA SE LAE DB