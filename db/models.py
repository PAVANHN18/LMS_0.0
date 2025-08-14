# =====================================================
# SQLAlchemy Models: Employee and LeaveRequest
# =====================================================
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Employee table
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    department = Column(String(50), nullable=False)
    joining_date = Column(Date, nullable=False)
    leave_balance = Column(Integer, default=20)
    leaves = relationship('LeaveRequest', back_populates='employee')

# LeaveRequest table
class LeaveRequest(Base):
    __tablename__ = 'leave_requests'
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    reason = Column(String(255), nullable=False)
    status = Column(Enum('Pending','Approved','Rejected', name='leave_status'), default='Pending')
    employee = relationship('Employee', back_populates='leaves')
