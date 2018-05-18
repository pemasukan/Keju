import scholarly
def cari(nama):
    return next(scholarly.search_author('Steven A. Cholewiak')).fill()
    #print(nama)

import scholarly
def coba(nama):
    return next(scholarly.search_author(nama)).fill()