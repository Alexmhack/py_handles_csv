import csv

with open('employee_file1.csv', 'w', newline='') as csvfile:
	fieldnames = ['emp_name', 'dept', 'birth_month']
	employee_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	employee_writer.writeheader()
	employee_writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
	employee_writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
