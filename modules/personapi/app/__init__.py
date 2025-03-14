from flask import Flask

def create_app(config_filename=None):
    app = Flask(__name__)
    
    # Load config from a file (optional)
    if config_filename:
        app.config.from_pyfile(config_filename)
    else:
        app.config.from_mapping(
            SECRET_KEY='mysecretkey',
            DATABASE='app.db'
        )

    # Import and register blueprints
    from .routes import main
    from .controllers import api
    app.register_blueprint(main, url_prefix='/api') 
    

    return app