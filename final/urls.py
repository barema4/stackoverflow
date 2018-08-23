# -*- coding: utf-8 -*-
"""
Module decorates views to urls
"""
from views import GetQuestion
class GetUrls:
    """
    Method that views with urls
    """
    @staticmethod
    def fetch_urls(app):
        """
        Method that views with urls
        """
        questions_view = GetQuestion.as_view('questions')
        app.add_url_rule('/api/v1/questions', view_func=questions_view, defaults={'question_id': None}, methods=['GET',])
        app.add_url_rule('/api/v1/questions/<int:question_id>', view_func=questions_view, methods=['GET',])
        solutions_view = GetQuestion.as_view('solutions')
        app.add_url_rule('/api/v1/questions', defaults={'question_id': None}, view_func=questions_view, methods=['POST',])
        app.add_url_rule('/api/v1/questions/<int:question_id>/answers', view_func=solutions_view, methods=['POST',])