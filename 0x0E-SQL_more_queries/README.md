0x0E. SQL - More queries
========================

Resources
---------

**Read or watch**:

-   [How To Create a New User and Grant Permissions in MySQL](https://alx-intranet.hbtn.io/rltoken/RniBKj48bnIN8xpXhGl1yA "How To Create a New User and Grant Permissions in MySQL")
-   [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://alx-intranet.hbtn.io/rltoken/FIiEIvA6IN_hSKM5TvgyxQ "How To Use MySQL GRANT Statement To Grant Privileges To a User")
-   [MySQL constraints](https://alx-intranet.hbtn.io/rltoken/LrovGa6N-OE2ID_tpWZRaQ "MySQL constraints")
-   [SQL technique: subqueries](https://alx-intranet.hbtn.io/rltoken/kR71h5zjkPtx4kBoVf7q0g "SQL technique: subqueries")
-   [Basic query operation: the join](https://alx-intranet.hbtn.io/rltoken/rNMJeQ1jbNTCljbvCSjf6w "Basic query operation: the join")
-   [SQL technique: multiple joins and the distinct keyword](https://alx-intranet.hbtn.io/rltoken/HhZ6TJ1q5S0aR4lhfpKdOQ "SQL technique: multiple joins and the distinct keyword")
-   [SQL technique: join types](https://alx-intranet.hbtn.io/rltoken/T6FZUQdsMzr8hgNInBzudA "SQL technique: join types")
-   [SQL technique: union and minus](https://alx-intranet.hbtn.io/rltoken/Nd-sdM8QUpf0YKIlXzVv4w "SQL technique: union and minus")
-   [MySQL Cheat Sheet](https://alx-intranet.hbtn.io/rltoken/xP00kJWWi0SzvK-Lt8YdLQ "MySQL Cheat Sheet")
-   [The Seven Types of SQL Joins](https://alx-intranet.hbtn.io/rltoken/-plhBsra0N7BOuFoEg--zg "The Seven Types of SQL Joins")
-   [MySQL Tutorial](https://alx-intranet.hbtn.io/rltoken/I4Lws_eQrIrNTbkZvvk-oQ "MySQL Tutorial")
-   [SQL Style Guide](https://alx-intranet.hbtn.io/rltoken/051eAEP_rePBU7jeh879GA "SQL Style Guide")
-   [MySQL 8.0 SQL Statement Syntax](https://alx-intranet.hbtn.io/rltoken/YavbYiraYFr8oTukT_N6eQ "MySQL 8.0 SQL Statement Syntax")

Tasks
-----

### 0\. My privileges!

Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).

### 1\. Root user

Write a script that creates the MySQL server user `user_0d_1`.

### 2\. Read user

Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.

### 3\. Always a name

Write a script that creates the table `force_name` on your MySQL server.

### 4\. ID can't be null

Write a script that creates the table `id_not_null` on your MySQL server.

### 5\. Unique ID

Write a script that creates the table `unique_id` on your MySQL server.

### 6\. States table

Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.

### 7\. Cities table

Write a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.


### 8\. Cities of California

Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

### 9\. Cities by States

Write a script that lists all cities contained in the database `hbtn_0d_usa`.


### 10\. Genre ID by show

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download")

Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.


### 11\. Genre ID for all shows

Import the database dump of `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download") (same as `10-genre_id_by_show.sql`)

Write a script that lists all shows contained in the database `hbtn_0d_tvshows`.

### 12\. No genre

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download") (same as `11-genre_id_all_shows.sql`)

Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.

### 13\. Number of shows by genre

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download") (same as `12-no_genre.sql`)

Write a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

### 14\. My genres

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download") (same as `13-count_shows_by_genre.sql`)

Write a script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.

### 15\. Only Comedy

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download") (same as `14-my_genres.sql`)

Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`.

### 16\. List shows and genres

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download") (same as `15-comedy_only.sql`)

Write a script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.
