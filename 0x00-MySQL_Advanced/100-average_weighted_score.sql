-- Creates a stored procedure AddBonus

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE c INT DEFAULT user_id;
	DECLARE a INT DEFAULT SELECT (corrections.score * projects.weight) FROM corrections 
	INNER JOIN projects 
	ON corrections.project_id = projects.id, corrections.user_id = c;
	SELECT @b := SUM(projects.weight) FROM corrections
	INNER JOIN projects
	ON corrections.project_id = projects.id, corrections.user_id = c;
	UPDATE users
	SET average_score = @a / @b
	WHERE id = user_id;
END $$
DELIMITER $$
