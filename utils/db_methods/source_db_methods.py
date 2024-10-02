from sqlalchemy import create_engine, inspect
from sqlalchemy.exc import SQLAlchemyError

def test_db_connection(username, password, host, port, database):
    # Create the SQLAlchemy engine
        connection_string = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"
        engine = create_engine(connection_string)

        try:
            # Test the connection
            with engine.connect() as connection:
                print("Connection successful!")
                
                # Use the inspector to get table names
                inspector = inspect(engine)
                table_names = inspector.get_table_names()
                print("Table names:", table_names)
                
                return table_names

        except SQLAlchemyError as e:
            print("Error occurred while connecting to the database:", str(e))
            raise e