# === Stage 5: Связанная сущность ===
# Project: MovieClub
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Watch:
    """Просмотр фильма пользователем.

    Связан с фильмом по его идентификатору. Хранит дату просмотра,
    оценку и краткое впечатление о фильме.
    """

    movie_id: int
    user_id: int
    date: str
    rating: int
    comment: str = ""

    def __post_init__(self) -> None:
        if not 1 <= self.rating <= 5:
            raise ValueError("Оценка должна быть от 1 до 5")


class WatchBook:
    """Книга просмотров: связывает сущности фильмов с просмотрами."""

    def __init__(self) -> None:
        self._movies: dict = {}
        self._watches: List[Watch] = []

    def add_movie(self, title: str, director: str, year: int, genre: str) -> int:
        """Добавляет фильм и возвращает его сгенерированный идентификатор."""
        movie_id = len(self._movies) + 1
        self._movies[movie_id] = {
            "title": title,
            "director": director,
            "year": year,
            "genre": genre,
        }
        return movie_id

    def get_movie(self, movie_id: int) -> Optional[dict]:
        """Возвращает данные фильма по идентификатору или None."""
        return self._movies.get(movie_id)

    def add_watch(
        self,
        movie_id: int,
        user_id: int,
        date: str,
        rating: int,
        comment: str = "",
    ) -> Watch:
        """Добавляет запись о просмотре фильма.

        Проверяет существование фильма по переданному идентификатору и
        валидность оценки. Возвращает созданную запись.
        """
        if movie_id not in self._movies:
            raise ValueError(f"Фильм с идентификатором {movie_id} не найден")
        watch = Watch(
            movie_id=movie_id,
            user_id=user_id,
            date=date,
            rating=rating,
            comment=comment,
        )
        self._watches.append(watch)
        return watch

    def get_watches(self, movie_id: int) -> List[Watch]:
        """Возвращает все записи о просмотрах указанного фильма."""
        return [w for w in self._watches if w.movie_id == movie_id]

    def average_rating(self, movie_id: int) -> Optional[float]:
        """Вычисляет среднюю оценку фильма по всем его просмотрам."""
        watches = self.get_watches(movie_id)
        if not watches:
            return None
        return sum(w.rating for w in watches) / len(watches)
