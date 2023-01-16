-- Visits Table
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | visit_id    | int     |
-- | customer_id | int     |
-- +-------------+---------+
-- visit_id is the primary key for this table.
-- This table contains information about the customers who visited the mall.

-- Transactions Table
-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | transaction_id | int     |
-- | visit_id       | int     |
-- | amount         | int     |
-- +----------------+---------+
-- transaction_id is the primary key for this table.
-- This table contains information about the transactions made during the visit_id.


-- Questions
-- Write an SQL query to find the IDs of the users who visited without making any transactions 
-- and the number of times they made these types of visits.

-- OUTPUT -> customer_id | count_no_visits

-- Approach
1. left join visits and transactions on visit_id
2. group by customer_id | select customer_id and count(visit_id)
3. where visit_id is NULL
4. group by customer_id

-- SOLUTION
SELECT v.customer_id, count(v.visit_id) as count_no_trans
FROM Visits v
    LEFT JOIN Transactions t
    ON v.visit_id = t.visit_id
WHERE t.visit_id is null
GROUP BY v.customer_id 