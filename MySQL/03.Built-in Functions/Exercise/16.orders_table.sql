USE `orders`;

SELECT `product_name`, `order_date`,
ADDDATE(`order_date`, interval 3 day) as pay_due, 
ADDDATE(`order_date`, interval 1 month) as deliver_due
FROM `orders`;