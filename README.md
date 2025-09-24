# Backend API - Project Management Tool

FastAPI-based backend for the Project Management Tool with PostgreSQL, JWT authentication, and AI integration.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- PostgreSQL 15+
- pip

### Installation

1. **Clone and navigate to backend**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

5. **Set up database**
   ```bash
   createdb project_management
   ```

6. **Run the server**
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at http://localhost:8000

## 📚 API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Testing

```bash
pytest
```

## 🏗️ Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration settings
│   ├── database.py          # Database connection
│   ├── models/              # SQLAlchemy models
│   │   ├── user.py
│   │   ├── project.py
│   │   └── task.py
│   ├── routes/              # API routes
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── projects.py
│   │   ├── tasks.py
│   │   └── ai.py
│   ├── schemas/             # Pydantic schemas
│   │   ├── user_schema.py
│   │   ├── project_schema.py
│   │   └── task_schema.py
│   ├── services/            # Business logic
│   │   ├── auth_service.py
│   │   └── ai_service.py
│   └── utils/               # Utilities
│       ├── security.py
│       └── exceptions.py
├── tests/                   # Test files
├── requirements.txt         # Python dependencies
└── README.md
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://postgres:password@localhost:5432/project_management` |
| `SECRET_KEY` | JWT secret key | `your-secret-key-change-in-production` |
| `ALGORITHM` | JWT algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time | `30` |
| `ALLOWED_ORIGINS` | CORS allowed origins | `["http://localhost:3000"]` |
| `OPENAI_API_KEY` | OpenAI API key (optional) | - |
| `GROQ_API_KEY` | GROQ API key (optional) | - |

## 🔐 Authentication

The API uses JWT-based authentication with role-based access control.

### User Roles
- **Admin**: Full system access
- **Project Manager**: Can manage projects and tasks
- **Developer**: Can update assigned tasks

### Authentication Flow
1. Register/Login to get JWT token
2. Include token in Authorization header: `Bearer <token>`
3. Token expires after configured time

## 🗄️ Database Models

### Users
- User accounts with roles and authentication
- Password hashing with bcrypt

### Projects
- Project information and status tracking
- Owner relationship with users
- Member management

### Tasks
- Task management with assignments
- Status workflow (todo → in_progress → done)
- Priority levels and deadlines

### Comments
- Task comments for collaboration
- User attribution and timestamps

## 🤖 AI Integration

### User Story Generation
- Generate user stories from project descriptions
- Uses GROQ API for fast responses
- Configurable number of stories

### Task Generation
- Create tasks from user stories
- Automatic priority assignment
- Time estimation

## 🧪 Testing

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_auth.py
```

### Test Structure
- **conftest.py**: Test fixtures and configuration
- **test_auth.py**: Authentication tests
- **test_projects.py**: Project management tests
- **test_tasks.py**: Task management tests
- **test_ai.py**: AI feature tests

## 🚀 Deployment

### Docker
```bash
docker build -t project-management-backend .
docker run -p 8000:8000 project-management-backend
```

### Production Considerations
- Use environment-specific configuration
- Set strong SECRET_KEY
- Configure proper CORS origins
- Use production database
- Enable SSL/HTTPS
- Set up monitoring and logging

## 📊 API Endpoints

### Authentication
- `POST /api/auth/register` - Register user
- `POST /api/auth/login` - Login
- `GET /api/auth/me` - Get current user

### Users
- `GET /api/users/` - List users (Admin)
- `GET /api/users/{id}` - Get user
- `PUT /api/users/{id}` - Update user
- `DELETE /api/users/{id}` - Delete user (Admin)

### Projects
- `GET /api/projects/` - List projects
- `POST /api/projects/` - Create project
- `GET /api/projects/{id}` - Get project
- `PUT /api/projects/{id}` - Update project
- `DELETE /api/projects/{id}` - Delete project
- `POST /api/projects/{id}/members` - Add member
- `GET /api/projects/{id}/members` - Get members

### Tasks
- `GET /api/tasks/` - List tasks
- `POST /api/tasks/` - Create task
- `GET /api/tasks/{id}` - Get task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task
- `POST /api/tasks/{id}/comments` - Add comment
- `GET /api/tasks/{id}/comments` - Get comments
- `GET /api/tasks/dashboard/stats` - Dashboard stats

### AI Features
- `POST /api/ai/generate-user-stories` - Generate stories
- `POST /api/ai/generate-tasks` - Generate tasks

## 🔍 Error Handling

The API returns appropriate HTTP status codes and error messages:

- `200`: Success
- `201`: Created
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `422`: Validation Error
- `500`: Internal Server Error

## 📈 Performance

- Database connection pooling
- Efficient queries with SQLAlchemy
- JWT token caching
- Pagination for large datasets
- Optimized AI API calls

## 🛡️ Security

- JWT authentication
- Password hashing with bcrypt
- Role-based access control
- Input validation with Pydantic
- SQL injection prevention
- CORS protection
- Environment variable security

## 🔧 Development

### Code Style
- Follow PEP 8
- Use type hints
- Document functions and classes
- Write comprehensive tests

### Adding New Features
1. Create model in `models/`
2. Add schema in `schemas/`
3. Implement service logic in `services/`
4. Create routes in `routes/`
5. Add tests in `tests/`
6. Update documentation

## 📝 License

MIT License - see main README for details.
