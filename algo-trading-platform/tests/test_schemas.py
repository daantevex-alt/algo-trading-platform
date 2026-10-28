import pytest
from pydantic import ValidationError
from app.schemas.user import UserCreate


def test_user_create_valid():
    user = UserCreate(
        username="trader",
        email="trader@example.com",
        password="strongpass",
        age=25,
    )
    assert user.email == "trader@example.com"


def test_user_create_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(username="x", email="not-an-email", password="pass12345", age=25)


def test_user_create_short_password():
    with pytest.raises(ValidationError):
        UserCreate(username="x", email="a@b.com", password="short", age=25)


def test_user_create_underage():
    with pytest.raises(ValidationError):
        UserCreate(username="x", email="a@b.com", password="longpassword", age=16)
