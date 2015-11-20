### BASE URL ###
BASE_URL = '/api'

### HTML STATUS CODES ###
OK = 200
UNPROCESSABLE_ENTITY = 422
NOT_FOUND = 404

# SQLAlchemy config (only example not actually set)
SQLALCHEMY_DATABASE_URI = "postgresql://musicmecca:mecca@localhost/musicmecca"

### USER-FACING FLASH ERROR STRINGS ###
ARTIST_NOT_FOUND = 'Could not retrieve artist for id {}'
LABEL_NOT_FOUND = 'Could not retrieve label for id {}'
CONCERT_NOT_FOUND = 'Could not retrieve concert for id {}'
TVPRESENCE_NOT_FOUND = 'Could not retrieve tv presence for id {}'
RELEASE_NOT_FOUND = 'Could not retrieve release for id {}'
VIDEO_NOT_FOUND = 'Could not retrieve video for id {}'
AWARD_NOT_FOUND = 'Could not retrieve award for id {}'
SONG_NOT_FOUND = 'Could not retrieve song for id {}'
