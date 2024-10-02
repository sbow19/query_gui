from models.base.base import Base
from models.engine.engine import engine
from models.session.session import session
from models.tables.tables import TablesDatabase
from models.dbs.dbs import SavedDatabases
from models.projects.projects import ProjectsDatabase




def init_db():
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
                