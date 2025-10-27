###This class is used to create tables automatically#########

from app.db.session import engine
from app.db.base import Base
from app.model import personDetails  # import your model

def init_db():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
