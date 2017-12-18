#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# "Database code" for the DB News.

import psycopg2

DBNAME = "news"

POPULAR_ARTICLES_SQL = "select title, article_hit_count from articles, \
                        articles_popularity where \
                        articles.slug = articles_popularity.slug order by \
                        article_hit_count desc fetch first {0} rows only;"

POPULAR_AUTHORS_SQL = "select authors_slug.name, sum(article_hit_count) as count \
                        from articles_popularity, authors_slug where \
                        articles_popularity.slug = authors_slug.slug \
                        group by name order by count desc;"

HIGH_ERROR_DAYS = "select to_char(log_errors.log_date,'DD Mon, YYYY'), \
                    round((total_errors/total_paths::decimal)*100,2) \
                    as percent from log_total, log_errors where \
                    log_errors.log_date = log_total.log_date \
                    order by log_errors.log_date asc;"


def get_popular_articles(row_limit):
    """Return all articles from the 'database', most popular first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(POPULAR_ARTICLES_SQL.format(row_limit))
    result = c.fetchall()
    db.close()
    return result


def get_popular_authors():
    """Return all authors from the 'database', most popular first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(POPULAR_AUTHORS_SQL)
    result = c.fetchall()
    db.close()
    return result


def get_high_error_days():
    """Return days with errors more than 1% from the 'database', most errors
    first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(HIGH_ERROR_DAYS)
    result = c.fetchall()
    db.close()
    return result
