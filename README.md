# Courier Service Management

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://couriar-service-management.onrender.com/)

A modern courier service management system backend built with Django REST Framework. Features JWT authentication, role-based access control, and cloud deployment ready.

## Table of Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Deployment](#deployment)
- [Usage](#usage)

- [Contributing](#contributing)
- [License](#license)

## Features
- **Core Functionality**
  - Package tracking with real-time status updates
  - Delivery management system (Pending/In Transit/Delivered)
  
- **Security**
  - JWT Authentication (Access & Refresh tokens)
  - Role-based permissions (Admin,regular user )
  - HasObjectPermission checks for sensitive operations
- **Data Management**
  - Soft delete functionality with data preservation
  - PostgreSQL database support
- **API Features**
  - RESTful endpoints using DRF Viewsets and Generics
  - Detailed permission classes for CRUD operations
  - Browsable API interface

## Technology Stack
- **Backend**: Python 3.11+, Django 4.2
- **API**: Django REST Framework 3.14
- **Database**: PostgreSQL (Production,Development)
- **Authentication**: djangorestframework-simplejwt 5.2
- **Deployment**: Render, Gunicorn 

## Installation
### Local Development
```bash
# Clone repository
git clone https://github.com/TheReinforce43/Couriar_Service_management.git
cd Couriar_Service_management

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env file with your settings

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver



### Local Development


# Start server
gunicorn courier_service_backend.wsgi:application


