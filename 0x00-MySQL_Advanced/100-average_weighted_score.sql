--Creates a stored procedure AddBonus

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	SET @a = user_id;

	UPDATE users
	SET average_score = (SELECT SUM(score) FROM corrections WHERE user_id = @a) 
		/ (SELECT COUNT(score) FROM corrections WHERE user_id= @a)
	WHERE id = user_id;
END $$
DELIMITER $$
