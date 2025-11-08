import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    string = 'SecondHighestSalary'
    rs = pd.DataFrame(employee['salary'].unique(), columns=[string]).sort_values(by=string, ascending=False)

    if len(rs) < 2 :
        return pd.DataFrame({string: [None]})

    return rs.iloc[[1]]