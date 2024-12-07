import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError, SQLAlchemyError

def test_connection():
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'ssarticlecms3.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'dbArticleCMS3'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin3'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'F@ncyP@ssw0rd3'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    """
    Test the connection to the Azure SQL Database.
    """
    print("Attempting to connect to the database...")
    
    # Create the SQLAlchemy engine
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    
    try:
        # Connect to the database
        with engine.connect() as connection:
            print("Successfully connected to the database!")
            
            # Execute a simple query to verify the connection
            print("Executing test query...")
            result = connection.execute(text("SELECT TOP 1 * FROM INFORMATION_SCHEMA.TABLES"))
            
            # Fetch and display results
            rows = result.fetchall()
            if rows:
                print("Query executed successfully. Tables in the database:")
                for row in rows:
                    print(row)
            else:
                print("No tables found in the database.")
    
    except OperationalError as e:
        print("OperationalError: Unable to connect to the database.")
        print(f"Details: {e}")
    except SQLAlchemyError as e:
        print("SQLAlchemyError: A database error occurred.")
        print(f"Details: {e}")
    except Exception as e:
        print("An unexpected error occurred.")
        print(f"Details: {e}")
    finally:
        # Dispose of the engine
        engine.dispose()
        print("Database connection test completed.")

if __name__ == "__main__":
    test_connection()
