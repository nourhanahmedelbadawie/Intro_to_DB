import mysql.connector
from mysql.connector import Error

def create_database():
    """Create the 'alx_book_store' database if it does not exist."""
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="nourhan",  # Replace with your MySQL username
            password="121199"  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error as e:
        # Handle MySQL-specific errors
        print(f"Error: {e}")
    
    finally:
        # Close the connection and cursor if they are open
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

# Execute the function
if __name__ == "__main__":
    create_database()
