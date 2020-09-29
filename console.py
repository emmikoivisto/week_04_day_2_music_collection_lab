import pdb 
from models.artists import Artist

import repositories.artist_repository as artist_repository

artist1 = Artist("Cher")
artist_repository.save(artist1)

artist2 = Artist("Kiss")
artist_repository.save(artist2)