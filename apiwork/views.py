from flask.views import MethodView
from flask import Flask, request, Response

from flask import jsonify

class Questions(MethodView):
    questions = [
            {"user_name": "sam", "Description": "What is html", "id": 1},
            {"user_name": "Derick", "Description": "what is data structure", "id": 2},
            {"user_name": "jacob", "Description": "what is javascript", "id": 3},
        ]

    def get(self, id=None):
        
        if id == None:
            return jsonify({'question':[question for question in self.questions]})
        quest = [question for question in self.questions if question['id'] == id]
        return jsonify({'question' : quest[0]})
