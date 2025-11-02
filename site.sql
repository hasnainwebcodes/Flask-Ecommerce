-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308
-- Generation Time: Nov 02, 2025 at 08:41 AM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 7.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `site`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `no` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `message` varchar(500) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`no`, `name`, `email`, `phone`, `message`, `date`) VALUES
(1, 'hasnain raza vighio', 'vighiorazahasnain@gm', '03413253785', 'Hi this is a message just for testing the site.', '2025-10-12 06:36:58');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `amount` int(11) DEFAULT NULL,
  `status` varchar(12) DEFAULT NULL,
  `items` text,
  `itemsize` varchar(1) DEFAULT NULL,
  `cod` varchar(5) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `madeat` datetime DEFAULT NULL,
  `adress` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `username`, `amount`, `status`, `items`, `itemsize`, `cod`, `quantity`, `madeat`, `adress`) VALUES
(2, 'ME', 10, 'pending', 'hasnain raza vighio', 'L', 'False', 1, '2025-10-25 08:37:19', 'Our'),
(3, 'Hasnain', 30, 'pending', 'hasnain raza vighio', 'L', 'False', 3, '2025-10-26 05:38:27', 'Liaquat'),
(4, 'Hasnain', 180000, 'pending', 'Ok', 'L', 'False', 6, '2025-11-01 07:59:39', 'Our'),
(5, 'Hasnain', 90000, 'pending', 'Ok', 'M', 'False', 3, '2025-11-01 08:13:18', 'Our'),
(6, 'ME', 90000, 'pending', 'Ok', 'L', 'False', 3, '2025-11-01 08:25:32', 'Liaquat'),
(7, 'Hasnain', 90000, 'pending', 'Ok', 'L', 'False', 3, '2025-11-01 08:47:34', 'Liaquat'),
(8, 'Hasnain', 90000, 'pending', 'Ok', 'L', 'False', 3, '2025-11-01 08:48:15', 'Liaquat'),
(9, 'Hasnain', 180000, 'pending', 'Ok', 'M', 'False', 6, '2025-11-01 08:51:47', 'Liaquat'),
(10, 'Hasnain', 30000, 'pending', 'Ok', 'L', 'False', 1, '2025-11-01 09:42:17', 'Liaquat');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `description` text NOT NULL,
  `price` int(11) NOT NULL,
  `stock` int(11) DEFAULT NULL,
  `brand` varchar(20) NOT NULL,
  `image1` varchar(30) NOT NULL,
  `image2` varchar(30) NOT NULL,
  `image3` varchar(30) NOT NULL,
  `image4` varchar(30) NOT NULL,
  `image5` varchar(30) NOT NULL,
  `image6` varchar(30) NOT NULL,
  `image7` varchar(30) NOT NULL,
  `category` varchar(10) NOT NULL,
  `specification` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`, `description`, `price`, `stock`, `brand`, `image1`, `image2`, `image3`, `image4`, `image5`, `image6`, `image7`, `category`, `specification`) VALUES
(1, 'Sports', '   This is a test production involved just for testing you can see it order it and check the site for free. Note No real orders will be placed.    ', 25, 4, 'Nike', 'banner_img_01.jpg', 'banner_img_02.jpg', 'banner_img_03.jpg', 'brand_01.png', 'brand_02.png', 'brand_03.png', 'brand_04.png', 'Men', '   This is a test production involved just for testing you can see it order it and check the site for free. Note No real orders will be placed. '),
(2, 'Stylish Watch', 'This is a test production involved just for testing you can see it order it and check the site for free. Note No real orders will be placed. ', 10, 5, 'Rolex', 'category_img_01.jpg', 'feature_prod_02.jpg', 'category_img_02.jpg', 'category_img_03.jpg', 'feature_prod_01.jpg', 'feature_prod_03.jpg', 'category_img_01.jpg', 'Men', 'This is a test production involved just for testing you can see it order it and check the site for free. Note No real orders will be placed. '),
(3, 'Active', '   This is a test production involved just for testing you can see it order it and check the site for free. Note No real orders will be placed.    ', 10, 10, 'Easy', 'product_single_07.jpg', 'product_single_01.jpg', 'product_single_02.jpg', 'product_single_03.jpg', 'product-single_04.jpg', 'product_single_05.jpg', 'product_single_06.jpg', 'Women', '   This is a test production involved just for testing you can see it order it and check the site for free. Note No real orders will be placed. '),
(4, 'Active Wear', 'This is a test production involved just for testing you can see it order it and check the site for free. Note No real orders will be placed. ', 25, 10, 'Yoga Wear', 'product_single_03.jpg', 'product_single_04.jpg', 'product_single_05.jpg', 'product_single_06.jpg', 'product-single_07.jpg', 'product_single_08.jpg', 'product_single_09.jpg', 'Women', 'This is a test production involved just for testing you can see it order it and check the site for free. Note No real orders will be placed. '),
(5, 'Glasses', 'This is a test production involved just for testing you can see it order it and check the site for free. Note No real orders will be placed. ', 10, 1000, 'Nike', 'shop_01.jpg', 'shop_02.jpg', 'shop_03.jpg', 'category_img_03.jpg', 'shop_04.jpg', 'shop_05.jpg', 'shop_06.jpg', 'Child', 'This is a test production involved just for testing you can see it order it and check the site for free. Note No real orders will be placed. '),
(6, 'Coat', 'This is a test production involved just for testing you can see it order it and check the site for free. Note No real orders will be placed. ', 50, 10, 'H&M', 'shop_07.jpg', 'shop_08.jpg', 'shop_03.jpg', 'shop_10.jpg', 'shop_11.jpg', 'shop_09.jpg', 'shop_07.jpg', 'Men', 'This is a test production involved just for testing you can see it order it and check the site for free. Note No real orders will be placed. '),
(7, 'Water Cooler', 'This is a test production involved just for testing you can see it order it and check the site for free. Note No real orders will be placed. ', 10, 2, 'Levis', 'feature_prod_01.jpg', 'banner_img_02.jpg', 'product_single_02.jpg', 'brand_01.png', 'shop_11.jpg', 'feature_prod_03.jpg', 'category_img_01.jpg', 'Child', 'This is a test production involved just for testing you can see it order it and check the site for free. Note No real orders will be placed. ');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(40) NOT NULL,
  `role` varchar(5) NOT NULL,
  `password` varchar(80) NOT NULL,
  `phone` varchar(12) DEFAULT NULL,
  `since` datetime DEFAULT NULL,
  `address` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `role`, `password`, `phone`, `since`, `address`) VALUES
(1, 'this', 'that@gmail.com', 'user', 'scrypt:32768:8:1$3h6sLG7CmOgzb7w2$53c14d652adece87e00132edf98351d8b597a0e55596f3', '03413253785', '2025-10-28 14:40:45', NULL),
(2, 'that', 'th@gmail.com', 'user', '$2b$12$qwoY64ug4bkjvkABlIi.z.UX03EPcbtbIcc0ZBhr/AD9gC94GTVMi', '03413253785', '2025-10-28 14:47:15', NULL),
(3, 'aalia', 'aalia@gmail.com', 'user', '$2b$12$8BlbPTaVqxxD6kEEbJvgNeL39GBlwzuYjkmySOivkaIT0qe32agdq', '03413253785', '2025-10-29 09:47:53', NULL),
(4, 'waqas', 'vighiorazahasnain@gmail.com.com', 'user', '$2b$12$jls4D0uvnyaZf7FAWXqAK.euG0Y3ifbTfhFUA8lY3s74d.9n7hsOa', '03413253785', '2025-10-29 10:57:41', NULL),
(5, 'hasnain', 'vi@gmial.com', 'admin', '$2b$12$tWN59Jq3XtEESfZm5lpfFu4YDmbAWebdvYgZUPe5WtLLo1grnBnlS', '03413253785', '2025-10-30 10:12:57', NULL),
(6, 'this', 'tht@gmail.com', 'user', '$2b$12$BHPDs5VGG0oEFu7sAnRAVe0M0CJ46w6vn05Xh98f.yaViaA8SH8Aq', '03413253785', '2025-10-31 10:01:17', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
