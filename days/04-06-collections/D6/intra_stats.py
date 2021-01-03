import csv
import re
import datetime
from collections import defaultdict, namedtuple

DATA = 'days/04-06-collections/D6/BIO1101-intra.csv'

Student = namedtuple('Student', 'time score question')

def get_score_by_question():
    """Extracts all students form the datafile. For each question, get
    a list of all score on 100.

    Args:
        file (str): datafile
    Return:
        dictionary
    """
    headers = []
    scores_question = defaultdict(list)
    mean_score_by_question = {}
    with open(DATA, encoding='utf-8') as f:
        csvin = csv.reader(f)
        headers = next(csvin)
    with open(DATA, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            for h in headers:
                try:
                    q = re.search('^Q..[0-9]{1,2}',h).group(0)
                    brut = float(line[h])
                    t = float(h[-4:])
                    rel_score = brut/t
                except (ValueError, AttributeError):
                    continue
                scores_question[q].append(rel_score)
    for q, s in scores_question.items():
        mean_score_by_question[q] = round(sum(s)/len(s)*100, 2)
    return {key: value for key, value in sorted(mean_score_by_question.items(), key=lambda item: item[1])}


def time_spent():
    liste_temps = []
    with open(DATA, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                t = datetime.datetime.strptime(line['Temps utilisé'], '%H heures %M min').time()
                secondes = (t.hour * 60 + t.minute) * 60
            except ValueError:
                continue
            liste_temps.append(secondes)
    print(datetime.timedelta(seconds=sum(liste_temps)/len(liste_temps)))


if __name__ == "__main__":
    scores_by_question = get_score_by_question()
    for q, s in scores_by_question.items():
        print(f'{q}\t{s}')
    time_spent()