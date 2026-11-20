# === Stage 3: Хранилище в памяти ===
# Project: MovieClub
from typing import List, Optional, Dict


class Movie:
    def __init__(self, title: str, director: str, year: int, genre: str) -> None:
        self.id = self._generate_id()
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre

    @staticmethod
    def _generate_id() -> int:
        return len(MovieStore._all_ids) + 1

    def __repr__(self) -> str:
        return f"Movie(id={self.id}, title={self.title!r}, director={self.director!r}, year={self.year}, genre={self.genre!r})"


class MovieStore:
    _all_ids: List[int] = []
    _movies: Dict[int, Movie] = {}

    @classmethod
    def add_movie(cls, title: str, director: str, year: int, genre: str) -> Movie:
        movie = Movie(title, director, year, genre)
        cls._movies[movie.id] = movie
        cls._all_ids.append(movie.id)
        return movie

    @classmethod
    def get_movie(cls, movie_id: int) -> Optional[Movie]:
        return cls._movies.get(movie_id)

    @classmethod
    def list_movies(cls) -> List[Movie]:
        return list(cls._movies.values())

    @classmethod
    def clear(cls) -> None:
        cls._movies.clear()
        cls._all_ids.clear()
