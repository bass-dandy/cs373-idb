from nose_tests.constants import SLIM_SHADY_RECORDS
from nose_tests.nd_test_case import NDTestCase
from flask_app import app


class LabelAPITest(NDTestCase):

    def setUp(self):
        super(LabelAPITest, self).setUp()

    def test_get(self):
        get_uri = '{}/labels/{}'.format(app.config['BASE_URL'], SLIM_SHADY_RECORDS)
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

    def test_get_all(self):
        get_uri = '{}/labels'.format(app.config['BASE_URL'])
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

        get_uri = '{}/labels/'.format(app.config['BASE_URL'])
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

    def test_get_all_pagination(self):
        get_uri = '{}/labels?page=1&order=asc&pagesize=12'.format(app.config['BASE_URL'])
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

        self.assertEqual(reponse_dict[0]['bio'], 'Home of Slim Shady')
