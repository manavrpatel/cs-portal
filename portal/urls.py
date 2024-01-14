from django.contrib import admin
from django.urls import path
from users.views import UserCreateView, LoginView
from customer_support.views.tickets import TicketCreateAPI, TicketDetailsAPI, TicketUpdateAPI
from customer_support.views.messages import MessageCreateAPI, MessagesGetAPI
from customer_support.views.portal import portal, home
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', LoginView, name='login'),
    path('admin/', admin.site.urls),
    path('users/', UserCreateView.as_view(), name="users"),
    path('tickets/create-ticket', TicketCreateAPI.as_view(), name="create-tickets"),
    path('tickets/update-ticket/<uuid:pk>', TicketUpdateAPI.as_view(), name="update-ticket"),
    path('tickets/get-ticket/<uuid:pk>', TicketDetailsAPI.as_view(), name="ticket-details"),
    path('messages/', MessageCreateAPI.as_view(), name="create-messages"),
    path('get-messages/', MessagesGetAPI.as_view(), name="get-messages"),
    path('login/', LoginView, name='login'),
    path('home/', home, name='home'),
    path('portal/<uuid:ticket_id>/', portal, name='portal')
]

