from nose_tests.nd_test_case import NDTestCase
from flask_app import app


class SearchAPITest(NDTestCase):

    def setUp(self):
        super(SearchAPITest, self).setUp()
        
    def test_get_full_name(self):
        response = self.json_get('{}/?q=Eminem'.format(app.config['BASE_URL']))
    
        reponse_dict = self.dict_from_response(response)
    
        self.assertEqual(response.status_code, app.config['OK'])

    def test_get_partial_name(self):
        response = self.json_get('{}/?q=Em'.format(app.config['BASE_URL']))

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

    def test_case_insensitive(self):
        response = self.json_get('{}/?q=Em'.format(app.config['BASE_URL']))

        reponse_dict = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

        response = self.json_get('{}/?q=em'.format(app.config['BASE_URL']))

        reponse_dict_cmp = self.dict_from_response(response)

        self.assertEqual(response.status_code, app.config['OK'])

        self.assertEqual(reponse_dict, reponse_dict_cmp)


