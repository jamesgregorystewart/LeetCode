# SQL

[Calculate Special Bonus](https://leetcode.com/explore/learn/card/sql-language/683/sql-syntax/4321/)

```PostgreSQL
select employee_id, 
        case 
            when employee_id % 2 = 1 and name not like 'M%' then salary
            else 0
        end as bonus
from employees order by employee_id;
```

[Swap Salary](https://leetcode.com/explore/learn/card/sql-language/683/sql-syntax/4323/)

```PostgreSQL
update salary 
set sex =
    case
        when sex = 'm' then 'f'
        when sex = 'f' then 'm'
    end
;
```

## Aggregate Functions

```SQL
SELECT COUNT(*), `age` FROM `new_schema`.`users` GROUP BY age;
```

New we will alias the aggregation column and sort the results from small to large.

```SQL
SELECT COUNT(*) AS `age_count`, `age`
FROM `new_schema`.`users`
GROUP BY age
ORDER BY `age_count`;
```

[Find Followers Count](https://leetcode.com/explore/learn/card/sql-language/683/sql-syntax/4328/)
```SQL
select user_id, count(follower_id) as follower_count
from followers
group by user_id;
```

[Duplicate Emails](https://leetcode.com/explore/learn/card/sql-language/683/sql-syntax/4330/)
```SQL
select Email as Email from (
    select email as Email, count(email) as email_count
    from person
    group by email
)
where email_count > 1;
```

[Actors and Directors Who Cooperated at Least Three Times](https://leetcode.com/explore/learn/card/sql-language/683/sql-syntax/4331/)
```SQL
select actor_id, director_id
from (
    select actor_id, director_id, count(director_id) as collaborations
    from ActorDirector
    group by actor_id, director_id
)
where collaborations >= 3;
```

## Subqueries

```SQL
SELECT * FROM (
  SELECT CONCAT(`id`, '-', `name`) AS `identification`, `age` 
  FROM `new_schema`.`users`
) AS subquery
WHERE `identification` LIKE '%J%';
```
OR with a CTE (Common Table Expression)
```SQL
WITH CTE_Users AS (
  SELECT CONCAT(`id`, '-', `name`) AS `identification`, `age`
  FROM `new_schema`.`users`
)
SELECT * FROM CTE_Users
WHERE `identification` LIKE '%J%';
```

## HAVING vs WHERE

SQL provides the HAVING clause, which allows filtering on calculated or aggregated columns. However, it’s important to note that the direct use of HAVING without GROUP BY is a misuse of SQL syntax. The correct approach involves using a subquery or a Common Table Expression (CTE) to first define the calculated column, then applying the WHERE clause on that result. Here’s how:

Some might think that WHERE and HAVING can be used interchangeably. However, over-relying on HAVING can lead to performance issues as data volume grows. This is because HAVING is designed for filtering aggregate functions or the results of calculations done within the query, and its misuse can impact database efficiency.

The difference in performance between WHERE and HAVING is tied to how SQL databases index and retrieve data. WHERE is applied before data is grouped, making it more efficient for initial data filtration. HAVING, on the other hand, is applied after, making it less efficient for initial filtering. Understanding and using indexes effectively will be discussed in a future chapter titled "SQL in Business: Index"!


## JOINs

### LEFT JOINs and RIGHT JOINs

When using JOIN, the first thing we are familiar with is LEFT JOIN, which can be imagined as treating the table on the left side of the statement as the main table, and the other table as the attached table. When using the JOIN related syntax, all columns from both tables are displayed. However, if any the specific record of main table does not include any attached table records, the values of the columns in the attached table will be set to NULL.

```SQL
SELECT * FROM `new_schema`.`users`
LEFT JOIN `new_schema`.`orders` ON `users`.`id` = `orders`.`user_id`;
```

Right JOIN is just the opposite of LEFT JOIN and are interchangeable, as long as you order your main table appropriately

### INNER JOIN 

Although we have learned to combine data, do you occasionally find it strange to see data with NULL? At this time, we can learn how to use INNER JOIN to fetch records where both tables can be linked together. That is a common scenario for filtering data in practice, and the concept is like taking an intersection).

```SQL
SELECT * FROM `new_schema`.`users`
INNER JOIN `new_schema`.`orders` ON `users`.`id` = `orders`.`user_id`;
```

select visits.customer_id, count_no_trans from (
 select
)

[Customer Who Visited but Did Not Make any Transactions](https://leetcode.com/explore/learn/card/sql-language/684/sql-relationship/4338/)

```SQL
select visits.customer_id, count(visits.customer_id) as count_no_trans 
from visits
left join transactions on visits.visit_id = transactions.visit_id
where transactions.visit_id IS NULL 
group by customer_id;
```

[Market Analysis](https://leetcode.com/problems/market-analysis-i/description/)
```SQL
select 
    users.user_id as buyer_id, 
    users.join_date,
    count(orders.order_id) as orders_in_2019
from 
    users 
    left join orders on users.user_id = orders.buyer_id
    and order_date between '2019-01-01' and '2019-12-31'
group by 
    users.user_id,
    users.join_date
order by 
    users.user_id
```

## Subqueries

### Equal Condition
```SQL
SELECT * FROM `new_schema`.`orders`
WHERE user_id = (
  SELECT id FROM `new_schema`.`users`
  WHERE name = 'John'
);
```

### Contain Condition
```SQL
SELECT * FROM `new_schema`.`orders`
WHERE user_id IN (
  SELECT id FROM `new_schema`.`users`
  WHERE name LIKE '%j%'
);
```

[Sales Person](https://leetcode.com/explore/learn/card/sql-language/684/sql-relationship/4342/)
```SQL
select 
    salesperson.name as name
from 
    salesperson
where 
    salesperson.name not in 
    (
        select 
            salesperson.name
        from 
            salesperson
        inner join orders on salesperson.sales_id = orders.sales_id
        inner join company on orders.com_id = company.com_id
        and company.name = 'RED'
    )
```

[Customers Who Never Order](https://leetcode.com/explore/learn/card/sql-language/684/sql-relationship/4343/)
```SQL
select 
    customers.name as Customers
from
    customers
where 
    customers.id not in (
        select 
            distinct orders.customerId
        from
            orders
    )
```

[Customer Placing the Largest Number of Orders](https://leetcode.com/explore/learn/card/sql-language/684/sql-relationship/4344/)
```SQL
select 
    customer_number
from
    (
        SELECT
            customer_number, COUNT(*) as order_count
        FROM
            orders
        GROUP BY customer_number
        order by order_count desc
    )
limit 1
```

[Top Travelers](https://leetcode.com/explore/learn/card/sql-language/684/sql-relationship/4345/)
```SQL
select
    u.name as name,
    case
        when r.user_id is not null then sum(r.distance)
        else 0
    end as travelled_distance
from 
    users u
left join 
    rides r on u.id = r.user_id
group by 
    u.name,
    r.user_id
order by
    travelled_distance desc,
    name asc
```

[Employees with Missing Information](https://leetcode.com/explore/learn/card/sql-language/684/sql-relationship/4346/)
```SQL
select 
    employee_id
from
    employees
full join
    salaries using(employee_id)
where name is null or salary is null
```

## Foriegn Keys

```SQL
ALTER TABLE `new_schema`.`orders`
    ADD CONSTRAINT `orders_user_id_key`
    FOREIGN KEY (`user_id`)
    REFERENCES `new_schema`.`users` (`id`);
```

This adds protections from deleting a user from users table when there are records that refer to that user with foriegn Keys

# Query Optimizer


At a high level, a query optimizer plays a critical role in a database management system (DBMS) by determining the most efficient way to execute a given query. Given that the same query can often be executed through multiple paths (e.g., using different join orders or indexes), the optimizer's job is to analyze these possible paths and choose the one with the least estimated cost, considering factors like CPU usage, I/O operations, and memory consumption. The process involves several key steps and components:

1. Parsing and Syntax Check
First, the query is parsed to ensure it is syntactically correct. This step converts the query into a structured representation, such as a parse tree, which reflects the hierarchical structure of the query.

2. Query Rewriting
The optimizer may rewrite the query to a form that is equivalent in terms of results but potentially more efficient to execute. This can include simplifying expressions, eliminating redundant operations, or applying algebraic transformations.

3. Statistics Gathering
The optimizer relies on statistical information about the database tables and indexes involved in the query. This includes data like table sizes, index selectivity, and data distribution. These statistics are crucial for making informed decisions about the query execution plan.

4. Generation of Potential Execution Plans
Using the structured query representation and available statistics, the optimizer generates a set of potential execution plans. Each plan represents a strategy for executing the query, including how tables should be accessed (e.g., via full table scans or index lookups) and in what order joins should be performed.

5. Cost Estimation
For each potential execution plan, the optimizer estimates the cost associated with executing the plan. The cost model considers various factors, including the number of disk I/O operations required, the CPU time needed to process the rows, and the memory usage. The cost of a plan is a proxy for its expected execution time.

6. Plan Selection
After estimating the costs, the optimizer selects the execution plan with the lowest estimated cost. This plan is considered the most efficient way of executing the query given the current state of the database and the available statistics.

7. Execution
Finally, the selected plan is passed to the database engine's execution engine, which executes the query according to the plan.

# Case for Stored Procedures

Stored procedures are a powerful feature of many relational database management systems (RDBMS). They are SQL scripts, saved in the database, that are compiled once and can be executed many times. Stored procedures can take parameters, execute complex logic, return results, and can be used to encapsulate and enforce business logic at the database level. Below, we explore their purpose and various use cases.

### Purpose of Stored Procedures

1. **Performance Improvement**: Since stored procedures are compiled on their first execution and generally cached by the database system, subsequent executions are faster. This can significantly improve performance for complex queries and operations.
2. **Reduced Network Traffic**: By bundling several SQL commands into a single stored procedure, you minimize the back-and-forth communication between the application server and the database server. This can be particularly beneficial in high-latency environments.
3. **Security**: Stored procedures can enhance security by encapsulating the business logic, allowing users to execute database operations without granting them direct access to the tables. This means you can restrict direct SQL commands against the database and control access through stored procedures.
4. **Maintainability and Modularity**: Changes to business logic can often be made in the stored procedure without affecting the application code. This encapsulation offers better maintainability of the codebase. Stored procedures also promote code reuse.
5. **Centralized Business Logic**: Keeping the business logic centralized in the database ensures consistency in the implementation of the logic across different applications that access the database.

### Use Cases of Stored Procedures

1. **Data Validation**: Stored procedures can enforce data integrity and validation rules beyond what's defined in the schema constraints, ensuring that data meets business requirements before being inserted or updated in the database.
2. **Complex Business Logic**: They are ideal for encapsulating complex business logic that requires executing multiple SQL statements in a particular order, with conditional logic, or with complex calculations.
3. **Administrative Tasks**: Automation of administrative tasks like database maintenance operations (e.g., cleanup tasks, archiving data, monitoring database health) can be efficiently managed through stored procedures.
4. **Reporting**: For complex reporting needs, stored procedures can aggregate and summarize data, preparing it in a format suitable for reporting tools or applications.
5. **Batch Processing**: Stored procedures can handle batch processing of data efficiently, such as processing and transforming large volumes of data overnight or in real-time, as needed.
6. **Access Control**: By encapsulating database operations within stored procedures, you can provide fine-grained control over what actions users or applications can perform on the database, enhancing security.
7. **Integration with External Systems**: Stored procedures can be designed to interact with external systems, such as sending emails or integrating with other databases, as part of their execution logic.

### Conclusion

Stored procedures offer a robust way to encapsulate business logic, improve performance, and enhance security and maintainability of database operations. They are particularly useful in environments where complex business logic needs to be centralized, where performance and scalability are concerns, and where strict security around data access is required. However, the use of stored procedures should be balanced with considerations around database portability, as heavy reliance on them can make migrating to a different RDBMS platform more challenging.

# When to use a CTE vs a Temp Table

A Common Table Expression (CTE) and a temporary table are both tools used in SQL for organizing and simplifying complex queries, but they serve different purposes and have different strengths. Understanding what each is and when to use one over the other can significantly impact the performance, readability, and maintenance of your SQL queries.

### What is a CTE?

A CTE, or Common Table Expression, is a temporary result set that you can reference within a SELECT, INSERT, UPDATE, or DELETE statement. A CTE is defined using the `WITH` syntax and exists only during the execution of the query. CTEs are particularly useful for breaking down complex queries into simpler parts, making them easier to read and maintain. They're also great for recursive queries, such as hierarchical data processing.

**Syntax Example:**
```sql
WITH CTE_Name AS (
    SELECT column1, column2
    FROM table_name
    WHERE condition
)
SELECT * FROM CTE_Name;
```

### When to Use a CTE

- **Readability and Maintenance**: When you want to improve the readability of complex SQL queries by breaking them down into simpler parts.
- **Recursive Queries**: For executing recursive queries, like navigating hierarchical or tree-structured data.
- **Temporary Result Set**: When you need a temporary result set that is used within the scope of a single query execution.
- **No Physical Storage Requirement**: When you don’t need the results to persist beyond the immediate query.

### What is a Temporary Table?

A temporary table is a short-lived table that is created within the database and can be used to store and process intermediate results. Temporary tables are dropped automatically at the end of the database session or manually by the user. They are useful for storing results that need to be reused multiple times in subsequent queries or when performing complex manipulations of data.

**Syntax Example:**
```sql
CREATE TEMP TABLE TempTableName AS
SELECT column1, column2
FROM table_name
WHERE condition;
```

### When to Use a Temporary Table

- **Performance**: For complex operations that require reusing the result set multiple times. Storing the result in a temporary table can be faster since the data is written and can be indexed.
- **Large Intermediate Results**: When dealing with large volumes of data that might be too big to handle efficiently with a CTE.
- **Indexing and Constraints**: When you need to create indexes or enforce constraints on the intermediate result set to optimize further processing.
- **Multiple Query Reuse**: If the intermediate results need to be reused across multiple separate queries or in transactions.

### Summary of Differences

- **Scope and Persistence**: CTEs are defined within the scope of a single SQL statement and cannot be indexed, while temporary tables exist at the session level and can be indexed.
- **Performance**: CTEs can be faster for simpler queries or when the result set is used once. Temporary tables may perform better for larger data sets or when the result set is reused.
- **Use Case**: CTEs are ideal for readability and recursive queries. Temporary tables are better for large data sets and when needing to reuse the data, apply indexes, or enforce constraints.

In summary, whether you use a CTE or a temporary table depends on the specific needs of your query, including factors like the complexity of the query, the size of the data set, performance considerations, and how the intermediate results are used.

# Recursive Queries and how they work

A recursive query in SQL is used primarily to deal with hierarchical or tree-structured data, such as organization charts, file systems, or any scenario where a parent-child relationship exists. Recursive queries are particularly useful when the depth of the hierarchy is unknown or varies significantly, making it impractical to write a query with a fixed number of joins.

### How Does a Recursive Query Work?

A recursive query in SQL is usually constructed using Common Table Expressions (CTEs) with two main components:

1. **Anchor Member**: This is the initial query that retrieves the root of the recursion, i.e., the starting point of the hierarchy. It's the base result set upon which the recursion builds.
2. **Recursive Member**: This part of the query references the CTE itself, thus creating the recursion. It is responsible for adding rows to the result set by referring back to the data obtained in the previous step of the recursion.

The recursive process continues until no new rows are generated from the recursive member, at which point the query completes.

### Syntax of a Recursive Query

Here is a basic structure of a recursive CTE:

```sql
WITH RECURSIVE CTE_Name (column_list) AS (
    -- Anchor member
    SELECT column_list
    FROM table_name
    WHERE condition
    UNION ALL
    -- Recursive member
    SELECT column_list
    FROM table_name
    JOIN CTE_Name ON condition
)
SELECT * FROM CTE_Name;
```

### Example: Employee Hierarchy

Consider a table `employees` with columns `employee_id`, `name`, and `manager_id`, where `manager_id` refers to the `employee_id` of the employee's manager, creating a parent-child relationship.

```sql
WITH RECURSIVE EmployeeHierarchy AS (
    -- Anchor Member: Select the CEO (who has no manager)
    SELECT employee_id, name, manager_id, 1 AS depth
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    -- Recursive Member: Select each employee under their manager
    SELECT e.employee_id, e.name, e.manager_id, eh.depth + 1
    FROM employees e
    INNER JOIN EmployeeHierarchy eh ON e.manager_id = eh.employee_id
)
SELECT * FROM EmployeeHierarchy
ORDER BY depth, name;
```

### Why Use a Recursive Query?

- **Hierarchical Data Processing**: They are incredibly efficient for querying hierarchical data, like organizational structures, category trees in e-commerce systems, or threaded comments.
- **Path Building**: Useful for building paths or chains (e.g., breadcrumb navigation paths in websites).
- **Dynamic Depth**: They handle situations with varying and unknown depths without specifying a fixed number of joins or iterations.
- **Simplification**: Recursive queries can simplify complex SQL queries, making them more readable and easier to maintain, especially compared to equivalent iterative or cursor-based approaches.

Recursive queries are powerful but should be used judiciously as they can be resource-intensive and potentially lead to performance issues if not properly optimized or if the recursion depth becomes excessively large.

# SQL Injection and Mitigation Strategies

Yes, SQL injection is generally more likely, or at least easier to exploit, in a dynamic SQL context due to the way SQL commands are constructed and executed in such scenarios. Dynamic SQL involves constructing SQL statements as strings within an application and then executing those strings as queries. This method often involves concatenating user inputs with SQL command strings, which can inadvertently create opportunities for SQL injection if the inputs are not properly sanitized or validated.

### Why Dynamic SQL is More Vulnerable:

1. **String Concatenation**: In dynamic SQL, user inputs are often concatenated directly with SQL command strings. If the user input is not properly escaped or checked, an attacker can inject malicious SQL code.
2. **Lack of Prepared Statements**: Unlike static SQL, where prepared statements with placeholders can be used to separate the data from the code, dynamic SQL often relies on constructing the full query as a single string. This makes it harder to use the built-in protections offered by prepared statements or parameterized queries.
3. **Complexity of Sanitizing Inputs**: The dynamic nature of these queries can make it challenging to anticipate all possible forms of SQL injection attacks, leading to insufficient input validation and sanitization.
4. **Increased Attack Surface**: Applications that frequently use dynamic SQL for complex queries or to accommodate various user-driven query options can inadvertently increase the attack surface for SQL injection, simply due to the greater number of points where user input interacts with SQL commands.

### Mitigation Strategies:

- **Use Parameterized Queries**: Wherever possible, use parameterized queries or prepared statements, even in a dynamic SQL context. This allows the database to distinguish between code and data, regardless of user input.
- **Proper Input Sanitization**: Always validate and sanitize user inputs to ensure that they do not contain SQL code. This may involve stripping out or escaping certain characters.
- **Minimal Privileges**: Ensure that the database connections used by your application operate with the least privileges necessary to perform their function. This limits the potential damage of an SQL injection attack.
- **Use ORM Frameworks**: Object-Relational Mapping (ORM) frameworks can abstract SQL operations and inherently protect against SQL injection by using parameterized queries and other protective measures.
- **Regularly Review and Update**: Regularly review code for SQL injection vulnerabilities, especially when using dynamic SQL, and update it according to best practices and the latest security guidelines.

In summary, while dynamic SQL offers flexibility and can be powerful for certain applications, it also requires careful handling to prevent SQL injection vulnerabilities. Implementing robust input validation, using parameterized queries, and adhering to security best practices are key to mitigating these risks.

# Normalized vs Denormalized

### When to Normalize:

**Normalization** involves structuring a database according to a set of principles to reduce data redundancy and improve data integrity. The process typically involves dividing large tables into smaller, related tables and defining relationships between them. 

**Use Cases for Normalization:**

- **Improving Write Efficiency**: Normalization can reduce write latency in scenarios where data redundancy is minimized, leading to fewer updates and inserts. This can also save storage space.
- **Maintaining Data Integrity**: By reducing redundancy, normalization helps in maintaining data consistency and integrity through the use of constraints and relationships.
- **Flexible Database Design**: A normalized database is often more flexible, allowing for easier modifications and updates to the structure and schema without extensive rewriting of queries.

### When to Denormalize:

**Denormalization** is the process of adding redundancy to a database to improve read performance. This often involves combining tables or adding duplicate data across tables to avoid complex joins.

**Use Cases for Denormalization:**

- **Improving Read Efficiency**: Denormalization can significantly reduce read latency for complex queries by reducing the need for joins and aggregations. This is particularly beneficial in read-heavy applications.
- **Simplifying Queries**: By consolidating data, denormalization can simplify query logic, making it easier to write and understand.
- **Scaling Read Operations**: In scenarios where the system demands high throughput for read operations, denormalization can help scale performance by spreading the load across duplicated data.

### Considerations:

- **Nature of the Application**: OLTP (Online Transaction Processing) systems, which focus on managing transactional data, often benefit from normalization to ensure fast, reliable transactions. OLAP (Online Analytical Processing) systems, designed for analysis and reporting, may lean towards denormalization for faster query responses.
- **Volume of Data**: Large datasets might require a balanced approach, where normalization is used to maintain integrity and reduce storage costs, while strategic denormalization is applied to frequently accessed data to improve read performance.
- **Hardware and Infrastructure**: Sometimes, the decision between normalization and denormalization can be influenced by the hardware and infrastructure available. Faster, more powerful servers with ample storage might lessen the need for denormalization.
- **Maintenance and Complexity**: Normalized designs can be more complex to query and maintain, while denormalized designs can lead to challenges in data consistency and integrity. 

In summary, the choice between normalization and denormalization does not strictly adhere to prioritizing write or read latencies alone; it also encompasses considerations around data integrity, application requirements, and the specific challenges posed by the data and its use cases. A hybrid approach, carefully evaluating when to normalize and when to denormalize, is often the most effective strategy.

# Query Optimizations

SQL query performance can be affected by various factors, making queries "expensive" in terms of resource consumption (CPU, memory), execution time, and impact on the database's overall workload. Here's a breakdown of common issues that can make a SQL query expensive, along with optimization strategies for each case:

### 1. Full Table Scans

- **Issue**: The database engine scans the entire table to find the relevant rows. This is resource-intensive, especially for large tables.
- **Optimization**: Use indexes to speed up searches. Indexes can dramatically reduce the need for full table scans by allowing the database engine to quickly locate the data.

### 2. Lack of Indexes or Inefficient Use of Indexes

- **Issue**: Without proper indexes, the database must perform more work to fulfill queries.
- **Optimization**: Create indexes on columns that are frequently used in WHERE clauses, JOIN conditions, or as part of an ORDER BY. Ensure that the indexes are not overly broad or numerous, as this can slow down write operations.

### 3. Inefficient Joins

- **Issue**: Joining tables without proper indexes, or joining large datasets, can be very costly.
- **Optimization**: Ensure that foreign keys and fields used in joins are indexed. Sometimes, rewriting the query to filter out unnecessary rows early in the join process can reduce the workload.

### 4. Selecting Unnecessary Columns

- **Issue**: Selecting more columns than needed, especially with `SELECT *`, can increase the amount of data that needs to be processed and transferred.
- **Optimization**: Specify only the needed columns in the SELECT statement.

### 5. Poorly Written Queries

- **Issue**: Nested subqueries, non-sargable expressions (search arguments that cannot use indexes efficiently), and complex calculations in the WHERE clause can degrade performance.
- **Optimization**: Rewrite queries to be more efficient. Avoid subqueries where possible by using JOINs or Common Table Expressions (CTEs). Ensure expressions are sargable.

### 6. Lack of Query Caching

- **Issue**: Repeatedly running the same costly queries without caching the results can waste resources.
- **Optimization**: Use query caching features where available. Some RDBMS systems automatically cache query results, but the implementation may vary.

### 7. Large Data Volumes

- **Issue**: As tables grow, operations on them become slower if not properly managed.
- **Optimization**: Regularly archive old data, partition large tables, and consider using summary tables for frequent aggregate queries.

### 8. Hardware Limitations

- **Issue**: Insufficient CPU, memory, or slow disk IO can bottleneck performance.
- **Optimization**: Upgrade hardware, or migrate to a more powerful server if possible. Also, consider cloud solutions where resources can be scaled according to demand.

### 9. Network Issues

- **Issue**: Network latency can affect the perceived performance of database queries, especially in distributed databases.
- **Optimization**: Optimize the network infrastructure if possible, or design the application to minimize the impact of network latency (e.g., by fetching data in bulk).

### 10. Concurrency and Locking Issues

- **Issue**: High levels of concurrency can lead to locking and blocking, making queries wait.
- **Optimization**: Optimize transaction scopes and durations. Use appropriate isolation levels to balance consistency and performance.

### 11. Inefficient Schema Design

- **Issue**: A poorly designed database schema can lead to redundant data storage and complex queries.
- **Optimization**: Normalize the database schema to eliminate redundancy where appropriate, and denormalize selectively for performance as needed.

### 12. Outdated Statistics

- **Issue**: The database's query planner relies on statistics about data distribution, which, if outdated, can lead to suboptimal query plans.
- **Optimization**: Regularly update statistics and consider manual updates after large data changes.

Optimizing SQL queries and database performance often involves a combination of these strategies, tailored to the specific characteristics and workload of the database system in question.

# Windowed Functions

Window functions, also known as analytic functions, are a powerful feature in SQL that allow you to perform calculations across a set of rows that are related to the current row. This is somewhat similar to aggregate functions, but while aggregate functions return a single result for each group, window functions do not cause rows to become grouped into a single output row — the rows retain their separate identities. Unlike standard aggregation, window functions also do not filter out rows from the result set but rather allow each row to remain visible and part of the output.

### Key Concepts

- **OVER() Clause**: This is what distinguishes a window function from other types of SQL functions. The `OVER()` clause defines the window or set of rows the function operates on. It can include `PARTITION BY`, `ORDER BY`, and `ROWS` or `RANGE` specifications.
  
- **PARTITION BY**: This divides the result set into partitions to which the window function is applied. If not specified, the function treats the whole result set as a single partition.
  
- **ORDER BY**: Within the `OVER()` clause, this orders the rows in each partition or the entire result set if `PARTITION BY` is not used.
  
- **ROWS/RANGE**: These clauses further define the set of rows in each partition to which the function is applied, based on their order.

### Examples of Window Functions

1. **ROW_NUMBER()**: Assigns a unique number to each row starting from 1. For rows that are duplicates, it arbitrarily assigns a rank.

    ```sql
    SELECT name, sales, ROW_NUMBER() OVER (ORDER BY sales DESC) AS rank
    FROM sales_records;
    ```

2. **RANK() and DENSE_RANK()**: Similar to `ROW_NUMBER()`, but for rows that have the same value, `RANK()` will assign the same rank, with gaps in the sequence for ties. `DENSE_RANK()` does the same but without gaps.

    ```sql
    SELECT name, sales, RANK() OVER (ORDER BY sales DESC) AS rank
    FROM sales_records;
    ```

3. **SUM(), AVG()**, and other aggregate functions can be used as window functions to compute running totals, averages, etc., within a partition.

    ```sql
    SELECT name, sales, SUM(sales) OVER (PARTITION BY department) AS department_sales
    FROM sales_records;
    ```

4. **LEAD() and LAG()**: These functions allow you to access data from the next row (LEAD) or previous row (LAG) in the result set, according to the order specified in the `OVER()` clause.

    ```sql
    SELECT name, sales, LAG(sales, 1) OVER (ORDER BY name) AS previous_sales
    FROM sales_records;
    ```

### Use Cases

- Calculating running totals, moving averages, or cumulative sums.
- Assigning row numbers or ranks to rows based on their order in the result set.
- Comparing each row with the previous or next row in some ordered result set.
- Distributing rows into ranked categories or percentiles.

Window functions provide a highly efficient way to perform complex analytics and calculations in SQL without having to resort to multiple queries or complex subqueries. They allow you to analyze data in ways that would be difficult or impossible with traditional SQL aggregates alone.

# Pivot and Unpivot

Pivoting and unpivoting are techniques used in SQL and other data manipulation environments to transform data formats, essentially rotating data to provide a different perspective or structure. These operations are especially useful in data analysis and reporting, allowing for more flexible data presentation and examination.

### Pivot

The pivot operation transforms rows of data into columns, effectively turning unique values from one column into multiple columns in the output. This is particularly useful when you want to see data spread across categories as column headers with corresponding values underneath, often used in summarizing or aggregating data.

**Purpose of Pivot:**
- To summarize and aggregate data across multiple categories.
- To transform data into a format that is more suitable for analysis and reporting.

**Example Scenario:**
Imagine you have sales data in a table with columns for `Date`, `Product`, and `Sales`. If you want to analyze the sales by product for each month, you can pivot the data so that each product becomes a column, each row represents a month, and the cells contain the sum of sales for each product-month combination.

**SQL Implementation:**
Although the implementation can vary between different SQL databases, the concept involves using an aggregate function along with a `PIVOT` clause or a combination of aggregate functions and `CASE` or `IF` statements in databases that do not support `PIVOT` directly.

### Unpivot

The unpivot operation is the inverse of pivot; it transforms columns into rows. This operation is useful when you need to normalize a data structure, converting columns that represent categories or groups into row entries, which can then be more easily processed or analyzed.

**Purpose of Unpivot:**
- To normalize data by transforming categories represented as columns back into row entries.
- To prepare data for operations or analyses that require a more normalized form.

**Example Scenario:**
Continuing with the sales data example, suppose now you have a table where each column represents a different product's sales, and each row represents a month. If you want to analyze the data in a more normalized form, such as running queries on sales irrespective of the product, you might unpivot the data so that you have a row for each product's sales per month, rather than separate columns.

**SQL Implementation:**
The implementation of unpivoting can involve the `UNPIVOT` clause in databases that support it or alternative methods such as using `CROSS APPLY` in SQL Server or a combination of `UNION ALL` and `SELECT` statements in databases without direct `UNPIVOT` support.

### Summary

- **Pivot**: Turns unique row values into column headers, often for aggregation.
- **Unpivot**: Converts columns into rows, effectively normalizing data that was spread across columns.

Both operations enhance data analysis and reporting capabilities by allowing for more dynamic data restructuring. The specific syntax and capabilities can vary by database system, so it's important to consult the documentation for the SQL dialect you're using.
