from pydantic import BaseModel, ValidationError, Field, ConfigDict

class UserRegisterSchema(BaseModel):
    username : str = Field(..., min_length=3)
    password : str = Field(..., min_length=8)

    model_config = ConfigDict(extra='forbid')