select * from Player where position = 2;
select name, age from Player where position = 1 and team = "Rays";
select name,number,team from Player where (position = 7 or position = 8 or position = 9) and age <= 25;
select name,number from Player where (position = 3 or position = 4 or position = 5 or position = 6) and team = "Red Sox";
select name,number,team from Player where position = 1 and age > 30;
