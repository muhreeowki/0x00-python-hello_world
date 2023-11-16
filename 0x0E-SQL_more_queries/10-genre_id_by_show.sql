-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT s.title, g.genre_id
FROM tv_shows as s JOIN tv_show_genres as g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id ASC;
