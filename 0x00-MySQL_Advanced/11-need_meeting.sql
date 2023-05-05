--Creates a view

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80, last_meeting  = NULL OR DATEDIFF(CURDATE() - last_meeting) / 30 > 1;
