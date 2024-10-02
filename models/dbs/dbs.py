from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base.base import mapper_registry

# Define the SavedDatabases model
@mapper_registry.mapped
class SavedDatabases:
    __tablename__ = 'saved_databases'

    id = Column(Integer, primary_key=True, autoincrement=True)
    database_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    # Relatioship
    table_database = relationship("TablesDatabase", back_populates="saved_databases", cascade="all, delete-orphan")