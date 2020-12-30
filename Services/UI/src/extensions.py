## IMPORT FLASK MODULES
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

## INITIALIZE PLUGGINS
db = SQLAlchemy()
migrate = Migrate()