
import json

from .BaseHander import BaseHandler,RequestHandler


class IndexHandler(BaseHandler):

    def get(self):
        t_dict = {
            'name':'user',
            'password':'123456'
        }
        self.write(t_dict)