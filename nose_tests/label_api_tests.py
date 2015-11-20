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