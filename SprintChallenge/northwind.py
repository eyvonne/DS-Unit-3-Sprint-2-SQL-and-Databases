from query import SqlQueries

cursor = SqlQueries('northwind_small.sqlite3')

# ten most expensive items


def mostExpensive():
    '''prints the ten most expensive items, outputs a table'''
    print('What are the ten most expensive items')
    cursor.tquery('''SELECT * FROM product
                            ORDER BY UnitPrice DESC
                            LIMIT 10;''')

# average age of employee at hiring


def averageAge():
    '''prints the average age of an employy at hire, output: 37.222'''
    print('Whats the average age of an employee at hire?')
    hire_age = '''SELECT AVG(HireDate-BirthDate)
                FROM employee;'''
    cursor.tquery(hire_age)

# How does the average age of employee at hire vary by city?


def cityAge():
    '''prints a table of the average age of employees at hire
    divided by the city that they were hired in, outputs a table'''
    print('variation of age by hire city')
    city_age = '''SELECT AVG(HireDate-BirthDate), city
                FROM employee
                GROUP BY city;'''
    cursor.tquery(city_age)

# Part three, Joins

# whats the ten most expensive items and who supplies them?


def expensiveSuppliers():
    '''prints the ten most expensive items and who supplies them,
    outputs a table'''
    print('The ten Most expensive Items and who supplies them')
    expensive_supply = '''SELECT pd.ProductName, pd.UnitPrice, sp.CompanyName
                        FROM product AS pd
                        INNER JOIN supplier AS sp
                        ON pd.SupplierID=sp.id
                        ORDER BY pd.UnitPrice DESC
                        LIMIT 10;'''
    cursor.tquery(expensive_supply)

# Whats the largest Category by number of products


def largestCat():
    '''prints the largest category and how many products are in it,
    output: Confections, 13'''
    print('The Category with the most products')
    big_category = '''SELECT cat.CategoryName, COUNT(pd.Id) as prods
                    FROM Category AS cat
                    INNER JOIN Product AS pd
                    ON pd.CategoryID=cat.Id
                    GROUP BY cat.CategoryName
                    ORDER BY prods DESC
                    LIMIT 1;'''
    cursor.tquery(big_category)

# Who has the most Territories?


def empTerr():
    '''prints out which employee has the most territory,
    output: Robert King, 10'''
    print('The employee with the most territory')
    emp_territory = '''SELECT emp.FirstName, emp.LastName,
                    COUNT(et.TerritoryId) as Territories
                    FROM Employee AS emp, EmployeeTerritory as et
                    WHERE emp.Id = et.EmployeeID
                    GROUP BY emp.Id
                    ORDER BY Territories DESC
                    LIMIT 1'''
    cursor.tquery(emp_territory)
