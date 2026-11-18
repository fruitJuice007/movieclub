# === Stage 2: Проверка полей ===
# Project: MovieClub
import datetime


class MovieFieldError(ValueError):
    """Ошибка ввода данных фильма."""


def normalize_text(value):
    if value is None:
        return ""
    return value.strip()


def normalize_year(value):
    if value is None:
        return None
    text = normalize_text(value)
    if not text:
        return None
    year = int(text)
    if year < 1888 or year > datetime.date.today().year + 1:
        raise MovieFieldError(
            f"Некорректный год '{year}'. Укажите год от 1888 до {datetime.date.today().year + 1}."
        )
    return year


def validate_movie(title, director, year, genre):
    normalized_title = normalize_text(title)
    if not normalized_title:
        raise MovieFieldError("Название фильма не может быть пустым.")

    normalized_director = normalize_text(director)
    if not normalized_director:
        raise MovieFieldError("Режиссёр не может быть пустым.")

    normalized_genre = normalize_text(genre)
    if not normalized_genre:
        raise MovieFieldError("Жанр не может быть пустым.")

    normalized_year = normalize_year(year)

    return normalized_title, normalized_director, normalized_year, normalized_genre
