import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['duration'] = employees['out_time'] - employees['in_time']	# 행별 체류시간 구하기
    rs = employees.groupby(['event_day','emp_id'])['duration'].sum().reset_index()  # 일자별 체류시간 합계 구하기 및 데이터프레임화
    rs.columns = ['day', 'emp_id', 'total_time']    # 컬럼명 변경 및 지정
    return rs