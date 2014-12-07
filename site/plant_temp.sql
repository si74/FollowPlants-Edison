-- phpMyAdmin SQL Dump
-- version 4.2.6deb1
-- http://www.phpmyadmin.net
--

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `follow_plant_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `plant_temp`
--

CREATE TABLE IF NOT EXISTS `plant_temp` (
`plant_temp_id` int(11) NOT NULL,
  `plant_temperature` double NOT NULL,
  `create_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `plant_temp`
--

INSERT INTO `plant_temp` (`plant_temp_id`, `plant_temperature`, `create_date`) VALUES
(1, 5, '2014-12-07 16:00:34'),
(2, 5, '2014-12-07 16:00:35'),
(3, 5, '2014-12-07 16:01:08'),
(4, 5, '2014-12-07 16:01:10'),
(5, 5, '2014-12-07 16:01:29'),
(6, 5, '2014-12-07 16:01:30'),
(7, 5.22, '2014-12-07 16:01:46'),
(8, 5.22, '2014-12-07 16:01:47'),
(9, 5.22, '2014-12-07 16:01:57'),
(10, 5.22, '2014-12-07 16:02:51');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `plant_temp`
--
ALTER TABLE `plant_temp`
 ADD PRIMARY KEY (`plant_temp_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `plant_temp`
--
ALTER TABLE `plant_temp`
MODIFY `plant_temp_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=11;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
