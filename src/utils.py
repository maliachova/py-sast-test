import re


def normalize_username(raw: str) -> str:
    value = raw.strip().lower()
    value = re.sub(r"\s+", "_", value)
    return re.sub(r"[^a-z0-9_]", "", value)


def is_reasonable_port(port: int) -> bool:
    return 1024 <= port <= 65535
