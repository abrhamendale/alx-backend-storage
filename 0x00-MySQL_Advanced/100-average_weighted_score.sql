-- Creates a stored procedure AddBonus

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE c INT DEFAULT user_id;
	SELECT @a := (corrections.score * projects.weight) / SUM(projects.weight)
	FROM corrections
	JOIN projects 
	ON corrections.project_id = projects.id
	WHERE corrections.user_id = c
	GROUP BY corrections.user_id;
	UPDATE users
	SET average_score = @a
	WHERE id = user_id;
END $$
DELIMITER $$
