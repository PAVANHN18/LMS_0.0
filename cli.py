# =====================================================
# CLI Frontend to interact with FastAPI backend
# =====================================================
import requests

BASE_URL = 'http://127.0.0.1:8000'  # Change to Render URL after deployment

def add_employee():
    name = input('Name: ')
    email = input('Email: ')
    dept = input('Department: ')
    joining_date = input('Joining Date (YYYY-MM-DD): ')
    payload = {'name': name,'email': email,'department': dept,'joining_date': joining_date}
    res = requests.post(f'{BASE_URL}/employees/', json=payload)
    print(res.json())

def apply_leave():
    emp_id = int(input('Employee ID: '))
    start_date = input('Start Date (YYYY-MM-DD): ')
    end_date = input('End Date (YYYY-MM-DD): ')
    reason = input('Reason: ')
    payload = {'employee_id': emp_id,'start_date': start_date,'end_date': end_date,'reason': reason}
    res = requests.post(f'{BASE_URL}/leave/', json=payload)
    print(res.json())

def approve_leave():
    leave_id = int(input('Leave Request ID: '))
    status = input('Status (Approved/Rejected): ')
    payload = {'status': status}
    res = requests.put(f'{BASE_URL}/leave/{leave_id}/approve', json=payload)
    print(res.json())

def get_leave_balance():
    emp_id = int(input('Employee ID: '))
    res = requests.get(f'{BASE_URL}/leave_balance/{emp_id}')
    print(res.json())

def menu():
    while True:
        print('\n=== Leave Management CLI ===')
        print('1. Add Employee')
        print('2. Apply Leave')
        print('3. Approve/Reject Leave')
        print('4. Check Leave Balance')
        print('5. Exit')
        choice = input('Enter choice: ').strip()
        if choice == '1':
            add_employee()
        elif choice == '2':
            apply_leave()
        elif choice == '3':
            approve_leave()
        elif choice == '4':
            get_leave_balance()
        elif choice == '5':
            break
        else:
            print('Invalid choice.')

if __name__ == '__main__':
    menu()
