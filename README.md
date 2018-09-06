# py_handles_csv
reading and writing CSV files in python using csv and pandas module

# What CSV stands for ?
**CSV** stands for **Comma Separated Values File** is just like a plain file that uses 
a different approach for structuring data.

If you open a csv file in Sublime Text you will find simple plain text separated with 
commas

**Example**
```
id,name,email,amount,date,sent
1,Hopper,email-address,269,03 Sep at 21:14,False
2,Drake,email-address,690,03 Sep at 21:14,False
3,Adam,email-address,20,03 Sep at 21:14,False
4,Justin,email-address,199,03 Sep at 21:14,False
```

In general, the separator character is called a delimiter, and the comma is not the 
only one used. Other popular delimiters include the tab (\t), colon (:) and semi-colon 
(;) characters. Properly parsing a CSV file requires us to know which delimiter is 
being used.

CSV files are very useful for handling large chunk of data and this type of data can be
very easily handled with any programming language which supports string handling like
python.

**Python** has built-in [csv](https://docs.python.org/3/library/csv.html) library for
handling csv data. Using python csv library we can perform many tasks on csv files and
csv data like reading, writing and processing data from csv files.

# Reading CSV file
**csv** library has **reader** object for specifically reading purpose of csv files.
The ```with open()``` function in python opens any file including csv files in text 
format, the text is then passed onto reader object which does all the processing of 
the csv data.

We have a file ```employee_data.csv``` file which has values in comma seperated 
format, ```reading_csvfile.py``` opens the file and reads data from it using csv library

**reading_csvfile.py**
```
import csv 

with open('employee_data.csv') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
```

**NOTE:** delimiter specifies the character used to separate each field. The default is 
the comma (',').

# Options with reader
There are options with reader object along with ```delimiter``` like ```escapechar``` 
and ```quotechar```.

1. quotechar specifies the character used to surround fields that contain the delimiter 
character. The default is a double quote (' " ').

2. escapechar specifies the character used to escape the delimiter character, in case 
quotes aren’t used. The default is no escape character.

**But will we use these options ?**

These options come in handy when we have csv data that conflicts with the delimiter.
For example in ```employee_data.csv``` file has comma separated values, what if the
address field of an employee has a ```,``` in it

```
...address,
...56, South Avenue,
```

The extra comma will cause problems for csv reader. To solve this issue we can,

1. **Use a different delimiter**
That way, the comma can safely be used in the data itself. You use the delimiter 
optional parameter to specify the new delimiter.

2. **Wrap the data in quotes**
The special nature of your chosen delimiter is ignored in quoted strings. Therefore, 
you can specify the character used for quoting with the quotechar optional parameter. 
As long as that character also doesn’t appear in the data, you’re fine.

3. **Escape the delimiter characters in the data**
Escape characters work just as they do in format strings, nullifying the interpretation 
of the character being escaped (in this case, the delimiter). If an escape character is 
used, it must be specified using the escapechar optional parameter.

**Using quotechar**

**employee_data1.csv**
```
name,department,birthday month, address
John Smith,Accounting,November, 56, South Avenue
Erica Meyers,IT,March, 45, Washington Stree
Alex Hopper,EC,March, 106, Lake Palace
Micheal Jeff,IT,March, 23 A, Wallace Mansion
Ethan Hunt,IT,March, 21, Jump Stree
```

**using_quotechar.py**
```
import csv

with open('employee_data1.csv') as csvfile:
	
```

# Reading csv files into dictionary
**csv** library along with the simple reader that just reads the plain text into a csv
formatted data. csv has one more reader object that works in a slightly different way.

```csv.DictReader``` reads the csv file into a dictionary object with **key** of the 
dictionary as the header/column names and **values** as the values in each corresponding 
row.

This is how the dictionary looks like

```
OrderedDict([('name', 'John Smith'), ('department', 'Accounting'), ('birthday month', 'November')])
OrderedDict([('name', 'Erica Meyers'), ('department', 'IT'), ('birthday month', 'March')])
...
```

This is the data from the ```employee_data.csv``` file. Remember the column names

1. name
2. department
3. birthday month

Now take a look at the ```employee_data.csv``` file 

```
name,department,birthday month
John Smith,Accounting,November
Erica Meyers,IT,March
```

Code to reading file into dict is

**csv_dictreader.py**
```
import csv

with open('employee_data.csv') as csvfile:
	csv_reader = csv.DictReader(csvfile)
	for row in csv_reader:
		print(row)

```


Since the ```csv.DictReader``` returns an [dict](https://developers.google.com/edu/python/dict-files) object, question arises

**Is this dict object the regular dictionary that exists in python ?**

The answer is **Yes**

**You can actually apply all operations that can be done on dictionaries in python**

Just like we used our data to print useful information in ```reading_csvfile.py``` we 
can do the same here.

```
import csv

with open('employee_data.csv') as csvfile:
	csv_reader = csv.DictReader(csvfile)
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			print(f'Column names are {", ".join(row)}')
			line_count += 1
		 print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
```

Note how we use ```row["name"]``` to get the name key from the dictionary.

But how did csv know that **name** is actually a key to be used in dict object.

The first line of the CSV file is assumed to contain the keys to use to build the 
dictionary. If you don’t have these in your CSV file, you should specify your own keys 
by setting the fieldnames optional parameter to a list containing them.

When writing data into csv file we need to specify the fieldnames attribute for csv file
which we will see in a minute.


