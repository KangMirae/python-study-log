import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    string = f'getNthHighestSalary({N})'
    rs = pd.DataFrame(employee['salary'].unique(), columns=[string]).sort_values(by=string, ascending=False)

    if (len(rs) < N) | (N <= 0) :
        return pd.DataFrame({string: [None]})

    return rs.iloc[[N-1]]