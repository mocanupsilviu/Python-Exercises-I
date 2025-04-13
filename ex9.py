"""
Exercise 9
Problem statement:
 1. create a data file data.txt with the following data
 empid,empname,emplocation,empsalary
 e001,iniyal,chennai,20000.00
 e002,aniyal,bangalore,25000.00
 e003,indulekha,trivandrum,18000.00
 2. open the file, read line by line
 - extract data and put it in the following format
 {
 "employees": [
 {
 "empid":"e001",
 "empname":"iniyal",
 "emplocation":"chennai"
 "empsalary":20000.00
 },
 {
 "empid":"e002",
 "empname":"iniyal",
 "emplocation":"chennai"
 "empsalary":20000.00
 },{
 }
 ]
 }
 Problem statement:
 create a data file data.txt with the following data
 empid,empname,emplocation,empsalary
 e001,iniyal,chennai,20000.00
 e002,aniyal,bangalore,25000.00
 1. Get the header columns from the user separated by ,
 For e.g empid,empname
 empname
 empid,empname,emplocation
 *
 empname,empsalary
 Output should be based on the header columns
 For e.g, if the userinput is empname, empsalary, then the following data should be printed
 2. open the file, read line by line
 - extract data and put it in the following format
 {
 "employees": [
 {
 "empname":"iniyal",
 "empsalary":20000.00
 },
 {
 "empname":"iniyal",
 "empsalary":20000.00
 }
 ]
 }
 Output format:
 dict
 - list
 - dict
"""

import csv
import json

data = """empid,empname,emplocation,empsalary
e001,iniyal,chennai,20000.00
e002,aniyal,bangalore,25000.00
e003,indulekha,trivandrum,18000.00
"""

with open('data.txt', 'w') as file:
    file.write(data)

with open('data.txt', 'r') as file:
    csv_reader = csv.DictReader(file)
    headers = csv_reader.fieldnames

columns_to_extract = ['empid', 'empname', 'emplocation', 'empsalary']

employees = []
with open('data.txt', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        employee = {key: row[key] for key in columns_to_extract}
        employees.append(employee)

output = {"employees": employees}
print(json.dumps(output, indent=4))
