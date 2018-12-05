-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Nov 28, 2018 at 11:39 AM
-- Server version: 10.1.13-MariaDB
-- PHP Version: 5.6.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sistem_absensi`
--

-- --------------------------------------------------------

--
-- Table structure for table `absensi`
--

CREATE TABLE `absensi` (
  `id_absensi` int(11) NOT NULL,
  `nip` int(11) NOT NULL,
  `waktu_masuk` varchar(20) NOT NULL,
  `waktu_pulang` varchar(20) NOT NULL,
  `tanggal` varchar(20) NOT NULL,
  `foto_url` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `absensi`
--

INSERT INTO `absensi` (`id_absensi`, `nip`, `waktu_masuk`, `waktu_pulang`, `tanggal`, `foto_url`) VALUES
(1, 180201, '17:25:27', '', '2018-11-28', 'http://127.0.0.1:5000/static/img/img_180201.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `pegawai`
--

CREATE TABLE `pegawai` (
  `nip` int(11) NOT NULL,
  `nama` varchar(60) NOT NULL,
  `alamat` varchar(40) NOT NULL,
  `jabatan` text NOT NULL,
  `desk_kerja` text NOT NULL,
  `jenis_kelamin` varchar(2) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pegawai`
--

INSERT INTO `pegawai` (`nip`, `nama`, `alamat`, `jabatan`, `desk_kerja`, `jenis_kelamin`, `email`, `password`) VALUES
(180201, 'Safif Rafi Efendi', 'Paciran -Lamongan', 'Developer', 'Fullstack developer pada pembuatan aplikasi perusahaan, menciptakan aplikasi yang  sesuai dengan kebutuhan user dan perusahaan, baik web ataupun mobile.', 'L', 'esafif637@gmail.com', '82f69976379e71c77074377db3ea618c'),
(180202, 'Ichsan', 'Palembang', 'AI Engineer', 'Ai engineer, membuat model AI yang di pakai untuk kebutuhan aplikasi, baik aplikasi web desktop maupun mobile', 'L', 'ihsan@mail.com', 'f9c8074d5a013e0729373f8f74cd0648'),
(180203, 'ihsan', 'Tangerang', 'UI/UX Designer', 'UI/UX Designer , membuat tampilan semenarik mungkin untuk aplikasi yang akan di buat baik berupa web, desktop maupun mobile', 'L', 'ihsan2@mail.com', 'e5fb7dbe42de7b70ae8001c20d651b4b'),
(180204, 'Frans Sinatra', 'Kediri', 'Data Scientist', 'Data Scientist, eksperimentasi dengan menggunakan teknik machine learning dan metode statistik untuk digunakan dalam pemodelan prediktif dan preskriptif.', 'L', 'Frans@mail.com', '31cf2b3561b2aed60bf8c02414cc955a'),
(180205, 'Kevin K Purnomo', 'Surabaya', 'Data Engineer', 'Data Engineer, mengembangkan dan membuat desain arsitektur manajemen data dan memelihara/memonitor infrastruktur data di perusahaan, seperti sistem database, data warehouse, data lake, dan sistem pemrosesan data berskala besar.', 'L', 'kevin@gmail.com', '9d5e3ecdeb4cdb7acfd63075ae046672');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `absensi`
--
ALTER TABLE `absensi`
  ADD PRIMARY KEY (`id_absensi`),
  ADD KEY `nip` (`nip`);

--
-- Indexes for table `pegawai`
--
ALTER TABLE `pegawai`
  ADD PRIMARY KEY (`nip`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `absensi`
--
ALTER TABLE `absensi`
  MODIFY `id_absensi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `absensi`
--
ALTER TABLE `absensi`
  ADD CONSTRAINT `absensi_ibfk_1` FOREIGN KEY (`nip`) REFERENCES `pegawai` (`nip`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
