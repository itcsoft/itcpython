USE sakila;

SELECT city.city, country.country
FROM city
    INNER JOIN country 
    ON city.country_id = country.country_id
LIMIT 10;