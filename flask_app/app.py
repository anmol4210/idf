from flask import Flask
from flask_restful import Resource,Api,reqparse
from model import get_model,pre_process

app = Flask(__name__)
api = Api(app)

text_classifier = get_model('./model.sav')

post_args = reqparse.RequestParser()
post_args.add_argument("text",type=str,help="Text is required",required=True)

class ClassifyText(Resource):
    def get(self):
        return "Send Post Request with conversation inside text keyword"
    
    def post(self):
        args = post_args.parse_args()
        text = args["text"]
        text = pre_process(text)
        output =  text_classifier.predict([text])
        return output[0]

api.add_resource(ClassifyText,"/classify")

if __name__ == '__main__':
    app.run(debug=True)
