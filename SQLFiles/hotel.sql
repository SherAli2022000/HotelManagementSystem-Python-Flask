-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 19, 2021 at 04:03 PM
-- Server version: 8.0.21
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel`
--
CREATE DATABASE IF NOT EXISTS `hotel` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `hotel`;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `customer_id` int NOT NULL,
  `password` varchar(250) NOT NULL,
  `name` varchar(250) NOT NULL,
  `age` int NOT NULL,
  `Address` varchar(250) NOT NULL,
  `phone_no` varchar(250) NOT NULL,
  `room_id` int NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `password`, `name`, `age`, `Address`, `phone_no`, `room_id`) VALUES
(2, 'abc', 'abc', 20, 'Rawalpindi', '031232433234', -1);

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE IF NOT EXISTS `employee` (
  `emp_id` int NOT NULL,
  `emp_name` varchar(250) NOT NULL,
  `emp_address` varchar(250) NOT NULL,
  `emp_phone` varchar(250) NOT NULL,
  `emp_salary` int NOT NULL,
  `emp_jobtype` varchar(250) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`emp_id`, `emp_name`, `emp_address`, `emp_phone`, `emp_salary`, `emp_jobtype`) VALUES
(1, 'Faizan', 'Rawalpindi', '0312523213', 20000, 'Cleaner');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
CREATE TABLE IF NOT EXISTS `payment` (
  `payment_id` int NOT NULL,
  `cust_id` int NOT NULL,
  `cust_name` varchar(250) DEFAULT NULL,
  `total` int NOT NULL,
  `Description` varchar(250) NOT NULL,
  `status` varchar(250) NOT NULL,
  `DateAdd` varchar(250) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
CREATE TABLE IF NOT EXISTS `reservation` (
  `reservation_ID` int NOT NULL,
  `room_ID` int NOT NULL,
  `cust_ID` int NOT NULL,
  `date_Added` varchar(250) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
CREATE TABLE IF NOT EXISTS `room` (
  `room_id` int NOT NULL AUTO_INCREMENT,
  `room_type` varchar(250) NOT NULL,
  `room_price` int NOT NULL,
  `room_description` varchar(250) NOT NULL,
  `room_floor` int NOT NULL,
  `room_wing` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  PRIMARY KEY (`room_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`room_id`, `room_type`, `room_price`, `room_description`, `room_floor`, `room_wing`, `Status`) VALUES
(1, 'Suite', 5000, 'Spacious and clean', 3, 'Right', 'True'),
(2, 'Normal', 3000, 'Window room with beautiful view', 3, 'Left', 'False'),
(3, 'Normal', 1000, 'clean', 3, 'Right', 'False'),
(4, 'Normal', 3000, 'v Good', 4, 'Right', 'False'),
(5, 'Suite', 20000, 'Best', 5, 'Right', 'False');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
