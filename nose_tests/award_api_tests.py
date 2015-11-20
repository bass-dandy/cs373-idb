from nose_tests.constants import BEST_IN_THE_WORLD
from nose_tests.nd_test_case import NDTestCase
from flask_app import app


class AwardAPITest(NDTestCase):

    def setUp(self):
        super(AwardAPITest, self).setUp()

    def test_get(self):
        get_uri = '{}/awards/{}'.format(app.config['BASE_URL'], BEST_IN_THE_WORLD)
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])
