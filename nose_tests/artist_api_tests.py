from nose_tests.constants import EMINEM
from nose_tests.nd_test_case import NDTestCase
from flask_app import app


class ArtistAPITest(NDTestCase):

    def setUp(self):
        super(ArtistAPITest, self).setUp()

    def test_get(self):
        get_uri = '{}/artists/{}'.format(app.config['BASE_URL'], EMINEM)
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

    def test_get_by_name(self):
        get_uri = '{}/artists/{}'.format(app.config['BASE_URL'], 'Eminem')
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

    def test_get_all(self):
        get_uri = '{}/artists/'.format(app.config['BASE_URL'])
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

        get_uri = '{}/artists'.format(app.config['BASE_URL'])
        response = self.json_get(get_uri)

        reponse_dict_cmp = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

        self.assertEqual(reponse_dict, reponse_dict_cmp)

    def test_get_all_pagination(self):
        get_uri = '{}/artists?page=1&order=asc&pagesize=12'.format(app.config['BASE_URL'])
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

        self.assertEqual(reponse_dict[0]['bio'], 'Rapper')
