# 0x0E. SQL - More Queries

Welcome to the **0x0E. SQL - More Queries** subproject!

In this subproject, we delve deeper into the world of SQL queries and database manipulation. Building upon the foundational knowledge gained in previous subprojects, we'll explore advanced querying techniques, data manipulation, and optimization strategies.

## Table of Contents

- [Introduction](#introduction)
- [Objectives](#objectives)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Topics Covered](#topics-covered)
- [How to Use](#how-to-use)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In the **0x0E. SQL - More Queries** subproject, we focus on expanding our SQL skills to tackle more complex scenarios. We'll learn how to craft intricate queries, optimize database performance, and efficiently manage data relationships. By mastering these advanced techniques, you'll be better equipped to handle real-world database challenges.

## Objectives

- Enhance your SQL querying skills with advanced techniques.
- Understand and apply various types of SQL joins, including INNER JOIN, LEFT JOIN, RIGHT JOIN, and more.
- Explore subqueries, aggregate functions, and window functions.
- Optimize database performance through indexing and query optimization.
- Manage data relationships effectively using foreign keys and constraints.

## Prerequisites

Before you begin, make sure you have a solid grasp of the basics of SQL, including data retrieval, filtering, and basic joins. You should also have access to a SQL database management system such as MySQL, PostgreSQL, or SQLite.

## Getting Started

1. Clone this repository to your local machine or download the subproject files.
2. Set up your preferred SQL database management system if you haven't already.
3. Follow the instructions in the subproject files to complete the exercises and challenges.

## Topics Covered

- Advanced SQL queries
- Different types of joins (INNER, LEFT, RIGHT, FULL OUTER)
- Subqueries and correlated subqueries
- Aggregate functions (SUM, COUNT, AVG, MAX, MIN)
- Window functions and analytical queries
- Indexing and query optimization
- Data relationships and foreign keys

## How to Use

Each exercise or challenge in this subproject will be contained in its own directory. Inside each directory, you'll find the necessary SQL files and instructions. Follow the steps outlined in the instructions to complete each task.

Feel free to explore the SQL files and use them as a reference for understanding the concepts and syntax.

## Examples

```sql
-- Example of an INNER JOIN to retrieve customer orders
SELECT customers.name, orders.order_date
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id;
```

```sql
-- Example of a subquery to find the average salary of employees
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
GROUP BY department_id;
```

## Contributing

Contributions to this subproject are welcome! If you find any issues, have suggestions for improvements, or want to add new exercises, feel free to submit a pull request.

## License

This subproject is licensed under the [MIT License](LICENSE).

---

Happy querying and database exploring!

