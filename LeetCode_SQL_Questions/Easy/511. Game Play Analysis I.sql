-- SQL SCHEMA

-- Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int)
-- Truncate table Activity
-- insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5')
-- insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-05-02', '6')
-- insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1')
-- insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0')
-- insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5')

-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | player_id    | int     |
-- | device_id    | int     |
-- | event_date   | date    |
-- | games_played | int     |
-- +--------------+---------+
-- (player_id, event_date) is the primary key of this table.
-- This table shows the activity of players of some games.
-- Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.

-- Question
-- Write an SQL query to report the first login date for each player.
-- Return the result table in any order.

-- Input: 
-- Activity table:
-- +-----------+-----------+------------+--------------+
-- | player_id | device_id | event_date | games_played |
-- +-----------+-----------+------------+--------------+
-- | 1         | 2         | 2016-03-01 | 5            |
-- | 1         | 2         | 2016-05-02 | 6            |
-- | 2         | 3         | 2017-06-25 | 1            |
-- | 3         | 1         | 2016-03-02 | 0            |
-- | 3         | 4         | 2018-07-03 | 5            |
-- +-----------+-----------+------------+--------------+
-- Output: 
-- +-----------+-------------+
-- | player_id | first_login |
-- +-----------+-------------+
-- | 1         | 2016-03-01  |
-- | 2         | 2017-06-25  |
-- | 3         | 2016-03-02  |
-- +-----------+-------------+

------ Approach
-- 1. output - player_id | first_login
-- 2. group by player_id, where event_date is min

SELECT player_id, MIN(event_date) as first_login
FROM Activity
GROUP BY player_id