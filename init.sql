-- Initialize the database with some sample data
-- This script runs when the PostgreSQL container starts for the first time

-- Create extensions if needed
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- The tables will be created by SQLAlchemy, but we can add some initial data here
-- Note: This is optional and mainly for development/testing purposes

-- Insert sample users (passwords are hashed versions of 'password123')
INSERT INTO users (name, email, hashed_password, role, created_at) VALUES
('Admin User', 'admin@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/8KqKqKq', 'admin', NOW()),
('Project Manager', 'pm@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/8KqKqKq', 'project_manager', NOW()),
('Developer 1', 'dev1@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/8KqKqKq', 'developer', NOW()),
('Developer 2', 'dev2@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/8KqKqKq', 'developer', NOW())
ON CONFLICT (email) DO NOTHING;
