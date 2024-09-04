import models
import db

if __name__ == "__main__":
    con = db.engine.connect()
    models.Model.metadata.create_all(con)

