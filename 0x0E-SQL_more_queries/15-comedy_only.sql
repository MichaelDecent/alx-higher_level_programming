-- lists all Comedy shows in the database hbtn_0d_tvshows
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order by the show title

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id = (SELECT tv_genres.id
                                FROM tv_genres
                                WHERE tv_genres.name = 'Comedy')
ORDER BY tv_shows.title ASC;