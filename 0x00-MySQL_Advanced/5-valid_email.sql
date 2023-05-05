-- Resets valid_email attribute.

DELIMITER $$
CREATE TRIGGER emailtrig
AFTER UPDATE
ON users FOR EACH ROW
SET valid_email = 0 WHERE email != OLD.email;
$$
