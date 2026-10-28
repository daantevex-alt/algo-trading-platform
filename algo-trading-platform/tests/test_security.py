import pytest
from app.core.security import hash_password, verify_password


def test_hash_password_returns_string():
    hashed = hash_password("mypassword123")
    assert isinstance(hashed, str)
    assert hashed != "mypassword123"


def test_hash_password_is_bcrypt():
    hashed = hash_password("secret")
    assert hashed.startswith("$2b$")


def test_verify_password_correct():
    password = "correct_password"
    hashed = hash_password(password)
    assert verify_password(password, hashed) is True


def test_verify_password_wrong():
    hashed = hash_password("real_password")
    assert verify_password("wrong_password", hashed) is False


def test_same_password_different_hashes():
    h1 = hash_password("same")
    h2 = hash_password("same")
    assert h1 != h2
    # Но оба должны верифицироваться
    assert verify_password("same", h1) is True
    assert verify_password("same", h2) is True
