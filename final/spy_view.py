from flask.views import MethodView
from flask import Flask, request, Response

from flask import jsonify

class Questions(MethodView):
    questions = [
            {"user_name": "sam", "Description": "What is html",  "id": 1},
            {"user_name": "Derick", "Description": "what is data structure",  "id": 2},
            {"user_name": "jacob", "Description": "what is javascript", "id": 3},
        ]


    def get(self, id=None):

        if id == None:
            return jsonify({'question': [question for question in self.questions]})
        quest = [question for question in self.questions if question['id'] == id]
        return jsonify({'question': quest[0]})

    def post(self, id=None):
        """
        method for all post requests
        """

        if not request.json:
            return jsonify({'error': "not a json request"}), 400
        else:
                question = {'user_name': request.json['user_name'], 'Description': request.json['Description'],
                            'id': request.json['id']}
                self.questions.append(question)
                return jsonify({'questions': self.questions}), 201

class SpecificAnswer(MethodView):
    Answers = [
        {"user_name": "sam", "Description": "What is html", "answer": "", "id": 1},
        {"user_name": "Derick", "Description": "what is data structure", "answer": "", "id": 2},
        {"user_name": "jacob", "Description": "what is javascript", "answer": "", "id": 3},
    ]
    def post(self,id):

        if not request.json:

            return jsonify({'error': "not a json request"}), 400

        else:

            answer = {'user_name': request.json['user_name'], 'Description': request.json['Description'], 'answer': request.json['answer'], 'id': request.json['id']}


            self.Answers.append(answer)

            return jsonify({'Answers': self.Answers})
