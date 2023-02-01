ALTER TABLE `products` ADD CONSTRAINT kf__category_id__products_categoty_id
FOREIGN KEY `products`(`category_id`)
REFERENCES `categories`(`id`);