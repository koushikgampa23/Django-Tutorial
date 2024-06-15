from ..models import CustomUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.validators import ValidationError
import jwt


class Login(APIView):
    """To print http response"""

    def get(self, request) -> None:
        """Function to give response as hello world"""
        return Response("Hello World")

    def post(self, request) -> None:
        "if user login generate tokens"
        data = request.data
        username = data.get("username", None)
        password = data.get("password", None)
        user = CustomUser.objects.filter(username=username).first()
        if user:
            if user.check_password(password):
                key = "secret"
                encode_jwt = jwt.encode(
                    {"username": username, "id": user.id}, key, algorithm="HS256"
                )
                response = Response({"message": "Logged In successfull"})
                response.set_cookie("token", encode_jwt)
                return response
            raise ValidationError({"error": "Reenter the password again"})
        raise ValidationError({"error": "User doesnot Exist"})
        # decode_jwt = jwt.decode(encode_jwt, key, algorithms=["HS256"])
        # return Response({"encoded_jwt": encode_jwt, "decoded_jwt": decode_jwt})
