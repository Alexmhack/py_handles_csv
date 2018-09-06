import csv

with open('employee_file.csv', 'w', newline='') as csvfile:
	employee_writer = csv.writer(csvfile)
	employee_writer.writerow(['name', 'department', 'started'])
	employee_writer.writerow(['John Smith', 'Accounting', 'November'])
	employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
