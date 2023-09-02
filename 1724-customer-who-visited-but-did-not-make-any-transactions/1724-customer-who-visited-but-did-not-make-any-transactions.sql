# Write your MySQL query statement below
SELECT customer_id, Count(Visits.visit_id) AS count_no_trans
from Visits
Left Join Transactions ON Visits.visit_id = Transactions.visit_id
Where Transactions.transaction_id is NULL
Group by Visits.customer_id;