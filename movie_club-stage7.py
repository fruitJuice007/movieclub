# === Stage 7: Фильтрация записей ===
# Project: MovieClub
def filter_by_director(films, director):
    return [f for f in films if f.get("режиссёр") == director]

def filter_by_year_range(films, year_start, year_end):
    return [
        f for f in films
        if year_start <= f.get("год", 0) <= year_end
    ]

def filter_films(films, director=None, year_start=None, year_end=None):
    result = films
    if director is not None:
        result = filter_by_director(result, director)
    if year_start is not None:
        result = filter_by_year_range(result, year_start, year_end)
    return result

def find_releases_by_director(films, director, year_start, year_end):
    return filter_by_director(
        filter_by_year_range(films, year_start, year_end),
        director
    )
