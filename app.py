from flask import request, Flask, jsonify, render_template
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)


@app.route('/')
def index():
    # return jsonify({'Question': "harry potter", 'choice': "23", 'answer':"A"})
    return render_template('index.html', RESULT="good")


class Bank(Resource):
    @jwt_required()
    def get(self):
        return {}

    @jwt_required()
    def post(self,name):
        return {}
    
    @jwt_required()
    def delete(self, name):
        return {}




class Question(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('bank',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        return {'item': next(filter(lambda x: x['name'] == name, items), None)}



app.run(port=5000, host='0.0.0.0')
