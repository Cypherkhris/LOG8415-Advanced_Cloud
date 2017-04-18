# Initialisation :
CREATE DATABASE tp3;

USE tp3;

CREATE TABLE data (
  member_id INT(6),
  date DATE,
  country CHAR(2),
  gender ENUM('Female', 'Male'),
  ip_address VARCHAR(15),
  amount DOUBLE UNSIGNED,
  vip BOOLEAN,
  product_id INT(6),
  card_type VARCHAR(30),
  serial CHAR(11) PRIMARY KEY,
  zone CHAR(5)
) ENGINE NDBCLUSTER;


# Exemples :
INSERT INTO data VALUES (102468, '2012-09-18', 'ID', 'Female', '86.118.89.64', 9308.53, FALSE, 330124, 'jcb', '690-11-9719', 'zone1');
SELECT * FROM data WHERE serial = '690-11-9719';

# DATA_DUMP.CSV :
# suppression première ligne d'entête
# suppression des $
