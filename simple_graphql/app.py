from flask import Flask
from flask_graphql import GraphQLView
from models.model import db_session
from schemas.schema import Department, schema


def create_app(config='settings'):
    app = Flask(__name__, static_folder=None)
    # app.config.from_object(config)
    # app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
    # # 這行從 settings 設定好像不會起作用，但這樣設定則可以
    # app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}
    # app.config['JWT_SECRET_KEY'] = app.config['SECRET_KEY']
    # app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=20160)
    # app.config["SESSION_COOKIE_HTTPONLY"] = False
    # register_extensions(app)
    # cli_init(app)

    return app
    # with app.app_context():
    #     from command_line import commands
    #     return app


app = create_app()

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    ))


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()