from datetime import datetime
dt1=datetime.now()
dt2=datetime(2024,2,5,3,15,8)
difference=dt1-dt2
print(difference.total_seconds())