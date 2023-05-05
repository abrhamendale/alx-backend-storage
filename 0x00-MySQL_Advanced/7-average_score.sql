-- Creates a stored procedure AddBonus

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN u_id INT)
BEGIN
	SET @a = u_id;
	SELECT @b := AVG(score) FROM corrections WHERE user_id = u_id;
	UPDATE users
	SET average_score = @b
	WHERE id = u_id;
END $$
DELIMITER $$
