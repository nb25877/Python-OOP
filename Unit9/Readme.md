# ShopEase E-commerce System

A scalable, modular e-commerce system built with FastAPI, SQLAlchemy, and PostgreSQL.

## Project Structure

```
Unit9/
├── .env                 # Environment configuration
├── requirements.txt     # Project dependencies
└── src/
    ├── business/       # Business logic layer
    │   ├── notification_service.py
    │   ├── order_processing.py
    │   ├── product_catalog.py
    │   └── user_management.py
    ├── data/          # Data access layer
    │   └── database.py
    ├── presentation/  # API endpoints
    │   └── api_endpoints.py
    └── security/      # Authentication & security
        └── authentication.py
```

## Architecture

### Layered Architecture
1. **Presentation Layer**
   - REST API endpoints using FastAPI
   - Request/Response models using Pydantic
   - Dependency injection for services

2. **Business Logic Layer**
   - User management
   - Order processing
   - Product catalog
   - Notification system

3. **Data Access Layer**
   - SQLAlchemy ORM
   - PostgreSQL database
   - Model relationships

### Key Features
- JWT-based authentication
- Modular service architecture
- Strategy pattern for notifications
- Repository pattern for data access
- Dependency injection
- Type hints throughout

## Setup & Installation

1. **Create Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure PostgreSQL**
```bash
createdb shopease
```

4. **Environment Configuration**
Create `.env` file:
```
DATABASE_URL=postgresql://localhost/shopease
JWT_SECRET_KEY=your-secret-key-here
```

5. **Run Application**
```bash
cd src
python main.py
```

## API Endpoints

### Authentication
- `POST /auth/login`: User login
```json
{
    "username": "string",
    "password": "string"
}
```

### Products
- `GET /products/search`: Search products
```
?query=string
```

### Orders
- `POST /orders/create`: Create new order
```json
{
    "user_id": "integer",
    "items": [
        {
            "product_id": "integer",
            "quantity": "integer"
        }
    ]
}
```

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Code Quality
```bash
black src/
flake8 src/
mypy src/
```

## Requirements
- Python 3.x
- PostgreSQL
- Dependencies listed in requirements.txt

## Design Patterns Used

1. **Repository Pattern**
   - Abstracts data access
   - Enables switching data sources

2. **Strategy Pattern**
   - Used in notification system
   - Supports multiple notification methods

3. **Dependency Injection**
   - Loose coupling between components
   - Easier testing and maintenance

## Security Features
- Password hashing
- JWT authentication
- Database connection pooling
- Input validation
- Error handling

## Contributing
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License
MIT License