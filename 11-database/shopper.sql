-- DATABASE
CREATE DATABASE shopper_db;
DROP DATABASE shopper_db;

CREATE DATABASE `shopper_db` DEFAULT CHARACTER SET utf8;

-- TABLE
CREATE TABLE product (
 id int(11) NOT NULL AUTO_INCREMENT,
 product_name varchar(250) DEFAULT NULL,
 unit_price float(11,2) DEFAULT 0.00,
 PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE product
MODIFY product_name VARCHAR(500);

ALTER TABLE product
ADD sku varchar(50) DEFAULT NULL AFTER product_name,
ADD description VARCHAR(1000) AFTER sku;

ALTER TABLE product
DROP description;

DROP TABLE product;

-- INSERT
INSERT INTO product (product_name, unit_price, sku, quantity)
VALUES ("หม้อทอดไร้นำ้มัน", 2900, "OL-0001", 10);

INSERT INTO product (product_name, unit_price, sku, quantity)
VALUES
("เก้าอี้นวด", 8900, "OL-0002", 12),
("พัดลมไฟฟ้า", 1900, "OL-0003", 1);

-- SELECT
select * from product

select sku, product_name, quantity, unit_price from product

select sku, product_name, quantity, unit_price from product
where unit_price > 4000 

select sku, product_name, quantity, unit_price from product
where unit_price > 4000 and quantity > 0

select sku, product_name, quantity, unit_price from product
where unit_price > 4000 or quantity > 10

-- UPDATE
UPDATE product
SET product_name = "เก้าอี้นวดไฟฟ้า รุ่นใหม่", quantity = 5
WHERE sku = "OL-0002";

UPDATE product
SET unit_price = 3500
WHERE unit_price < 3000;

-- DELETE
DELETE FROM product WHERE quantity < 3 ;
