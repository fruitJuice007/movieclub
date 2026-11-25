# === Stage 6: Генерация идентификаторов ===
# Project: MovieClub
import string
import time
import uuid

PROJECT_PREFIX = "mc"


def _is_available(identifier: str, used: set[str]) -> bool:
    return identifier not in used


def generate_unique_identifier(used: set[str], *, length: int = 10) -> str:
    alphabet = string.ascii_lowercase + string.digits
    while True:
        candidate = "".join(
            alphabet[int((time.time_ns() >> (i % 64)) & 0x3F)]
            for i in range(length)
        )
        identifier = f"{PROJECT_PREFIX}-{candidate}"
        if _is_available(identifier, used):
            used.add(identifier)
            return identifier


def generate_unique_id() -> str:
    return generate_unique_identifier(set())


def generate_unique_id_with(used: set[str]) -> str:
    return generate_unique_identifier(used)
