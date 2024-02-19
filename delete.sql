USE hbnb_dev_db;

SET foreign_key_checks = 0;

-- Disable foreign key checks temporarily

DELETE FROM `cities` WHERE `state_id` IS NOT NULL;
-- Delete all cities with a non-null state_id (associated with states)

DELETE FROM `states`;

-- Now you can safely delete all records from the states table

SET foreign_key_checks = 1;
-- Re-enable foreign key checks

