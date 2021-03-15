
from django.core.exceptions import ValidationError
from django.conf import settings
# import requests
import re



def is_email_valid(email):
    if not email:
        return False,"Please provide a valid email address"
    if not re.match(email):
        return False,"Please make sure email is valid"
    return True,email        