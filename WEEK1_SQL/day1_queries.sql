Day 1: SELECT and WHERE Queries
Monday, May 18, 2026
First 6 SQL queries

Query 1: SELECT all columns and rows
SELECT * FROM users;

Query 2: SELECT specific columns (name and email)
SELECT name, email FROM users;

 Query 3: WHERE clause - age greater than 26
SELECT * FROM users WHERE age > 26;

Query 4: WHERE clause - city equals Kochi
SELECT * FROM users WHERE city = 'Kochi';

Query 5: WHERE with AND - two conditions must be true
SELECT * FROM users WHERE age > 25 AND city = 'Delhi';

Query 6: WHERE with OR - one of two conditions must be true
SELECT name FROM users WHERE city = 'Kochi' OR city = 'Mumbai';