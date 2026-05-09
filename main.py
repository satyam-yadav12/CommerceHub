from app import Create_app
from app.extensions import db
from app import models

service = Create_app()

with service.app_context():
    db.create_all()
    print("database initialized")
if __name__ == "__main__":

    service.run()
