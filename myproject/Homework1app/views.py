import logging
from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)

index_hw1 = """
    <h1>Это главная страница.</h1>
"""
about_hw1 = """
    <h1>Это страница обо мне.</h1>
"""


# Create your views here.
def main(request):
    logger.info('Main page accessed')
    return HttpResponse(index_hw1)


def about(request):
    try:
        # some code that might raise an exception
        result = 1 / 1
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Oops, something went wrong.")
    else:
        logger.debug('About page accessed')
        return HttpResponse(about_hw1)
