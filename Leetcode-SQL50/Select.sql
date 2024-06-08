-------------------------------------------------
-- 1757. Recyclable and Low Fat Products
-- Write your MySQL query statement below
SELECT product_id FROM Products
WHERE low_fats = 'Y'
AND recyclable = 'Y';

-------------------------------------------------

-- 584. Find Customer Referee
-- Write your MySQL query statement below
SELECT name FROM Customer
WHERE referee_id != 2
OR referee_id IS NULL;

-------------------------------------------------

-- 1148. Article Views I
-- Write your MySQL query statement below
SELECT DISTINCT author_id as id FROM Views
WHERE author_id = viewer_id
ORDER BY author_id ASC;

-------------------------------------------------

-- 1683. Invalid Tweets
-- Write your MySQL query statement below
# Write your MySQL query statement below
SELECT tweet_id FROM Tweets
WHERE LENGTH(content) > 15;

-------------------------------------------------
