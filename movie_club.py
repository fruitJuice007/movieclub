# === Stage 1: Каркас модуля ===
# Project: MovieClub
from dataclasses import dataclass, field
from typing import List


@dataclass
class Film:
    title: str
    director: str
    year: int
    genre: str

    @property
    def age(self) -> int:
        return 2025 - self.year


def demo_films() -> List[Film]:
    return [
        Film("Криминальное чтиво", "Квентин Тарантино", 1994, "Криминал"),
        Film("Начало", "Кристофер Нолан", 2010, "Фантастика"),
        Film("Побег из Шоушенка", "Фрэнк Дарабонт", 1994, "Драма"),
        Film("Интерстеллар", "Кристофер Нолан", 2014, "Фантастика"),
    ]


def main() -> None:
    films = demo_films()
    for film in films:
        print(f"{film.title} ({film.year}), {film.director} — "
              f"{film.genre}, рейтинг {film.age}+")
    print(f"\nДобро пожаловать в MovieClub — "
          f"найдено фильмов: {len(films)}")


if __name__ == "__main__":
    main()
