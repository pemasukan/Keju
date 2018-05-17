import scholarly
def cari(nama):
    return next(scholarly.search_author(nama))