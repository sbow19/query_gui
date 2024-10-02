from sqlalchemy import Column, Integer, String
from models.base.base import mapper_registry

# Define the SavedDatabases model
@mapper_registry.mapped
class ProjectsDatabase:
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String, nullable=False)
    
    