CREATE TABLE `user_registration` (
  `user_name` varchar(10) PRIMARY KEY,
  `password` varchar(20) NOT NULL,
  `security_que_1` text NOT NULL,
  `pref_lang_name` varchar(50) NOT NULL,
  `permanent_address` text NOT NULL,
  `temp_address` text,
  `first_name` varchar(200) NOT NULL,
  `last_name` varchar(200),
  `middle_name` varchar(200),
  `occupation` varchar(50),
  `email` varchar(200),
  `phone_number` varchar(200) NOT NULL,
  `telephone_number` varchar(200) NOT NULL,
  `nationality` varchar(200) NOT NULL,
  `aadhaar_number` int NOT NULL
);

CREATE TABLE `user_existing_login` (
  `username` varchar(10) PRIMARY KEY,
  `password` varchar(20)
);

CREATE TABLE `agent_login` (
  `agent_id` int PRIMARY KEY,
  `agent_name` varchar(20) NOT NULL,
  `agent_reg_no` varchar(200) NOT NULL,
  `password` varchar(20) NOT NULL,
  `agent_type` varchar(20) NOT NULL
);

CREATE TABLE `user_enquiry` (
  `source` varchar(20) NOT NULL,
  `destination` varchar(20) NOT NULL,
  `via` varchar(20) NOT NULL,
  `boarding_date` date,
  `class` varchar(20) NOT NULL,
  `category` varchar(20) NOT NULL,
  `flexibility_date` boolean
);

CREATE TABLE `route_table` (
  `route_id` int PRIMARY KEY NOT NULL,
  `station_id` int NOT NULL,
  `distance` int NOT NULL
);

CREATE TABLE `time` (
  `train_id` int NOT NULL,
  `arrival_time` time NOT NULL,
  `departure_time` time NOT NULL,
  `halt_time` time NOT NULL,
  `day` int NOT NULL
);

CREATE TABLE `train_details` (
  `train_id` int PRIMARY KEY,
  `train_name` varchar(20) NOT NULL,
  `train_type` varchar(20) NOT NULL,
  `source` varchar(20) NOT NULL,
  `destination` varchar(20) NOT NULL,
  `route_id` int NOT NULL,
  `coach_id` int NOT NULL,
  `arrival_time` time,
  `depart_time` time NOT NULL,
  `availability_days` varchar(20) NOT NULL
);

CREATE TABLE `station` (
  `station_id` int PRIMARY KEY NOT NULL,
  `station_code` varchar(20) NOT NULL,
  `station_name` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pincode` int NOT NULL
);

CREATE TABLE `seat_availability` (
  `train_id` int NOT NULL,
  `date_journey` date NOT NULL,
  `seats` int NOT NULL,
  `category` varchar(20) NOT NULL
);

CREATE TABLE `location` (
  `train_id` int NOT NULL,
  `current_station_id` int NOT NULL,
  `next_station_id` int NOT NULL,
  `speed` int NOT NULL
);

CREATE TABLE `ticket` (
  `ticket_no` int PRIMARY KEY,
  `passenger_name` varchar(20) NOT NULL,
  `pnr_no` int NOT NULL,
  `boarding_station_id` int,
  `dropping_station_id` int,
  `insurance_details` boolean,
  `class` varchar(20) NOT NULL,
  `status_type` varchar(10) NOT NULL,
  `aadhar_no` int NOT NULL,
  `booking_id` int NOT NULL
);

CREATE TABLE `mode_table` (
  `mode_id` int PRIMARY KEY,
  `mode_name` varchar(20)
);

CREATE TABLE `booking` (
  `booking_id` int PRIMARY KEY,
  `user_id` int NOT NULL,
  `no_persons` int NOT NULL
);

CREATE TABLE `payment` (
  `tranx_id` int PRIMARY KEY,
  `acc_no` int NOT NULL,
  `booking_id` int NOT NULL,
  `mode_id` int,
  `status` varchar(50),
  `pay_date` datetime
);

CREATE TABLE `passenger` (
  `pass_id` int PRIMARY KEY,
  `booking_id` int NOT NULL,
  `pass_name` varchar(20),
  `age` int,
  `gender` varchar(10),
  `seat_preference` varchar(20),
  `quota` varchar(20)
);

CREATE TABLE `fare` (
  `booking_id` int NOT NULL,
  `fare` decimal NOT NULL,
  `discount` decimal,
  `total_cost` decimal NOT NULL
);

CREATE TABLE `train_cancellation` (
  `train_id` int NOT NULL,
  `message` text,
  `rescheduled` boolean
);

CREATE TABLE `ticket_cancellation` (
  `booking_id` int NOT NULL,
  `ticket_no` int NOT NULL,
  `refund_status` text
);

ALTER TABLE `user_existing_login` ADD FOREIGN KEY (`username`) REFERENCES `user_registration` (`user_name`);

ALTER TABLE `route_table` ADD FOREIGN KEY (`station_id`) REFERENCES `station` (`station_id`);

ALTER TABLE `train_details` ADD FOREIGN KEY (`route_id`) REFERENCES `route_table` (`route_id`);

ALTER TABLE `seat_availability` ADD FOREIGN KEY (`train_id`) REFERENCES `train_details` (`train_id`);

ALTER TABLE `location` ADD FOREIGN KEY (`train_id`) REFERENCES `train_details` (`train_id`);

ALTER TABLE `payment` ADD FOREIGN KEY (`mode_id`) REFERENCES `mode_table` (`mode_id`);

ALTER TABLE `payment` ADD FOREIGN KEY (`booking_id`) REFERENCES `booking` (`booking_id`);

ALTER TABLE `passenger` ADD FOREIGN KEY (`booking_id`) REFERENCES `booking` (`booking_id`);

ALTER TABLE `fare` ADD FOREIGN KEY (`booking_id`) REFERENCES `booking` (`booking_id`);

ALTER TABLE `train_cancellation` ADD FOREIGN KEY (`train_id`) REFERENCES `train_details` (`train_id`);

ALTER TABLE `ticket_cancellation` ADD FOREIGN KEY (`booking_id`) REFERENCES `booking` (`booking_id`);

ALTER TABLE `ticket_cancellation` ADD FOREIGN KEY (`ticket_no`) REFERENCES `ticket` (`ticket_no`);

ALTER TABLE `ticket` ADD FOREIGN KEY (`booking_id`) REFERENCES `booking` (`booking_id`);
