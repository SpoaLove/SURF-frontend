from flask import Flask

app = Flask(__name__)



if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
elif app.config['ENV'] == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.DevelopmentConfig')
    
print(f' * Flask ENV is set to {app.config["ENV"]}')   

from app import views
