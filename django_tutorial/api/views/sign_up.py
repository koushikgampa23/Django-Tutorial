from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import CustomUser
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.exceptions import ValidationError


class User(APIView):
    """Signup"""

    # def get_object(self, pk):
    #     obj = CustomUser.objects.filter(id=pk)
    #     if obj.exists():
    #         return obj.first()
    #     return None

    def post(self, request) -> None:
        "Adding user in the database"
        data = request.data

        # Destructing the data
        # Here None used since if the password is not present in the dictonary will get None
        email = data.get("email", None)
        password = data.get("password", None)
        username = data.get("username", None)

        if (email is None) or (password is None) or (username is None):
            return Response("Enter the required Fields")

        find_user = CustomUser.objects.filter(email=data.get("email"))
        if find_user.exists():
            return Response("Username already exists")

        user = CustomUser.objects.create(username=username, email=email)
        user.set_password(password)  # Method to hash the password
        user.save()
        return Response({"status": True})

    def get(self, request) -> None:
        """Get the email of starts with username"""
        username = request.GET.get("username")
        user = CustomUser.objects.filter(email__startswith=username)
        if user.exists():
            print(user)
        return Response({"message": "Retrived"})

    def delete(self, request) -> None:
        """Delete the user"""
        pk = int(request.GET.get("pk"))
        user = CustomUser.objects.filter(id=pk).first()
        # It is equivalent to user[0] but in advanced
        if user:
            user.delete()
            return Response({"message": "user has been deleted"})
        raise ValidationError({"error": "user does not exist"})

    def put(self, request) -> None:
        """Update the row"""
        pk = int(request.GET.get("pk"))
        user = CustomUser.objects.filter(id=pk).first()  # CustomUserObject
        data = request.data
        username = data.get("username", None)
        email = data.get("email", None)
        password = data.get("passworrd", None)
        if user:
            user.username = username
            user.email = email
            # user.update(username=username, email=email) #filter dont use first
            user.set_password(password)
            user.save()
            return Response({"message": "Modified the data successfully"})
        raise ValidationError({"error": "user doesnot exist"})
