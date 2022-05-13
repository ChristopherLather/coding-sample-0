from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class CutString(Resource):
    def post(self):
        try:
            string_to_cut = request.json['string_to_cut']
            letters_to_cut = list(string_to_cut)
            letters = [x for x in letters_to_cut if (letters_to_cut.index(x) + 1) % 3 == 0]
            return_string = ''.join(letters)
        except:
            return 'Invalid request'
        return {'return_string': return_string}

api.add_resource(CutString, '/test')

if __name__ == '__main__':
    app.run(debug=True)