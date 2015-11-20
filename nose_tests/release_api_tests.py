from nose_tests.constants import CURTAIN_CALL
from nose_tests.nd_test_case import NDTestCase
from flask_app import app


class ReleaseAPITest(NDTestCase):

    def setUp(self):
        super(ReleaseAPITest, self).setUp()

    def test_get(self):
        get_uri = '{}/releases/{}'.format(app.config['BASE_URL'], CURTAIN_CALL)
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

    def test_get_all(self):
        get_uri = '{}/releases'.format(app.config['BASE_URL'])
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

        get_uri = '{}/releases/'.format(app.config['BASE_URL'])
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

    def test_get_all_pagination(self):
        get_uri = '{}/releases?page=1&order=asc&pagesize=12'.format(app.config['BASE_URL'])
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

        self.assertEqual(reponse_dict[0]['name'], 'Curtain Call')
