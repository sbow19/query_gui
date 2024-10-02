from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped 
from models.base.base import mapper_registry


# Define the SavedDatabases model
@mapper_registry.mapped
class TablesDatabase:
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True, autoincrement=True)
    table_name = Column(String, nullable=False)
    db_id = Column(Integer, ForeignKey('saved_databases.id'))
    
    # Relatinoship
    saved_databases = relationship("SavedDatabases", back_populates="table_database")
    