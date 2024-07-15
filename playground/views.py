from django.core.mail import EmailMessage, BadHeaderError
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
import requests
import logging

logger = logging.getLogger(__name__)


class HelloView(APIView):
 
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('http://httpbin.org/delay/2')
            logger.info('Recceived the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')

        return render(request, 'hello.html', {'name': 'Sheryl'})


# def say_hello(request):
#     try:
#         message = BaseEmailMessage(
#             template_name='emails/hello.html',
#             context={'name': 'Sheryl'}
#         )
      
#         message.send(['john@sherylbuy.com'])
       
#     except BadHeaderError:
#         pass
#     return render(request, 'hello.html', {'name': 'Sheryl'})


