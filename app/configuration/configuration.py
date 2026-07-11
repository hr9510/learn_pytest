import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    
# # ❌ Kamzor Key (Example)
# SECRET_KEY = "mykey12345"  # Sirf 10 bytes

# # ✅ Strong Key (Kam se kam 32 characters)
# SECRET_KEY = "super_secret_complex_key_length_more_than_32_chars_xyz"   
    