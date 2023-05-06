-- Creates a stored procedure AddBonus

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
	FROM corrections JOIN
	     projects
	     ON corrections.project_id = projects.id
	GROUP BY corrections.user_id;
END $$
DELIMITER $$
