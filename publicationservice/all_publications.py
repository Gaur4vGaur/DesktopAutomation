import json
import urllib.request

from persistence.persist import update

ALL_PUBLICATIONS = "./all_publications_sorted_by_year.json"


def sort_by_year(pub):
    return pub['year']


"""
The file is only used once when we need to refresh the db
"""
if __name__ == '__main__':
    # check this everytime on page
    publications_url = "https://research.google/static/data/" \
                       "publications-758c6de0e0664d961c861c29abd006034a729a53182fff5438270d0fe918b547.json"
    contents = urllib.request.urlopen(publications_url).read()
    parsed = json.loads(contents)
    publications = parsed.get("publications")
    publications.sort(reverse=True, key=sort_by_year)
    update(publications, ALL_PUBLICATIONS)
