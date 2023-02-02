USE `level_2`;

ALTER TABLE `users`
DROP PRIMARY KEY,
ADD PRIMARY KEY pk_users (`id`, `username`);
