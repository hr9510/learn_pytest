import factory

from factory.alchemy import SQLAlchemyModelFactory
from faker import Faker
from app.models.user import User
from app import db

fake = Faker() # Faker library ka instance create kar raha hai, jo random data generate karne ke liye use hota hai.


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session  # Auto-session injection

    username = factory.Faker('user_name')  # Random username generate karega
    password = factory.Faker('password')  # Random password generate karega
    # @factory.post_generation