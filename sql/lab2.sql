-- SELECT * FROM country
-- WHERE country.country LIKE 'U%';


-- SELECT COUNT(*) FROM country;
-- SELECT COUNT(*) FROM actor;

-- SELECT COUNT(*) FROM customer;


-- Получаем клиентов по id между 54 и 60
-- SELECT * FROM customer
-- WHERE customer_id BETWEEN 54 AND 60;

-- Получаем клиентов по конкретному id IN
SELECT * FROM customer
    WHERE customer_id IN (100, 300, 199);

