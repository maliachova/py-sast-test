from src.safe import safe_equals
from src.utils import normalize_username, is_reasonable_port


def test_safe_equals_true():
    assert safe_equals("token", "token") is True


def test_safe_equals_false():
    assert safe_equals("token", "other") is False


def test_normalize_username():
    assert normalize_username("  Alice Smith! ") == "alice_smith"


def test_reasonable_port():
    assert is_reasonable_port(8080) is True
    assert is_reasonable_port(80) is False
