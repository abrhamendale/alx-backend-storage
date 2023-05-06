-- Creates a stored procedure AddBonus

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	SET @a =
	(SELECT (SUM(corrections.score * projects.weight) / SUM(projects.weight))
		    FROM corrections
		    JOIN projects ON corrections.project_id = projects.id
		    JOIN users ON corrections.user_id = users.id and corrections.user_id = user_id
		GROUP BY corrections.user_id);
	UPDATE users
	        SET average_score = @a
		WHERE users.id = user_id;
END $$
DELIMITER $$
