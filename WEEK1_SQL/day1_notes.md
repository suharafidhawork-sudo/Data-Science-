 Day 1: SELECT and WHERE


Monday, May 18, 2026

 Topics Learned
- SELECT statement (choose columns)
- WHERE clause (filter rows)
- Comparison operators (>, <, =)
- Logical operators (AND, OR)

Key Concepts

 SELECT
- What: Choose which columns to display
- syntax: SELECT column1, column2 FROM table;
- Example: SELECT name, email FROM users;
- Why: You don't always need all columns
- SELECT *: Shows all columns

 WHERE
- What: Filter rows based on condition
- Syntax: SELECT * FROM table WHERE condition;
- Example: SELECT * FROM users WHERE age > 26;
- Why: You only want specific rows matching criteria

 AND
- What: Both conditions must be TRUE
- Example: WHERE age > 25 AND city = 'Delhi'
- Meaning: Age MUST be > 25 AND city MUST be Delhi
- Both must be true: Only then row is included

 OR
- What: One condition must be TRUE
- Example: WHERE city = 'Kochi' OR city = 'Mumbai'
- Meaning: City can be Kochi OR Mumbai
- Either can be true: If either true, row included

 Comparison Operators
- >: Greater than (age > 26)
- <: Less than (age < 30)
- =: Equals (city = 'Kochi')
- !=: Not equal (age != 25)

 Queries Written Today

 Query 1: SELECT * FROM users;
- Purpose: Show all data
- Result: All 6 users, all columns
- Learning: SELECT * means everything

Query 2: SELECT name, email FROM users;
- Purpose: Show specific columns only
- Result: 6 users with 2 columns each
- Learning: Can choose which columns to show

 Query 3: SELECT * FROM users WHERE age > 26;
- Purpose: Filter by age
- Result: 3 users (Priya 28, Arjun 30, Vikram 32)
- Learning: WHERE filters rows by condition

 Query 4: SELECT * FROM users WHERE city = 'Kochi';
- Purpose: Filter by city
- Result: 2 users (Raj, Neha)
- Learning: Text values need QUOTES
 Query 5: SELECT * FROM users WHERE age > 25 AND city = 'Delhi';
- Purpose: Multiple conditions with AND
- Result: 1 user (Priya)
- Learning: AND means BOTH must be true

 Query 6: SELECT name FROM users WHERE city = 'Kochi' OR city = 'Mumbai';
- Purpose: Multiple conditions with OR
- Result: 3 users (Raj, Ananya, Neha)
- Learning: OR means ONE can be true

 What Was Clear
✅ SELECT * works perfectly
✅ WHERE filtering is logical and clear
✅ AND/OR makes sense when I test it
✅ Seeing actual results helps understanding



 
The query results make the concepts REAL!
I can SEE what each query does.
Not just reading - actually SEEING!

 Progress
✅ 6 SQL queries written
✅ All tested and working
✅ All documented
✅ Ready for Day 2!

Tomorrow
JOINs - combining multiple tables
COMPLETED :1/184 DAYS