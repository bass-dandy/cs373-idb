from tests.constants import CURTAIN_CALL
from tests.nd_test_case import NDTestCase
from flask_app import app


class ReleaseAPITest(NDTestCase):

    def setUp(self):
        super(ReleaseAPITest, self).setUp()

    def test_get(self):
        get_uri = '{}/releases/{}'.format(app.config['BASE_URL'], CURTAIN_CALL)
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])
