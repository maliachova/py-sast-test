from safe import get_user_by_name as safe_get_user
from vulnerable import get_user_by_name as vuln_get_user


def demo() -> None:
    db_path = "example.db"

    print("Safe query:")
    print(safe_get_user(db_path, "alice"))

    print("Unsafe query:")
    print(vuln_get_user(db_path, "alice' OR '1'='1"))


if __name__ == "__main__":
    demo()
