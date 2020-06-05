# Third
from flask_restful import Api, Resource

# Apps
from apps.users.resources import SingUp


class Index(Resource):

    # Defines the get method
    def get(self):
        return {'hello': 'world by apps'}


api = Api()


def configure_api(app):
    api.add_resource(Index, '/')
    api.add_resource(SingUp, '/users')

    api.init_app(app)
