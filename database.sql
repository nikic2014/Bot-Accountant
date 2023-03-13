DROP TABLE Expenses;
DROP TABLE Income;
DROP TABLE Users;

CREATE TABLE Users(
	user_id integer PRIMARY KEY,
	chat_id integer NOT NULL
);

CREATE TABLE Expenses(
	fk_user_id integer NOT NULL,
	data_expenses date,
	amount integer,
	
	FOREIGN KEY (fk_user_id) REFERENCES Users(user_id)
);

CREATE TABLE Income(
	fk_user_id integer NOT NULL,
	data_income date,
	amount integer,
	
	FOREIGN KEY (fk_user_id) REFERENCES Users(user_id)
);

-- INSERT INTO Users VALUES (2323, 165);

select * from users;
select * from Expenses;
select * from Income;

INSERT INTO Users VALUES (12, 165);
INSERT INTO Expenses VALUES (12, '2023-03-19', 3421);

select *
from Expenses
WHERE fk_user_id = 452895447 and data_expenses >= '2023-03-13' and data_expenses <= '2023-03-13';

INSERT INTO users VALUES (generate_series(3, 10000), 1512);
INSERT INTO Expenses VALUES (generate_series(1, 10000), '2023-03-19', 3421);

CREATE INDEX test_index on using 'B-tree' fk_user_id;
DROP INDEX test_index;

EXPLAIN select *
from Expenses
WHERE fk_user_id = 5000;
