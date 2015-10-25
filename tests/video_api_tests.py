from tests.constants import FACK_VIDEO
from tests.nd_test_case import NDTestCase
from flask_app import app


class VideoAPITest(NDTestCase):

    def setUp(self):
        super(VideoAPITest, self).setUp()

    def test_get(self):
        get_uri = '{}/videos/{}'.format(app.config['BASE_URL'], FACK_VIDEO)
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])
