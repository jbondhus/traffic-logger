## Traffic Logger

Logs traffic data for routes

## Database Setup

```sql
--
-- Disable foreign keys
--
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;

--
-- Set SQL mode
--
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

--
-- Set character set the client will use to send SQL statements to the server
--
SET NAMES 'utf8';

--
-- Create database
--
CREATE DATABASE traffic_logger;

--
-- Set default database
--
USE `traffic_logger`;

--
-- Definition for table states
--
DROP TABLE IF EXISTS states;
CREATE TABLE IF NOT EXISTS states (
  state_id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  state_abbreviation CHAR(2) NOT NULL,
  state_name VARCHAR(15) DEFAULT NULL,
  PRIMARY KEY (state_id)
)
ENGINE = INNODB
AUTO_INCREMENT = 1
CHARACTER SET utf8
COLLATE utf8_general_ci;

--
-- Definition for table transit
--
DROP TABLE IF EXISTS transit;
CREATE TABLE IF NOT EXISTS transit (
  transit_id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  route INT(11) UNSIGNED NOT NULL,
  duration INT(11) NOT NULL,
  all_data TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (transit_id)
)
ENGINE = INNODB
AUTO_INCREMENT = 1
CHARACTER SET utf8
COLLATE utf8_general_ci;

--
-- Definition for table cities
--
DROP TABLE IF EXISTS cities;
CREATE TABLE IF NOT EXISTS cities (
  city_id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  city_name VARCHAR(255) NOT NULL,
  state INT(11) UNSIGNED NOT NULL,
  PRIMARY KEY (city_id),
  CONSTRAINT FK_cities_state FOREIGN KEY (state)
    REFERENCES states(state_id) ON DELETE NO ACTION ON UPDATE RESTRICT
)
ENGINE = INNODB
AUTO_INCREMENT = 1
CHARACTER SET utf8
COLLATE utf8_general_ci;

--
-- Definition for table locations
--
DROP TABLE IF EXISTS locations;
CREATE TABLE IF NOT EXISTS locations (
  location_id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  address_1 VARCHAR(255) NOT NULL,
  address_2 VARCHAR(255) DEFAULT NULL,
  city INT(11) UNSIGNED NOT NULL,
  latitude DECIMAL(11, 8) NOT NULL,
  longitude DECIMAL(11, 8) NOT NULL,
  PRIMARY KEY (location_id),
  CONSTRAINT FK_locations_city FOREIGN KEY (city)
    REFERENCES cities(city_id) ON DELETE RESTRICT ON UPDATE RESTRICT
)
ENGINE = INNODB
AUTO_INCREMENT = 1
CHARACTER SET utf8
COLLATE utf8_general_ci;

--
-- Definition for table routes
--
DROP TABLE IF EXISTS routes;
CREATE TABLE IF NOT EXISTS routes (
  route_id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  start_location INT(11) UNSIGNED NOT NULL,
  end_location INT(11) UNSIGNED NOT NULL,
  PRIMARY KEY (route_id),
  CONSTRAINT FK_routes_end_location FOREIGN KEY (end_location)
    REFERENCES locations(location_id) ON DELETE NO ACTION ON UPDATE RESTRICT,
  CONSTRAINT FK_routes_start_location FOREIGN KEY (start_location)
    REFERENCES locations(location_id) ON DELETE RESTRICT ON UPDATE RESTRICT
)
ENGINE = INNODB
AUTO_INCREMENT = 1
CHARACTER SET utf8
COLLATE utf8_general_ci;

--
-- Restore previous SQL mode
--
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;

--
-- Enable foreign keys
--
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
```