# stackoverflow
Questions and Answers

[![Build Status](https://travis-ci.org/barema4/stackoverflow.svg?branch=Api_final)](https://travis-ci.org/barema4/stackoverflow)
[![Maintainability](https://api.codeclimate.com/v1/badges/678045f9d54de68f4191/maintainability)](https://codeclimate.com/github/barema4/stackoverflow/maintainability)


[![Coverage Status](https://coveralls.io/repos/github/barema4/stackoverflow/badge.svg?branch=Api_final)](https://coveralls.io/github/barema4/stackoverflow?branch=Api_final)

Link to heroku app:
https://final-apiapp.herokuapp.com/

- Now you can access the system api Endpoints:

|Verb       | End Point                                             |Use                                     
| -------   |-----------------------------------------------      |------------------------------------------|
|  GET      |  /api/v1/questions/                                 |Gets a list of all questions              |
|  GET      | /api/v1/questions/<question_id>/                    |Gets a specific question and the answers  |
|  POST     |/api/v1/questions/                                   |Posting a question                        |
|  POST     |/api/v1/questions/<question_id>/answers/             |Posts answer to a specific question       |
