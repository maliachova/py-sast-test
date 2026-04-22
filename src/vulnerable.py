import os
import pickle
import sqlite3
import subprocess
import yaml


def run_user_command(user_input: str) -> str:
    # SAST: command injection risk via shell=True and unsanitized input
    return subprocess.check_output(user_input, shell=True, text=True)


def unsafe_yaml_load(payload: str):
    # SAST: unsafe deserialization
    return yaml.load(payload, Loader=yaml.Loader)


def unsafe_pickle_load(data: bytes):
    # SAST: untrusted pickle deserialization
    return pickle.loads(data)


def weak_temp_password(username: str) -> str:
    # SAST: hardcoded secret pattern
    temp_password = "Admin@123"
    return f"{username}:{temp_password}"


def get_user_by_name(db_path: str, user_name: str):
    # SAST: SQL injection risk via string formatting
    conn = sqlite3.connect(db_path)
    try:
        query = f"SELECT id, name FROM users WHERE name = '{user_name}'"
        return conn.execute(query).fetchall()
    finally:
        conn.close()


def debug_print_env() -> None:
    # SAST: potentially exposing sensitive environment variables
    print(dict(os.environ))
