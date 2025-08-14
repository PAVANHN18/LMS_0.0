
# Leave Management System (LMS)

A simple Leave Management System built with **FastAPI** for backend and PostgreSQL as the database.  
The system allows employees to apply for leave, check leave balance, and allows managers to approve/reject leave requests.

## Features
- Add new employees with details
- Apply for leave with start/end date and reason
- Approve or reject leave requests
- Check remaining leave balance for employees
- REST API built with FastAPI
- PostgreSQL database integration

## Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Hosting:** Render

## API Endpoints

### Employee Management
- **POST** `/employees/` – Add new employee
- **GET** `/employees/{employee_id}` – Get employee details

### Leave Management
- **POST** `/leave/` – Apply for leave
- **PUT** `/leave/{leave_id}/approve` – Approve/Reject leave
- **GET** `/leave_balance/{employee_id}` – Get leave balance

## Database Schema (Simplified)
- **Employee**
  - id (Primary Key)
  - name
  - email
  - department
  - joining_date

- **Leave**
  - id (Primary Key)
  - employee_id (Foreign Key → Employee.id)
  - start_date
  - end_date
  - reason
  - status


## Future Enhancements
- User authentication & role-based access
- Email notifications for leave approval/rejection
- Caching frequently accessed data using Redis
- Deploy backend on Kubernetes for scalability

##Access link for FastAPI
- public hosted on render both backend and DB
- https://lms-0-0.onrender.com/docs 
---
**Author:** Pavan H N
