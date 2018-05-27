import scholarly
def cari(nama):
    search_query = scholarly.search_author(nama)
    return next(search_query)