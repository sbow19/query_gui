from models.dbs.dbs import SavedDatabases
from models.session.session import session

class SavedDatabasesMethods():
    def __init__():
        pass

    @staticmethod
    def does_database_exist() -> bool:
        
        results = session.query(SavedDatabases).all()
        
        print(results)
        
        # If rows in db, then return true
        if len(results) > 0:
            return True
        
        return False

    
