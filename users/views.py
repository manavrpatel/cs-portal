from rest_framework import generics,status
from django import forms
from rest_framework.response import Response
from users.serializers import UserCreateSerializer
from django.shortcuts import render, redirect


class UserForm(forms.Form):
    username = forms.CharField(max_length=255)

# Create your views here.
class UserCreateView(generics.GenericAPIView):
    serializer_class=UserCreateSerializer

    def post(self, request):
        user=request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)
    
def LoginView(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            response = redirect('home')
            response.set_cookie('username', username)
            return response
    else:
        form = UserForm()
    return render(request, 'customer_support/login.html', {'form': form})
    
    