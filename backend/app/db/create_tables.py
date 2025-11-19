from app.db.session import engine, Base
from app.models import user, task, project

Base.metadata.create_all(bind=engine)
