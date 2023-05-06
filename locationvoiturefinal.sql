-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 07, 2023 at 12:42 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `locationvoiture`
--

-- --------------------------------------------------------

--
-- Table structure for table `reservation`
--

CREATE TABLE `reservation` (
  `id_res` int(10) NOT NULL,
  `nom_complet` varchar(50) NOT NULL,
  `num_tel` int(50) NOT NULL,
  `cin` varchar(50) NOT NULL,
  `numero_permis` int(50) NOT NULL,
  `voiture` varchar(50) NOT NULL,
  `datedebut` date NOT NULL,
  `datefin` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservation`
--

INSERT INTO `reservation` (`id_res`, `nom_complet`, `num_tel`, `cin`, `numero_permis`, `voiture`, `datedebut`, `datefin`) VALUES
(1, 'amine amine', 147, '0147', 147, 'mercedes', '0000-00-00', '0000-00-00'),
(2, 'safaa safaa', 258, '0258', 8520, 'bmw', '0000-00-00', '0000-00-00'),
(3, 'wiam wiam', 147, '0147', 147, 'mercedes', '0000-00-00', '0000-00-00'),
(4, 'asmaa', 258, '0258', 8520, 'bmw', '0000-00-00', '0000-00-00'),
(5, 'salma ', 35345345, '3453453', 3534534, 'mercedes', '0000-00-00', '0000-00-00');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(10) NOT NULL,
  `nom_complet` varchar(50) NOT NULL,
  `cin` varchar(10) NOT NULL,
  `num_tel` int(20) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `num_permis` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `nom_complet`, `cin`, `num_tel`, `username`, `password`, `email`, `num_permis`) VALUES
(20, 'admin', '111111', 1111111, 'admin', 'admin', 'admin@gmail.com', 1111111),
(21, 'user', '22222', 22222, 'user', 'user', 'user@gmail.com', 222222);

-- --------------------------------------------------------

--
-- Table structure for table `voiture`
--

CREATE TABLE `voiture` (
  `id_voiture` int(10) NOT NULL,
  `marque` varchar(20) NOT NULL,
  `modele` varchar(20) NOT NULL,
  `type_carburant` varchar(20) NOT NULL,
  `nb_places` int(20) NOT NULL,
  `transmission` int(20) NOT NULL,
  `prix_location` int(20) NOT NULL,
  `disponibilité` tinyint(1) NOT NULL,
  `image` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `voiture`
--

INSERT INTO `voiture` (`id_voiture`, `marque`, `modele`, `type_carburant`, `nb_places`, `transmission`, `prix_location`, `disponibilité`, `image`) VALUES
(66, 'marque', 'modele', 'typeCarburant', 8, 69, 700, 1, 'image.png'),
(67, 'mercedes', '2019', 'res', 3, 89, 300, 1, 'img.png'),
(68, 'Toyota', 'Corolla', 'Essence', 5, 0, 50, 1, 'images/car1.jpg'),
(69, 'renau', 'r4', 'Essence', 5, 0, 50, 1, 'images/car1.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`id_res`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `voiture`
--
ALTER TABLE `voiture`
  ADD PRIMARY KEY (`id_voiture`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `reservation`
--
ALTER TABLE `reservation`
  MODIFY `id_res` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `voiture`
--
ALTER TABLE `voiture`
  MODIFY `id_voiture` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
