
import os

from handlers.UserProfile import IndexHandler
from handlers.BaseHander import StaticFileHandler

urlpatterns = [
    (r'/', IndexHandler),
    (r'/(.*)', StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'html')}),
]