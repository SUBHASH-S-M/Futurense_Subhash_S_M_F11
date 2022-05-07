
show databases;
use world;
show tables;

-- inner join
select * from city
inner join country on city.CountryCode=country.Code
inner join countrylanguage clang on country.Code=clang.CountryCode;
-- aggregate functions
-- Max
select Name,CountryCode,Population from city
where population=(select max(population) from city );

-- Min
select Name,CountryCode,Population from city
where population=(select min(population) from city );
-- sum
select city.CountryCode,country.Name,sum(city.Population) from city
inner join country on city.CountryCode=country.Code
group by country.Code,country.Name
order by 3 desc;
-- count
select city.CountryCode,country.Name,sum(city.Population) as Country_Population,count(city.ID) as Total_cities from city
inner join country on city.CountryCode=country.Code
group by country.Code,country.Name
order by 4 desc;
-- avg
select city.CountryCode,country.Name,sum(city.Population) as Country_Population,count(city.ID) as Total_cities,avg(city.Population) as Avg_Population from city
inner join country on city.CountryCode=country.Code
group by country.Code,country.Name
order by 5 desc,4;

-- sub queries
-- city with max population within its country
select Name,Population,CountryCode from city c1
where c1.Population=(select max(c2.Population) from city c2 where c2.CountryCode=c1.CountryCode);
/*
 city with population below the avergae should be displayed low population country and
above the avg populaiton should be dispalyes as high populaiton country
*/
select city.Name,city.Population,city.CountryCode,
CASE
    WHEN city.Population > (select avg(ci.Population) from city ci) THEN "Good Population"
    ELSE "Low than Avg"
END as Pop_Status
from city;

-- select * from city where District like 'a%';
select District,char_length(District) from city;
select District,character_length(District) from city;

select District,lcase(District) from city;

select District,ucase(District) from city;

-- REPLACE(str,from_str,to_str)
select REPLACE(District,"bol","alob") from city;

-- REVERSE(str)
select REVERSE(District) from city;
SELECT RTRIM('barbar   '); -- removes righ side space
SELECT LTRIM('    barbar'); -- removes left side space
SELECT TRIM('   barbar   '); -- removes space from both side
SELECT CONCAT(District," ",Population) from city;
SELECT CONCAT_WS(',',District,Population) from city;
SELECT SUBSTRING(District FROM 1 FOR 3) from city;






