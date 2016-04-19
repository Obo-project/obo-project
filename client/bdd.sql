-- phpMyAdmin SQL Dump
-- version 4.3.10
-- http://www.phpmyadmin.net
--
-- Client :  localhost:8889
-- Généré le :  Lun 18 Avril 2016 à 22:46
-- Version du serveur :  5.5.42
-- Version de PHP :  5.6.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Base de données :  `obo_cake`
--

-- --------------------------------------------------------

--
-- Structure de la table `entities`
--

CREATE TABLE `entities` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Contenu de la table `entities`
--

INSERT INTO `entities` (`id`, `name`) VALUES
(1, 'france');

-- --------------------------------------------------------

--
-- Structure de la table `facts`
--

CREATE TABLE `facts` (
  `id` int(11) NOT NULL,
  `relation_id` int(11) NOT NULL,
  `entity_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Contenu de la table `facts`
--

INSERT INTO `facts` (`id`, `relation_id`, `entity_id`, `quantity`) VALUES
(1, 1, 1, 67148000);

-- --------------------------------------------------------

--
-- Structure de la table `relations`
--

CREATE TABLE `relations` (
  `id` int(11) NOT NULL,
  `type` varchar(255) NOT NULL,
  `unity` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Contenu de la table `relations`
--

INSERT INTO `relations` (`id`, `type`, `unity`) VALUES
(1, 'hasPopulation', 'people');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `entities`
--
ALTER TABLE `entities`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `facts`
--
ALTER TABLE `facts`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `relations`
--
ALTER TABLE `relations`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `entities`
--
ALTER TABLE `entities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT pour la table `facts`
--
ALTER TABLE `facts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT pour la table `relations`
--
ALTER TABLE `relations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
