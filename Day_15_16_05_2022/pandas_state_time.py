#date time conversion
import pandas as pd
from datetime import date
df=pd.DataFrame({'name':['alice','bob','charlie'],
                 'date_of_birth':['10/25/2005','10/29/2002','01/01/2001']})
print("Before Conversion")
print(df)
df['date_of_birth']=pd.to_datetime(df['date_of_birth'])
print("After Conversion")

print(df)
print("Filter the data")
#convert dt and fetch that matches
print(df[df['date_of_birth']<pd.Timestamp(date(2002,1,1))])



