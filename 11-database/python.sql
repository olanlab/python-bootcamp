-- phpMyAdmin SQL Dump
-- version 4.9.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 27, 2023 at 07:03 AM
-- Server version: 5.6.51
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python`
--

-- --------------------------------------------------------

--
-- Table structure for table `budgets`
--

CREATE TABLE `budgets` (
  `id` int(11) NOT NULL,
  `created_date` datetime NOT NULL,
  `title` varchar(200) NOT NULL,
  `type` varchar(1) NOT NULL,
  `amount` float NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `budgets`
--

INSERT INTO `budgets` (`id`, `created_date`, `title`, `type`, `amount`, `user_id`) VALUES
(17, '2023-05-21 16:50:06', 'ค่าข้าว', 'e', 100, NULL),
(25, '2023-05-24 15:32:22', 'ค่าโบนัส', 'r', 10000, NULL),
(26, '2023-05-24 15:32:44', 'ผ่อนมือถือ 1/10', 'e', 2000, NULL),
(27, '2023-05-24 15:33:03', 'ค่ากินข้าว', 'e', 500, NULL),
(29, '2023-05-24 16:21:31', 'ค่าทำงานบ้าน', 'e', 1500, NULL),
(30, '2023-05-24 16:21:44', 'เงินเดือน', 'r', 21500, NULL),
(32, '2023-05-24 16:22:12', 'ค่าอินเตอร์เนต', 'e', 900, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `milkteas`
--

CREATE TABLE `milkteas` (
  `id` int(11) NOT NULL,
  `created_date` datetime NOT NULL,
  `glass` int(11) NOT NULL,
  `total` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `milkteas`
--

INSERT INTO `milkteas` (`id`, `created_date`, `glass`, `total`) VALUES
(1, '2023-04-24 00:00:00', 1, 60),
(2, '2023-04-24 00:00:00', 2, 150),
(3, '2023-04-24 00:00:00', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `sex` varchar(1) DEFAULT NULL,
  `gpa` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `firstname`, `lastname`, `sex`, `gpa`) VALUES
(1, 'Olan', 'S.', 'M', 3.5),
(2, 'Seen', 'V.', 'F', 3),
(5, 'Jame', 'J.', 'M', 2.5),
(6, 'Jojo', 'J.', 'M', 4),
(7, 'Jee', 'F.', 'F', 2.5);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `firstname`, `lastname`, `email`) VALUES
(1, 'olan', '1234', 'Olan', 'Samritjiarapon', 'olan@olanlab.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `budgets`
--
ALTER TABLE `budgets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_idx` (`user_id`);

--
-- Indexes for table `milkteas`
--
ALTER TABLE `milkteas`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `budgets`
--
ALTER TABLE `budgets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `milkteas`
--
ALTER TABLE `milkteas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `budgets`
--
ALTER TABLE `budgets`
  ADD CONSTRAINT `users` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
