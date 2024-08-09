-- Indexing first letter of names and score

DROP INDEX IF EXISTS idx_name_first_score;

CREATE INDEX idx_name_first_score
ON names(name(1), score);
