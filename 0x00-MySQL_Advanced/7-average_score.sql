-- Creates a stored procedure AddBonus

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE a INT DEFAULT user_id;
	UPDATE users
	SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = a)
	WHERE id = user_id;
END $$
DELIMITER $$
