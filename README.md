# Log Analysis
This is a internal reporting tool that will use information from the "news" database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, the code will answer questions about the site's user activity.

The program will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

## How to launch the program.
1. Make sure you create the following 4 views,

  * create view **articles_popularity** as (select REPLACE(path, '/article/', '')
as slug, count(path) as article_hit_count from log where trim(path) != ('/')
and status = ('200 OK') group by path);

  * create view **authors_slug** as (select name, slug from authors, articles where
  authors.id = articles.author);

  * create view **log_total** as (select log.time::timestamp::date as log_date,
  count(path) as total_paths from log group by log_date);

  * create view **log_errors** as (select log.time::timestamp::date as log_date,
  count(path) as total_errors from log where status != ('200 OK')
  group by log_date);

2. Execute the python script, news.py in your environment.
