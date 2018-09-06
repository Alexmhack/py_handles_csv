import pandas

df = pandas.read_csv('hrdata.csv')

df_2 = pandas.read_csv('hrdata.csv', index_col='Name')

df_3 = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])

df_4 = pandas.read_csv(
	'hrdata.csv',
	index_col='Employee',
	parse_dates=['Hired'],
	header=0,
	names=['Employee', 'Hired', 'Salary', 'Sick Days']
)

print(df_4)
