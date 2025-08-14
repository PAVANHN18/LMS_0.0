# =====================================================
# Pydantic Schemas for request and response validation
# =====================================================
from pydantic import BaseModel
from datetime import date

# Employee create schema
class EmployeeCreate(BaseModel):
    name: str
    email: str
    department: str
    joining_date: date

# Leave request schema
class LeaveRequestCreate(BaseModel):
    employee_id: int
    start_date: date
    end_date: date
    reason: str

# Leave approve/reject schema
class LeaveApproveRequest(BaseModel):
    status: str  # Must be 'Approved' or 'Rejected'
