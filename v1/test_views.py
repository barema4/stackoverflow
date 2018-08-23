
"""This is the main module"""
import unittest
import json
from json import JSONEncoder

from app import APP
class TestViews(unittest.TestCase):
    """
    Class defines test cases
    """
    def setUp(self):
        """
        initializing
        """
        self.question = APP
        self.client = self.question.test_client
    def test_get_all_questions(self):
        """
        method for testing get all questions
        """
        result = self.client().get('api/v1/questions')
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["questions"])
        result2 = self.client().get('/api/v1/questions/@')
        self.assertEqual(result2.status_code, 404)

        result3 = self.client().get('/api/v1/questions/5/')
        self.assertEqual(result3.status_code, 404)

        result4 = self.client().get('/api/v1/questions/2/')
        self.assertEqual(result4.status_code, 404)

    def test_get_specific_question(self):
        """
        testing for get specific question
        """
        result = self.client().get('api/v1/questions/2')
        self.assertEqual(result.status_code, 200)
        result1 = self.client().get('/api/v1/questions/ak/')
        self.assertEqual(result1.status_code, 404)

        result2 = self.client().get('/api/v1/questions/@')
        self.assertEqual(result2.status_code, 404)

        result3 = self.client().get('/api/v1/questions/4/')
        self.assertEqual(result3.status_code, 404)

        result4 = self.client().get('/api/v1/questions/6/')
        self.assertEqual(result4.status_code, 404)
        
    def test_create_question(self):
        """
        testing for create question
        """
        result = self.client().post('api/v1/questions', content_type="application/json", data=json.dumps(dict(id=4, title="", body="", user_name="Gayaza")))
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["questions"])
        
    def test_requests(self):
        """
        testing for answering question
        """
        result = self.client().post('/api/v1/questions/2/answers', content_type="application/json", data=json.dumps(dict(answer_id=4, question_id=5, body="hello")))
        
        self.assertTrue(result.json["solutions"])
        
        
