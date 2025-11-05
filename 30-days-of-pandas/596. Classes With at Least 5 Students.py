import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    rs = courses.groupby('class')['student'].sum().reset_index()
    return rs[rs['student'].str.len()>=5][['class']]