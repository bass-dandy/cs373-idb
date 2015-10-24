from tests.constants import EMINEM
from tests.nd_test_case import NDTestCase
from flask_app import app

class TicketAPITest(NDTestCase):

    def setUp(self):
        super(TicketAPITest, self).setUp()

    def test_get_high_urgency_ticket(self):
        get_uri = '{}/artists/{}'.format(app.config['BASE_URI'], EMINEM)
        response = self.json_get(get_uri)

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])
