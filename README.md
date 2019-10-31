# py_handles_csv
reading and writing CSV files in python using csv and pandas module

# What CSV Stands For ?
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

# Reading CSV File
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

# Options With Reader
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

# Reading CSV Files Into Dictionary
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

# Writing CSV Data In File
csv library has **wirter** object and **write_row()** method through which we can write 
to csv file

**writing_csv.py**
```
import csv

with open('employee_file.csv', 'w') as csvfile:
	employee_writer = csv.writer(csvfile)
	employee_writer.write_row(['name', 'department', 'started'])
	employee_writer.writer_row(['John Smith', 'Accounting', 'November'])
	employee_writer.writer_row(['Erica Meyers', 'IT', 'March'])
```

Alternatively you could have used 

**writing_csv.py**
```
import csv

with open('employee_file.csv', 'w') as csvfile:
	employee_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	employee_writer.write_row(['name', 'department', 'started'])
	employee_writer.writer_row(['John Smith', 'Accounting', 'November'])
	employee_writer.writer_row(['Erica Meyers', 'IT', 'March'])

```

Run the file 

```
python writing_csv.py
```

A new file named ```employee_file.csv``` is created

```
name,department,started

John Smith,Accounting,November

Erica Meyers,IT,March

```

So why is this extra line added after each row, we wouldn't want this to happen. If we
had another field named **id** then using **row number** to automatically provide **id**
would completely go wrong. It did go wrong in my [python_intermediate](https://github.com/Alexmhack/python_intermediate/blob/master/python_csv/data.csv
) tutorial.

Well this happened because in the python3 we need to open the file with a attribute
```newline=''``` so that newline doesn't use ```\n```

Editing the code a bit,

**writing_csv.py**
```
import csv

with open('employee_file.csv', 'w', newline='') as csvfile:
	employee_writer = csv.writer(csvfile)
	employee_writer.writerow(['name', 'department', 'started'])
	employee_writer.writerow(['John Smith', 'Accounting', 'November'])
	employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

```

Running this version of file would give results,

```
name,department,started
John Smith,Accounting,November
Erica Meyers,IT,March
```

Here the first row represents the column names, the values start from second line.

The quotechar optional parameter tells the csv writer which character to use when 
quoting fields while writing.

1. If quoting is set to csv.QUOTE_MINIMAL, then .writerow() will quote fields only if they contain the delimiter or the quotechar. This is the default case.
2. If quoting is set to csv.QUOTE_ALL, then .writerow() will quote all fields.
3. If quoting is set to csv.QUOTE_NONNUMERIC, then .writerow() will quote all fields containing text data and convert all numeric fields to the float data type.
4. If quoting is set to csv.QUOTE_NONE, then .writerow() will escape delimiters instead of quoting them. In this case, you also must provide a value for the escapechar optional parameter.

# Writing From Dictionary Into File
Just like **csv** has ```DictReader``` for reading data into dictionary, csv also has
an object to write data from dictionary

**csv_dictwriter.py**
```
import csv

with open('employee_file1.csv', 'w', newline='') as csvfile:
	fieldnames = ['emp_name', 'dept', 'birth_month']
	employee_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	employee_writer.writeheader()
	employee_writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
	employee_writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
```

```csv.DictWriter``` has to be provided the required argument ```fieldnames``` which is
a list containing the ```keys``` for dictionary.

Just like ```csv.writer``` we use ```writerrow({})``` but this time passing a dict 
containing the ```values``` for ```keys```

# Parsing CSV File Using [Pandas](http://pandas.pydata.org/index.html)
**Pandas** library comes into play when you have a lot of data to analyze. **Pandas** is
highly recommended for processing arge amount of data.

Install pandas using

```
pip install pandas
```

**Reading the CSV into a pandas DataFrame is quick and straightforward:**

**pandas_reads_csv.py**
```
import pandas

df = pandas.read_csv('hrdata.csv')
print(df)
```

Run the file

