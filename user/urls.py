from django.urls import path

from user.resources.views_user import CreateUserView, ManageUserView
from user.resources.views_auth import CreateTokenView

app_name = 'user'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('me/', ManageUserView.as_view(), name='me'),
]