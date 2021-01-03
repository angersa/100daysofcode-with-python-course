import csv
from collections import defaultdict, namedtuple

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples). 
    Filter movies anterior to MIN_Year.'''
    directors = defaultdict(list)
    with open(MOVIE_DATA, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title']
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            m = Movie(title=movie, year=year, score=score)
            if m.year >= MIN_YEAR:
                directors[director].append(m)
    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score.
    Structure: dict = {[director, avg]: Movies}.
    Return dictionary sorted by average score.'''
    directors_score = {}
    for director, movies in directors.items():
        if len(movies) >= 4:
            avg = _calc_mean(movies)
            directors_score[(director, avg)] = movies
    return {key: value for key, value in sorted(directors_score.items(), key=lambda item: item[0][-1], reverse=True)}



def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    scores = [m.score for m in movies]
    return round(sum(scores)/len(scores), 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    rank = 0
    for director, movies in directors.items():
        rank += 1
        if rank <= 20:
            print(fmt_director_entry.format(counter=rank, director=director[0], avg=director[1]))
            print(sep_line)
            for movie in movies:
                print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))
            print()


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)



if __name__ == '__main__':
    main()