-- Creates a stored procedure AddBonus

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	SET @a = user_id;
	SELECT @b := AVG(score) FROM corrections WHERE user_id = @a;
	UPDATE users
	SET average_score = @b
	WHERE id = user_id;
END $$
DELIMITER $$
