import traceback

from core.authentication import authenticate
from flask_restx import Resource, Namespace

from services.chat_response_service import generate_chat_response

chat_controller_api = Namespace("api")


@chat_controller_api.route("/chat")
@authenticate
class AiResponseController(Resource):
    def post(self):
        try:
            user_messages = chat_controller_api.payload # JSON body of the API request
            response = generate_chat_response(user_messages)
            return response, 201
        except Exception as e:
            print(traceback.format_exc())
            return {"error": str(e)}, 500

    def get(self):
        try:
            response = "Test success!"
            return response, 201
        except Exception as e:
            print(traceback.format_exc())
            return {"error": str(e)}, 500
