from tests.constants import ACL
from tests.nd_test_case import NDTestCase
from flask_app import app


class ConcertAPITest(NDTestCase):

    def setUp(self):
        super(ConcertAPITest, self).setUp()

    def test_get(self):
        get_uri = '{}/concerts/{}'.format(app.config['BASE_URL'], ACL)
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])
