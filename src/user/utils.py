# from django.conf import settings
# from django.core.exceptions import ValidationError
# import requests
# import re


# MESSAGE_RP="GSA tizimining parolini tiklash kodi: "
# MESSAGE_SC="GSA tizimiga kirish codi: "
# pattern = r'^(\+?998)?([. \-])?((\d){2})([. \-])?(\d){3}([. \-])?(\d){2}([. \-])?(\d){2}$'


# def validate_phone_number(value):
#     if not re.match(pattern, value):
#         return ValidationError("%(value) does not follow phone number pattern ", params={"value": value})


# def generate_correct_number(phone_num):
#     if len(phone_num) > 12:
#         if len(phone_num.split()) == 1:
#             return phone_num if len(phone_num) > 9 else '+9989'+phone_num
#         else:
#             c_ph_n = ''.join([c for c in phone_num if c.isdigit()])
#             return '+9989' + c_ph_n
#     else:
#         c_ph_n=''.join([c for c in phone_num if c.isdigit()])
#         return c_ph_n

# def is_phone_number_valid(phone_number):
#     if not phone_number:
#         return False,"Please enter a valid phone number"
#     if not re.match(pattern, phone_number):
#         return False,"Please make sure phone number is correct"
#     return True,phone_number


# def send_code_phone_number(phone_number,code,reset=False):

#     if reset:
#         msg = '{}{}'.format(MESSAGE_RP,code)
#     else:
#         msg = '{}{}'.format(MESSAGE_SC,code)
#         payload = get_message_payload(phone_number,msg)
#         headers = get_header()
#         res = requests.post(settings.ESKIZ_SMS_SEND_URL,json=payload,headers=headers)
#         return res    