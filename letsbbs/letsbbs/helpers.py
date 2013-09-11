def register_blueprint(app):
    from .views import account, frontend

    app.register_blueprint(account, url_prefix='/account')
    # put this in the end 
    app.register_blueprint(frontend, url_prefix='')