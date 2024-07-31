Select Employees.name, EmployeeUNI.unique_id
From Employees Left JOIN EmployeeUNI On Employees.id = EmployeeUNI.id;