from tests.constants import FACK
from tests.nd_test_case import NDTestCase
from flask_app import app


class SongAPITest(NDTestCase):

    def setUp(self):
        super(SongAPITest, self).setUp()

    def test_get(self):
        get_uri = '{}/songs/{}'.format(app.config['BASE_URL'], FACK)
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])
