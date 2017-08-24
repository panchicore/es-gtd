import os

ES_HOST = os.environ.get("ES_GTD_HOST")
ES_USER = os.environ.get("ES_GTD_USER")
ES_PASSWORD = os.environ.get("ES_GTD_PASSWORD")
ES_INDEX = os.environ.get("ES_GTD_INDEX")
URL = ES_HOST + ES_INDEX
INDEX_URL = URL + "/event/"