```
> python pandas_reads_csv.py

             Name Hire Date   Salary  Sick Days remaining
0  Graham Chapman  03/15/14  50000.0                   10
1     John Cleese  06/01/15  65000.0                    8
2       Eric Idle  05/12/14  45000.0                   10
3     Terry Jones  11/01/13  70000.0                    3
4   Terry Gilliam  08/12/14  48000.0                    7
5   Michael Palin  05/23/13  66000.0                    8
```

A lot cleaner printing, right!

**So what happened ?**

Just three lines of code and we are done!

```pandas.read_csv(file_path)``` is the piece of code that does all the work. Pandas
opens, analyzes and reads the csv file and stores the data in **df (dataframe)**

Pandas numbered or actually indexed the data starting from ```0``` this is default 
nature since we didn't give the ```index_col``` parameter. 

Let's index our dataframe from name field

```
import pandas 

df = pandas.read_csv('hrdata.csv', index_col='Name')
print(df)
```

And what do you know

```
               Hire Date   Salary  Sick Days remaining
Name
Graham Chapman  03/15/14  50000.0                   10
John Cleese     06/01/15  65000.0                    8
Eric Idle       05/12/14  45000.0                   10
Terry Jones     11/01/13  70000.0                    3
Terry Gilliam   08/12/14  48000.0                    7
```

Now we see that our ```Hire Dat``` column is of type ```<class 'str'>```.

Let’s fix the data type of the Hire Date field. You can force pandas to read data as a 
date with the parse_dates optional parameter, which is defined as a list of column 
names to treat as dates:

```
import pandas

df = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
print(df)
```

```
                Hire Date   Salary  Sick Days remaining
Name
Graham Chapman 2014-03-15  50000.0                   10
John Cleese    2015-06-01  65000.0                    8
Eric Idle      2014-05-12  45000.0                   10
Terry Jones    2013-11-01  70000.0                    3
Terry Gilliam  2014-08-12  48000.0                    7
Michael Palin  2013-05-23  66000.0                    8
```

Formatted date is printed which is of type ```<class 'pandas._libs.tslibs.timestamps.Timestamp'>```

If the csv file doesn't has the first line that tells the columns for file or you
want to override the columns and give your own then in that case you can use 
```header=0```

```
import pandas

df = pandas.read_csv('hrdata.csv', 
            index_col='Employee', 
            parse_dates=['Hired'], 
            header=0, 
            names=['Employee', 'Hired','Salary', 'Sick Days'])
print(df)
```

On changing the header names we get 

```
                    Hired   Salary  Sick Days
Employee
Graham Chapman 2014-03-15  50000.0         10
John Cleese    2015-06-01  65000.0          8
Eric Idle      2014-05-12  45000.0         10
Terry Jones    2013-11-01  70000.0          3
Terry Gilliam  2014-08-12  48000.0          7
Michael Palin  2013-05-23  66000.0          8
```

# Writing CSV Files With Pandas
Just as Reading CSV with pandas could be done in three lines of code Writing CSV with 
pandas is also simple, just using ```df.to_csv(file_path)``` and we are done.

**pandas_to_csv.py**
```
import pandas

df = pandas.read_csv(
	'hrdata.csv',
	index_col='Employee',
	parse_dates=['Hired'],
	header=0,
	names=['Employee', 'Hired', 'Salary', 'Sick Days']
)

df.to_csv('hrdata_modified.csv')

df_modified = pandas.read_csv(
	'hrdata_modified.csv',
	index_col='Employee',
	parse_dates=['Hired'],
)

print(df_modified)

```

Running file we get a new file ```hrdata_modified.csv```

```
                    Hired   Salary  Sick Days
Employee
Graham Chapman 2014-03-15  50000.0         10
John Cleese    2015-06-01  65000.0          8
Eric Idle      2014-05-12  45000.0         10
Terry Jones    2013-11-01  70000.0          3
Terry Gilliam  2014-08-12  48000.0          7
Michael Palin  2013-05-23  66000.0          8
```
