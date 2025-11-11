import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    rs = employee.groupby('departmentId')['salary'].max().reset_index()
    rs1 = employee.merge(rs, on=['departmentId', 'salary'])
    rs2 = rs1.merge(department, left_on='departmentId', right_on='id')
    return rs2[['name_y', 'name_x', 'salary']].rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})