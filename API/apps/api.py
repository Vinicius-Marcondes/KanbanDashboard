from flask_restful import Api, Resource


class Index(Resource):

    # Defines the get method
    def get(self):
        return {'hello': 'world by apps'}


api = Api()


def configure_api(app):
    api.add_resource(Index, '/')
    api.init_app(app)
