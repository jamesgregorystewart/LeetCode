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
