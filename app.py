from flask import Flask
from flask_graphql import GraphQLView
from flask_graphql_auth import (
    AuthInfoField,
    GraphQLAuth,
    get_jwt_identity,
    get_raw_jwt,
    create_access_token,
    create_refresh_token,
    query_jwt_required,
    mutation_jwt_refresh_token_required,
    mutation_jwt_required,
)

from database.db_session import db_session
from schema.schema import schema

app = Flask(__name__)
app.debug = True
auth = GraphQLAuth(app)

app.config["JWT_SECRET_KEY"] = "something"  # change this!
app.config["REFRESH_EXP_LENGTH"] = 30
app.config["ACCESS_EXP_LENGTH"] = 10

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()