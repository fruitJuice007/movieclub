# === Stage 4: Редактирование записей ===
# Project: MovieClub
EDITABLE_FIELDS = ("title", "director", "year", "genre")


def edit_movie(movie_id, changes):
    """Редактирует фильм по идентификатору с проверкой допустимых полей.

    changes - словарь с полями для обновления.
    Возвращает обновлённый фильм или None при ошибке.
    """
    if not isinstance(changes, dict):
        return None

    new_changes = {}
    for key, value in changes.items():
        if key not in EDITABLE_FIELDS:
            raise ValueError(f"Поле '{key}' не подлежит редактированию")
        new_changes[key] = value

    movie = _find_movie(movie_id)
    if movie is None:
        return None

    for key, value in new_changes.items():
        movie[key] = value

    return movie


def _find_movie(movie_id):
    """Находит фильм по идентификатору в глобальном реестре фильмов."""
    for movie in _get_all_movies():
        if movie.get("id") == movie_id:
            return movie
    return None


def _get_all_movies():
    """Возвращает список всех фильмов из основного модуля."""
    try:
        from main import MOVIE_DB
        return MOVIE_DB
    except ImportError:
        return []
