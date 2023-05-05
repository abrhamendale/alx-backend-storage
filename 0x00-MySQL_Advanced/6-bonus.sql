-- Creates a stored procedure AddBonus

DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
	SET @a = user_id;
	SET @b = score;
	SELECT DISTINCT @C := id FROM projects WHERE name = project_name;
	IF (EXISTS(SELECT name FROM projects WHERE name = project_name))
		THEN
		INSERT INTO corrections (user_id, project_id, score) 
			VALUES (@a, @c, @b);
	ELSE
		INSERT INTO projects (name) VALUES (project_name);
		INSERT INTO corrections (user_id, project_id, score)
		        VALUES (@a, LAST_INSERT_ID(), @b);
		END IF;
END $$
DELIMITER ;
