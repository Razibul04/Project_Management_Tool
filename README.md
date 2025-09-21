# Project Management Tool

A comprehensive web-based project management tool built with FastAPI, React, PostgreSQL, and AI integration.

## 🚀 Features

### Core Features
- **User Management**: Role-based access control (Admin, Project Manager, Developer)
- **Project Management**: Create, update, and track projects with team members
- **Task Management**: Kanban-style task board with status tracking
- **Comments System**: Add comments to tasks for collaboration
- **Dashboard**: Real-time metrics and project progress visualization
- **JWT Authentication**: Secure login and role-based permissions

### AI Features (Bonus)
- **User Story Generator**: AI-powered generation of user stories from project descriptions
- **Task Generation**: Automatically create tasks from user stories
- **GROQ Integration**: Fast AI responses using GROQ API

## 🏗️ Architecture

### Backend (FastAPI)
- **Framework**: FastAPI with Python 3.11+
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT with role-based access control
- **API Documentation**: Auto-generated Swagger/OpenAPI docs
- **Testing**: Comprehensive unit tests with pytest

### Frontend (React)
- **Framework**: React 18 with Material-UI
- **State Management**: Context API for authentication
- **Routing**: React Router for navigation
- **Charts**: Recharts for data visualization
- **Responsive Design**: Mobile-friendly interface

### Database Schema
- **Users**: User accounts with roles and authentication
- **Projects**: Project information and status tracking
- **Tasks**: Task management with assignments and deadlines
- **Comments**: Task comments for collaboration
- **Project Members**: Many-to-many relationship for team management

## 📋 Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 15+
- Docker & Docker Compose (optional)

## 🛠️ Installation & Setup

### Option 1: Docker Compose (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd project-management-tool
   ```

2. **Set up environment variables**
   ```bash
   cp backend/env.example backend/.env
   # Edit backend/.env with your configuration
   ```

3. **Start the application**
   ```bash
   docker-compose up -d
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Option 2: Manual Setup

#### Backend Setup

1. **Navigate to backend directory**
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
   # Edit .env with your database and API keys
   ```

5. **Set up PostgreSQL database**
   ```bash
   createdb project_management
   ```

6. **Run the backend**
   ```bash
   uvicorn app.main:app --reload
   ```

#### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the backend directory:

```env
# Database
DATABASE_URL=postgresql://postgres:password@localhost:5432/project_management

# JWT
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
ALLOWED_ORIGINS=["http://localhost:3000", "http://127.0.0.1:3000"]

# AI Services (Optional)
OPENAI_API_KEY=your-openai-api-key
GROQ_API_KEY=your-groq-api-key
```

### AI Integration Setup

1. **Get API Keys**
   - [GROQ API Key](https://console.groq.com/keys)
   - [OpenAI API Key](https://platform.openai.com/api-keys) (optional)

2. **Add to environment variables**
   ```env
   GROQ_API_KEY=your-groq-api-key
   OPENAI_API_KEY=your-openai-api-key
   ```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 📚 API Documentation

### Interactive Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Postman Collection
Import the collection from `docs/Postman-collection.json` for easy API testing.

### Key Endpoints

#### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login and get token
- `GET /api/auth/me` - Get current user info

#### Projects
- `GET /api/projects/` - List projects
- `POST /api/projects/` - Create project
- `GET /api/projects/{id}` - Get project details
- `PUT /api/projects/{id}` - Update project
- `DELETE /api/projects/{id}` - Delete project

#### Tasks
- `GET /api/tasks/` - List tasks
- `POST /api/tasks/` - Create task
- `GET /api/tasks/{id}` - Get task details
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task

#### AI Features
- `POST /api/ai/generate-user-stories` - Generate user stories
- `POST /api/ai/generate-tasks` - Generate tasks from stories

## 👥 User Roles

### Admin
- Full system access
- Manage all users, projects, and tasks
- Access to AI features

### Project Manager
- Create and manage projects
- Assign tasks to team members
- Access to AI features
- View all project data

### Developer
- View assigned tasks
- Update task status and add comments
- Limited project access

## 🎯 Usage Guide

### Getting Started

1. **Register an account** or use the default admin account:
   - Email: `admin@example.com`
   - Password: `password123`

2. **Create a project**
   - Navigate to Projects page
   - Click "New Project"
   - Fill in project details

3. **Add team members**
   - Go to project details
   - Add members with appropriate roles

4. **Create tasks**
   - Navigate to Tasks page
   - Create tasks and assign to team members

5. **Track progress**
   - Use the Dashboard for overview
   - Update task status as work progresses

### AI Features

1. **Generate User Stories**
   - Go to a project
   - Use AI to generate user stories from project description

2. **Create Tasks from Stories**
   - Select generated user stories
   - Use AI to create specific development tasks

## 🚀 Deployment

### Production Deployment

1. **Update environment variables**
   ```env
   SECRET_KEY=your-production-secret-key
   DATABASE_URL=your-production-database-url
   ALLOWED_ORIGINS=["https://yourdomain.com"]
   ```

2. **Build and deploy**
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

### Environment-specific Configurations

- **Development**: Hot reload enabled, debug mode
- **Production**: Optimized builds, security headers, SSL

## 🔒 Security Features

- JWT-based authentication
- Role-based access control
- Password hashing with bcrypt
- CORS protection
- Input validation and sanitization
- SQL injection prevention with SQLAlchemy

## 📊 Monitoring & Logging

- Health check endpoints
- Structured logging
- Error tracking
- Performance monitoring

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🆘 Support

For support and questions:
- Check the API documentation at `/docs`
- Review the test cases for usage examples
- Open an issue for bugs or feature requests

## 🔮 Future Enhancements

- Real-time notifications
- File attachments for tasks
- Time tracking
- Advanced reporting and analytics
- Mobile app
- Integration with external tools (Slack, GitHub, etc.)
- Advanced AI features (automated task prioritization, project risk assessment)

## 📈 Performance Considerations

- Database indexing for large datasets
- Caching for frequently accessed data
- Pagination for large lists
- Optimized queries with SQLAlchemy
- Frontend code splitting and lazy loading

---

**Built with ❤️ using FastAPI, React, and modern web technologies.**
