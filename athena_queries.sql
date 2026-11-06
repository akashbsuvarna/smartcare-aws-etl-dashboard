SELECT department, COUNT(*) as visits, SUM(fees) as total_fees
FROM smartcare_cleaned GROUP BY department;

SELECT gender, COUNT(*) as total
FROM smartcare_cleaned GROUP BY gender;