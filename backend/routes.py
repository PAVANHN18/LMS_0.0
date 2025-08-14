# =====================================================
# FastAPI Routes for Leave Management System
# =====================================================
from fastapi import APIRouter, HTTPException
from db.database import SessionLocal, engine, Base
from db.models import Employee, LeaveRequest
from backend.schemas import EmployeeCreate, LeaveRequestCreate, LeaveApproveRequest
from datetime import date

router = APIRouter()

# Auto-create tables on startup
Base.metadata.create_all(bind=engine)

# -----------------------------
# Add Employee Endpoint
# -----------------------------
@router.post('/employees/')
def add_employee(emp: EmployeeCreate):
    db = SessionLocal()
    existing = db.query(Employee).filter(Employee.email == emp.email).first()
    if existing:
        raise HTTPException(status_code=400, detail='Email already exists')
    new_emp = Employee(**emp.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return {'message':'Employee added', 'employee_id': new_emp.id}

# -----------------------------
# Apply Leave Endpoint
# -----------------------------
@router.post('/leave/')
def apply_leave(leave: LeaveRequestCreate):
    db = SessionLocal()
    emp = db.query(Employee).filter(Employee.id == leave.employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail='Employee not found')
    leave_days = (leave.end_date - leave.start_date).days + 1
    if leave_days > emp.leave_balance:
        raise HTTPException(status_code=400, detail='Insufficient leave balance')
    # Overlap check
    overlapping = db.query(LeaveRequest).filter(
        LeaveRequest.employee_id==leave.employee_id,
        LeaveRequest.status.in_(["Pending","Approved"]),
        LeaveRequest.start_date <= leave.end_date,
        LeaveRequest.end_date >= leave.start_date
    ).first()
    if overlapping:
        raise HTTPException(status_code=400, detail='Overlapping leave exists')
    new_leave = LeaveRequest(**leave.dict())
    db.add(new_leave)
    db.commit()
    db.refresh(new_leave)
    return {'message':'Leave requested', 'leave_id': new_leave.id}

# -----------------------------
# Approve / Reject Leave Endpoint
# -----------------------------
@router.put('/leave/{leave_id}/approve')
def approve_leave(leave_id: int, status_req: LeaveApproveRequest):
    db = SessionLocal()
    leave = db.query(LeaveRequest).filter(LeaveRequest.id==leave_id).first()
    if not leave:
        raise HTTPException(status_code=404, detail='Leave request not found')
    if leave.status != 'Pending':
        raise HTTPException(status_code=400, detail='Leave already processed')
    if status_req.status == 'Approved':
        emp = leave.employee
        leave_days = (leave.end_date - leave.start_date).days + 1
        if leave_days > emp.leave_balance:
            raise HTTPException(status_code=400, detail='Insufficient leave balance')
        emp.leave_balance -= leave_days
    leave.status = status_req.status
    db.commit()
    return {'message': f'Leave {status_req.status.lower()}'}

# -----------------------------
# Get Leave Balance Endpoint
# -----------------------------
@router.get('/leave_balance/{employee_id}')
def get_leave_balance(employee_id: int):
    db = SessionLocal()
    emp = db.query(Employee).filter(Employee.id==employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail='Employee not found')
    return {'employee': emp.name, 'leave_balance': emp.leave_balance}
