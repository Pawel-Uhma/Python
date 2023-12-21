import pandas as pd

table = pd.read_csv('ds_salaries.csv')

table = table.drop(columns = 'salary', axis = 1)
table = table.drop(columns = 'salary_currency', axis = 1)

table = table[(table.employee_residence != table.company loca)]
table.sort_values('work_year', inplace = True, ascending = False)

table.to_csv('dest.csv')
print(table)
