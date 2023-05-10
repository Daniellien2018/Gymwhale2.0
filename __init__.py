from flask import Flask,render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
import logging
import os
from dotenv import load_dotenv



load_dotenv()
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # #Oauth google plus API
    # client_id = os.getenv('GOOGLE_CLIENT_ID')
    # client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
    # app.secret_key = os.getenv('secret_key')

    # #accounts for google changing the requested OAuth scope
    # os.environ['OAUTHLIB_INSECRE_TRANSPORT']='1'
    # os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE']='1'

    # blueprint = make_google_blueprint(
    #     client_id=client_id,
    #     client_secret=client_secret,
    #     reprompt_consent=True,
    #     scope=["profile", "email"]
    # )
    # app.register_blueprint(blueprint, url_prefix="/login")

    @app.route('/hello')
    def hello():
        return "hello world"
    
    # @app.route("/")
    # def index():  
    #     google_data = None
    #     user_info_endpoint = '/oauth2/v2/userinfo'
    #     if google.authorized:
    #         google_data = google.get(user_info_endpoint).json()

    #     return render_template('index.j2',
    #                         google_data=google_data,
    #                         fetch_url=google.base_url + user_info_endpoint)

    # @app.route('/login')
    # def login():
    #     return redirect(url_for('google.login'))

    # @app.route("/signup/")
    # def signup():
    #     return "<p>This is the Signup page</p>"

    # if __name__ == "__main__":
    #     app.run()
    
    from . import db
    db.init_app(app)
    
    return app
