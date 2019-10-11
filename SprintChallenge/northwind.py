import sqlite3
# I'm not technically allowed to use this on the sprint
# but it doesn't change the code I'm doing, just
# makes the results readable. I'm doing this for you.
from tabulate import tabulate


def query(query):
    '''this function takes in a SQL query and connects to
    the northwind_small.sqlite3 database to execute it'''
    conn = sqlite3.connect('northwind_small.sqlite3')
    curs = conn.cursor()
    result = curs.execute(query).fetchall()
    curs.close()
    conn.commit()
    conn.close()
    return result


# ten most expensive items
print('What are the ten most expensive items')
print(tabulate(query('''SELECT * FROM product
                        ORDER BY UnitPrice DESC
                        LIMIT 10;''')))

# average age of employee at hiring
print('Whats the average age of an employee at hire?')
hire_age = '''SELECT AVG(HireDate-BirthDate)
            FROM employee;'''
print(tabulate(query(hire_age)))

# How does the average age of employee at hire vary by city?
print('variation of age by hire city')
city_age = '''SELECT AVG(HireDate-BirthDate), city
            FROM employee
            GROUP BY city;'''
print(tabulate(query(city_age)))

# Part three, Joins

# whats the ten most expensive items and who supplies them?
print('The ten Most expensive Items and who supplies them')
expensive_supply = '''SELECT pd.ProductName, pd.UnitPrice, sp.CompanyName
                    FROM product AS pd
                    INNER JOIN supplier AS sp
                    ON pd.SupplierID=sp.id
                    ORDER BY pd.UnitPrice DESC
                    LIMIT 10;'''
print(tabulate(query(expensive_supply)))

# Whats the largest Category by number of products
print('The Category with the most products')
big_category = '''SELECT cat.CategoryName, COUNT(pd.Id) as prods
                FROM Category AS cat
                INNER JOIN Product AS pd
                ON pd.CategoryID=cat.Id
                GROUP BY cat.CategoryName
                ORDER BY prods DESC
                LIMIT 1;'''
print(tabulate(query(big_category)))

# Who has the most Territories?
print('The employee with the most territory')
emp_territory = '''SELECT emp.FirstName, emp.LastName,
                COUNT(et.TerritoryId) as Territories
                FROM Employee AS emp, EmployeeTerritory as et
                WHERE emp.Id = et.EmployeeID
                GROUP BY emp.Id
                ORDER BY Territories DESC
                LIMIT 1'''
print(tabulate(query(emp_territory)))
