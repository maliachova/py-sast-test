import hashlib
import hmac
import sqlite3
from pathlib import Path


def hash_password(password: str, salt: str) -> str:
    data = f"{salt}:{password}".encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def safe_equals(left: str, right: str) -> bool:
    return hmac.compare_digest(left, right)


def get_user_by_name(db_path: str, user_name: str):
    conn = sqlite3.connect(db_path)
    try:
        query = "SELECT id, name FROM users WHERE name = ?"
        return conn.execute(query, (user_name,)).fetchall()
    finally:
        conn.close()


def constrained_read_text(base_dir: str, relative_name: str) -> str:
    base = Path(base_dir).resolve()
    target = (base / relative_name).resolve()

    if base not in target.parents and target != base:
        raise ValueError("Path traversal attempt blocked")

    return target.read_text(encoding="utf-8")
