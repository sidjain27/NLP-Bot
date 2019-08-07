-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 13, 2019 at 02:11 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `question set`
--

-- --------------------------------------------------------

--
-- Table structure for table `quest`
--

CREATE TABLE `quest` (
  `srno` int(10) NOT NULL,
  `question` text NOT NULL,
  `userans` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `quest`
--

INSERT INTO `quest` (`srno`, `question`, `userans`) VALUES
(1, 'What is your First name?\r\n\r\n<Provide your answer in a single word\r\nEg: John>', 'Abcd'),
(2, 'Are you a fresher?\r\n\r\n<Provide your answer in Yes/No format\r\nEg: Yes>', 'no'),
(3, 'How many years of experience do you have?\r\n<Mention your answer in years and months only\r\nEg: 3 years and 7 months>', '3 months'),
(4, 'Bot: Mention your previous experiences.\r\n<Enter your experience in the foll format:\r\nCompany Name as Designation for Time period\r\n\r\nEg:\r\nNextNT as Intern for 1 Year>', 'TechM as developer for 3 months'),
(5, 'Why do you want to join our company?\r\n\r\n<Answer directly to the point in not more than 200 words>', 'because im interested'),
(6, 'Where do you see yourself 5 years from now?', 'somewhere'),
(7, 'Would you like to add anything to your information or leave a message for the recruiter?\r\n<If you wish to leave a message send it, else type No\r\nEg: No >', 'no');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
