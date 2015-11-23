from nose_tests.constants import EMINEM
from nose_tests.nd_test_case import NDTestCase
from flask_app import app


class DiscussionAPITest(NDTestCase):

    def setUp(self):
        super(DiscussionAPITest, self).setUp()

    def test_get(self):
        uri = '{}/artists/{}/discussions'.format(app.config['BASE_URL'], EMINEM)
        response = self.json_get(uri)

        self.assertEqual(response.status_code, app.config['NOT_FOUND'])

        payload = {
            'discussion': 'Bust that crazy shit!'
        }
        response = self.json_post(uri, payload, data_json=True)
        self.assertEqual(response.status_code, app.config['OK'])
        response_dict = self.dict_from_response(response)

        self.assertEqual(response_dict['discussion'], 'Bust that crazy shit!')

        uri = '{}/artists/{}/discussions'.format(app.config['BASE_URL'], EMINEM)
        response = self.json_get(uri)

        self.assertEqual(response.status_code, app.config['OK'])
        response_dict = self.dict_from_response(response)
        self.assertEqual(response_dict[0]['discussion'], 'Bust that crazy shit!')

        id = response_dict[0]['id']

        #test a reply
        uri = '{}/discussions/{}'.format(app.config['BASE_URL'], id)
        response = self.json_get(uri)

        self.assertEqual(response.status_code, app.config['NOT_FOUND'])

        payload = {
            'reply': 'MORE WACKY SHIT!'
        }
        response = self.json_post(uri, payload, data_json=True)
        self.assertEqual(response.status_code, app.config['OK'])
        response_dict = self.dict_from_response(response)

        self.assertEqual(response_dict['reply'], 'MORE WACKY SHIT!')

        uri = '{}/discussions/{}'.format(app.config['BASE_URL'], id)
        response = self.json_get(uri)

        payload = {
            'reply': 'AHHHHHHHH!'
        }
        response = self.json_post(uri, payload, data_json=True)
        self.assertEqual(response.status_code, app.config['OK'])
        response_dict = self.dict_from_response(response)

        self.assertEqual(response_dict['reply'], 'AHHHHHHHH!')

        uri = '{}/artists/{}/discussions'.format(app.config['BASE_URL'], EMINEM)
        response = self.json_get(uri)

        self.assertEqual(response.status_code, app.config['OK'])

        response_dict = self.dict_from_response(response)
        self.assertEqual(len(response_dict[0]['reply']), 2)


