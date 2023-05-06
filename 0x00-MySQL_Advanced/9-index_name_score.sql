--Creates an index of the first letter only.

CREATE INDEX idx_name_first_score ON names(name(1), score);
