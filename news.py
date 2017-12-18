#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Prints out information about News articles in news database.

import newsdb

ROW_LIMIT = 3


# Formats results of a database call that provides most popular 3 articles
# of all time.
def print_popular_articles():
    rows = newsdb.get_popular_articles(ROW_LIMIT)
    for row in rows:
        print '\"' + row[0] + '\"' + " — " + str(row[1]) + " views"


# Formats results of a database call that provides most popular authors.
def print_popular_authors():
    rows = newsdb.get_popular_authors()
    for row in rows:
        print row[0] + " — " + str(row[1]) + " views"


# Formats results of a database call that provides days where errors were
# more than 1%.
def print_high_error_days():
    rows = newsdb.get_high_error_days()
    for row in rows:
        if (row[1] > 1):
            print row[0] + " — " + str(row[1]) + "% errors"


# Show the reports one after another
def printAllReports():
    print("What are the most popular three articles of all time?\n")
    print_popular_articles()
    print("\n")
    print("Who are the most popular authors of all time?\n")
    print_popular_authors()
    print("\n")
    print("On which days did more than 1% of requests lead to errors? \n")
    print_high_error_days()
    print("\n")


printAllReports()
