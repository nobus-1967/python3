#!/usr/bin/env python3
# Write a comma separated value (CSV) file and then read it.


def main():
    """Write and read a comma separated value (CSV) file."""
    persons = [('George', 'New York', 32),
               ('Eve', 'Boston', 29),
               ('Matt', 'Los Angeles', 26)]
    
    print('This program demonstrates how to write and read CSV files.')
    print('CSV (comma-separated values) is a plain text consists of records;')
    print('records include the same fields (i.e. values) separated by commas.')
    print()
    print('The example data list consists of 3 tuples (each with 3 values):')
    print('name (of a person), city and age.')
    print()
    print('These records:')
    print('------------------')
    
    records = show_persons(persons)
    
    print('Let\'s write these data into a CVS-file (persons.cvs)...')
    
    filename = 'persons.cvs'
    
    write_csv(records, filename)
    
    print('Well, then read and display a CVS-file (persons.cvs)...')
    print()
    print('The content of this file:')
    print('-------------')
    
    print_csv(filename)
    
    print('Seems our program works well!')
    print('And do you know that a CVS file can be read by almost all')
    print('spreadsheets and database management systems, including')
    print('Microsoft Excel, Apple Numbers and LibreOffice Calc & Base?')


def show_persons(persons):
    """Show and return data from list of tuples."""
    records = list()
    
    for person in persons:
        name, city, age = person
        record = f'{name},{city},{age}\n'
        records.append(record)
        
        print(record, end='')
        
    print()
    
    return records
        
        
def write_csv(records, filename):
    """Write data into a CSV file."""
    with open(filename, 'w') as csv:
        csv.write('name,city,age\n');
        
        for record in records:
            csv.write(record)


def print_csv(filename):
    """Read and print a CVS file."""
    with open(filename, 'r') as csv:
        for record in csv:
            print(record, end='')
            
    print()


if __name__ == '__main__':
    main()
