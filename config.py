### HTML STATUS CODES ###
OK = 200
UNPROCESSABLE_ENTITY = 422
NOT_FOUND = 404

# SQLAlchemy config (only example not actually set)
SQLALCHEMY_DATABASE_URI = "postgresql://musicmecca:mecca@localhost/musicmecca"

### USER-FACING FLASH ERROR STRINGS ###
ARTIST_NOT_FOUND = 'Could not retrieve artist for id {}'
