import csv

with open('employee_data1.csv') as csvfile:
	csv_reader = csv.reader(csvfile)
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			print(f"Columns are {", ".join(row)}")
			line_count += 1
		else:
			print(f"\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.")
			line_count += 1
	print(f"Processed {line_count} lines")

