from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum

class Role(Enum):
    customer="CUSTOMER"
    agent="AGENT"

class User(AbstractUser):
    USER_ROLES = [
        (Role.customer.value, 'CUSTOMER'),
        (Role.agent.value, 'AGENT'),
    ]

    userID = models.UUIDField(primary_key=True, default=uuid4)
    username = models.TextField(max_length=50, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=20, choices=USER_ROLES)
