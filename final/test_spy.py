import unittest
import json


from app import APP


class TestViews(unittest.TestCase):
    """
    Class defines test cases
    """

    def setUp(self):

        self.question = APP
        self.client = self.question.test_client

    def test_get(self):


        result = self.client().get('/api/v1/questions/')
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["question"])

    def test_get(self):
        result = self.client().get('/api/v1/questions/2')
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["question"])


    def test_post(self):

        result = self.client().post('api/v1/questions', content_type="application/json", data=json.dumps(
            dict(id=2, Description="what is javascript", user_name="sarah",
                 )))
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["questions"])
        self.assertIn('Description', str(result.data))

    def test_post(self):


        result = self.client().post('/api/v1/questions/3/answers', content_type="application/json",
                                    data=json.dumps(dict(id=4, user_name="Junior Sara", Description="what is javascript",answer="sawre")))

        self.assertAlmostEquals(result.status_code, 200)
        # self.assertIn("id", result.data)