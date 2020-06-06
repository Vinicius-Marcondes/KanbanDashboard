# Third
from flask_restful import Api, Resource

# Apps
from apps.users.resources import SignUp
from apps.users.resources_admin import AdminUserPageList


class Index(Resource):

    # Defines the get method
    def get(self):
        return {'hello': 'world by apps'}


api = Api()


def configure_api(app):
    api.add_resource(Index, '/')
    api.add_resource(SignUp, '/signup/api/users')
    api.add_resource(AdminUserPageList, '/admin/api/users/<int:page_id>')

    api.init_app(app)
