from nose_tests.constants import EMINEM
from nose_tests.nd_test_case import NDTestCase
from flask_app import app


class ArtistAPITest(NDTestCase):

    def setUp(self):
        super(ArtistAPITest, self).setUp()

    def test_get(self):
        get_uri = '{}/artists/{}?q=test'.format(app.config['BASE_URL'], EMINEM)
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])
