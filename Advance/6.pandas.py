"""
Pandas helps work with:
CSV files
Excel files
Tables of data
"""

import pandas as pd
data = {
    "Name": ["Wilson", "John"],
    "Age": [18, 20]
}
df = pd.DataFrame(data)
print(df)
"""
output:
  Name  Age
0 Arup  18
1 John  20
"""

#read CSV
import pandas as pd
df = pd.read_csv("students.csv")
print(df.head())
