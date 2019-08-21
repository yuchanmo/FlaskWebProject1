##"""
##This script runs the application using a development server.
##It contains the definition of routes and views for the application.
##"""

##from flask import Flask
##app = Flask(__name__)

### Make the WSGI interface available at the top level so wfastcgi can get it.
##wsgi_app = app.wsgi_app


##@app.route('/')
##def hello():
##    """Renders a sample page."""
##    return "Hello World!"

##if __name__ == '__main__':
##    import os
##    HOST = os.environ.get('SERVER_HOST', 'localhost')
##    try:
##        PORT = int(os.environ.get('SERVER_PORT', '5555'))
##    except ValueError:
##        PORT = 5555
##    app.run(HOST, PORT)


#import os
#from flask import Flask

#def create_app(test_config=None):
#    app = Flask(__name__,instance_relative_config=True)
#    app.config.from_mapping(
#        SECRET_KEY='dev',
#        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#    )

#    if test_config is None:
#        # load the instance config, if it exists, when not testing
#        app.config.from_pyfile('config.py', silent=True)
#    else:
#        # load the test config if passed in
#        app.config.from_mapping(test_config)

#    # ensure the instance folder exists
#    try:
#        os.makedirs(app.instance_path)
#    except OSError:
#        pass


#    @app.route('/hello')
#    def hello():
#        return "Hello, world!"

#    return app

