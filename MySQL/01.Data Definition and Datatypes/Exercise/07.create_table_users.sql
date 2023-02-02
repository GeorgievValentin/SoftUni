USE `level_2`;

CREATE TABLE `users` (
	`id` BIGINT PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(30) NOT NULL ,
    `password` VARCHAR(26) NOT NULL,
    `profile_picture` BLOB,
    `last_login_time` TIME,
    `is_deleted` BOOLEAN
);

INSERT INTO `users` (`username`, `password`,  `last_login_time`, `is_deleted`)
VALUES
	("Stefan", "1234", TIME(NOW()), false),
	("Kiril", "qwer", TIME(NOW()), false),
	("Peter", "asdf", TIME(NOW()), false),
	("Stefka", "4r5t", TIME(NOW()), true),
	("Gergana", "0987", TIME("19:30:10"), false);