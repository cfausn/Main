.echo off
.headers off
SELECT '' ;
SELECT '' ;
SELECT '**** Standard questions ****' ;
SELECT '10 at 5 points each for 50 points' ;
SELECT '' ;
SELECT '' ; SELECT 'Query 1';
.headers on

-- Query 1
-- Print the player name, player number, and player team
-- for all catchers (position 2)

-- SELECT 'Placeholder for 1' ;

select name,number,team from Player where position = 2;
.headers off
SELECT '' ; SELECT 'Query 2' ;
.headers on

-- Query 2
-- Print the coach name and team name for all the managers (a type of coach).

--SELECT 'Placeholder for 2' ;
select name,team from Coach where title = "Manager";

.headers off
SELECT '' ; SELECT 'Query 3' ;
.headers on

-- Query 3
-- Print the player name, number, and position (as a title) for all
-- outfielders (positions 7-9) whose home field is 'Fenway Park'.

--SELECT 'Placeholder for 3' ;

select Player.name, Player.number, Position.title from 
	Player, Position, Team 
	where (Player.team = Team.name and Team.ballpark = "Fenway Park") and 
	(Player.position = Position.posnum and 
	(Position.posnum between 7 and 9));
.headers off
SELECT '' ; SELECT 'Query 4' ;
.headers on

-- Query 4
-- Print the names and numbers of the hitting coaches for 'Hanley Ramirez'.
-- There may be more than one; any coach with a title containing 'Hitting'
-- anywhere within it is a hitting coach.

-- SELECT 'Placeholder for 4' ;
select Coach.name, Coach.number from Coach, Player, Team
	where (Player.name = 'Hanley Ramirez' and Player.team = Team.name and Coach.team = Player.team) and 
	Coach.title LIKE  "%Hitting%";

--select name, number, from Coach, Player where Player.name = "Hanley Ramirex" and Coach.team = Player.team and Coach.title = "Hitting" ;


.headers off
SELECT '' ; SELECT 'Query 5' ;
.headers on

-- Query 5
-- Print the player name, pitching coach name, and team name for
-- all pitchers (position 1) who are over 30 years old.
-- Pitching coaches have 'Pitching' somewhere in their title.

-- SELECT 'Placeholder for 5' ;

select Player.name, Coach.name, Team.name from Position, Player, Coach, Team
	where (Player.position = Position.posnum and Position.posnum = 1) and
	Player.age > 30 and (Coach.title LIKE "%Pitching%" and Player.team = Team.name and Coach.team = Player.team);

.headers off
SELECT '' ; SELECT 'Query 6' ;
.headers on

-- Query 6
-- Print the names, numbers, and ages of all infielders (positions 3-6)
-- whose home field is 'Camden Yards'.

-- SELECT 'Placeholder for 6' ;

select Player.name, Player.number, Player.age from Player, Position, Team
	where (Player.position = Position.posnum and 
	(Position.posnum between 3 and 6))
	and (Player.team = Team.name and Team.ballpark = "Camden Yards");

.headers off
SELECT '' ; SELECT 'Query 7' ;
.headers on

-- Query 7
-- Print the names, numbers, and team of all outfielders (positions 7-9)
-- whose manager's first name is 'John'

-- SELECT 'Placeholder for 7' ;

select Player.name, Player.number, Team.name from Player, Team, Coach, Position
	where (Player.team = Team.name and Coach.team = Player.team) 
	and (Coach.title = "Manager" and Coach.name LIKE "John%")
	and (Player.position = Position.posnum and (Position.posnum between 7 and 9));

.headers off
SELECT '' ; SELECT 'Query 8' ;
.headers on

-- Query 8
-- Print the names of the bullpen coaches for teams on the Eastern Seaboard
-- (Boston, Baltimore, and New York).

-- SELECT 'Placeholder for 8' ;

select Coach.name from Coach, Team 
	where (Coach.title = "Bullpen Coach") and
	((Team.city = "Boston" or Team.city = "Baltimore" or Team.city = "New York") and Team.name = Coach.team);

.headers off
SELECT '' ; SELECT 'Query 9' ;
.headers on

-- Query 9
-- Print the name, position, number, and team of all players whose
-- position is greater than their (jersey) number.

-- SELECT 'Placeholder for 9' ;

select Player.name, Position.posnum, Player.number, Player.team from Position, Player
	where (Player.position = Position.posnum and Position.posnum > Player.number);

.headers off
SELECT '' ; SELECT 'Query 10' ;
.headers on

-- Query 10
-- Print the name and position title for all players whose (first) name
-- begins with 'D'

-- SELECT 'Placeholder for 10' ;

select Player.name, Position.title from Player, Position
	where (Player.position = Position.posnum) and Player.name LIKE "D%"; 

.headers off
SELECT '' ;
SELECT '' ;
SELECT '**** Extra credit ****'  ;
SELECT '5 at 2 points each for 10 bonus points max.' ;
SELECT '' ;
SELECT '' ; SELECT 'Extra Credit 1' ;
.headers on

-- Query EC1
-- Create a listing of all player names and numbers for players on the 'Rays'
-- sorted by ascending name.
-- See ORDER BY

-- SELECT 'Placeholder for EC1' ;

select Player.name, Player.number from Player, Team
	where (Player.team = Team.name and Team.name = "Rays")
	order by Player.name ASC;

.headers off
SELECT '' ; SELECT 'Extra Credit 2' ;

-- Query EC2
-- How many infielders (positions 3-6) are in the database?
-- See the count() function.

-- SELECT 'Placeholder for EC2' ;

select count(Player.position) from Player, Position
	where (Player.position = Position.posnum and 
	(Position.posnum between 3 and 6));

SELECT '' ; SELECT 'Extra Credit 3' ;

-- Query EC3
-- What is the average age of all pitchers (position 1) in the database (rounded to
-- two fractional digit)?
-- See the avg() and round() functions.

-- SELECT 'Placeholder for EC3' ;

select round(avg(Player.age), 2) from Player, Position
	where Player.position = Position.posnum and Position.posnum = 1;

SELECT '' ; SELECT 'Extra Credit 4' ;

-- Query EC4
-- How many infielders (positions 3-6) are there in the database *by team*?
-- Each output line has a count and a team name.
-- See GROUP BY

-- SELECT 'Placeholder for EC4' ;

select count(Player.position), Player.team from Player, Position
	where (Player.position = Position.posnum and 
	(Position.posnum between 3 and 6))
	group by Player.team;

SELECT '' ; SELECT 'Extra Credit 5' ;

-- Query EC5
-- What is the average age of all pitchers (position 1) in the database *by team*?
-- Each output line has an average age rounded to two fractional digits and a team name.
-- The lines should be ordered by increasing average age.
-- See GROUP BY

-- SELECT 'Placeholder for EC5' ;

select round(avg(Player.age),2), Player.team from Player, Position
	where Player.position = Position.posnum and Position.posnum = 1
	group by Player.team;
