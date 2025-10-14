import uvicorn
from dotenv import load_dotenv
import os
from src.data.database import init_db
from src.presentation.api_endpoints import app

load_dotenv()

def main():
    # Initialize database
    database_url = os.getenv("DATABASE_URL")
    SessionLocal = init_db(database_url)
    
    # Run application
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()