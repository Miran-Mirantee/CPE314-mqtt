CREATE DATABASE cpe314_database;
CREATE TABLE `data` (
  `Node` varchar(4) NOT NULL,
  `Time` datetime NOT NULL,
  `Humidity` varchar(200) NOT NULL,
  `Temperature` varchar(200) NOT NULL,
  `ThermalArray` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;