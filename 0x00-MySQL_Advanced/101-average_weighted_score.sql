-- Creates a stored procedure AddBonus

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	SELECT corrections.user_id AS id, users.name, (users.SUM(corrections.score * projects.weight) / SUM(projects.weight)) AS average_score
	FROM corrections
		JOIN projects ON corrections.project_id = projects.id
		JOIN users ON corrections.user_id = users.id
	GROUP BY corrections.user_id;
END $$
DELIMITER $$
