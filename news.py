#!/usr/bin/env python2.7
import psycopg2


class SqlPython:

    def most_popular_articlex3(self):
        conn = psycopg2.connect("dbname=news")  # Connects to database
        cur = conn.cursor()
        # Executes my PostgreSQL query
        cur.execute("""
            SELECT articles.title, COUNT(articles.title) AS totalnumber
            FROM articles LEFT JOIN log
            ON articles.slug = substr(log.path, 10, 25)
            GROUP BY articles.title
            ORDER BY totalnumber desc limit 3;
            """)

        # Stores the query into a variable result
        result = cur.fetchall()

        print("The three most popular articles of all time: ")
        print("--------------------------------------------")
        #  Loop through results to print out in a readable format
        for title, count in result:
            print('"' + title + '" -- ' + str(count) + " views.")
            print(" ")

        conn.close

    def most_popular_author(self):
        conn = psycopg2.connect("dbname=news")
        cur = conn.cursor()
        cur.execute("""
            SELECT authors.name, count(authors.name) as totalnum FROM authors
            LEFT JOIN articles ON authors.id = articles.author LEFT JOIN log
            ON articles.slug = substr(log.path, 10, 25) GROUP BY authors.name
            ORDER BY totalnum desc;
            """)

        result = cur.fetchall()

        print(" ")
        print("The most popular authors of all time: ")
        print("-------------------------------------")

        for author, count in result:
            print(author + " -- " + str(count) + " views.")
            print(" ")

        conn.close

    def most_errors(self):
        conn = psycopg2.connect("dbname=news")
        cur = conn.cursor()
        cur.execute("""
            WITH totalCallsByDate AS
            (SELECT to_char(time, 'FMMonth DD, YYYY') AS CallDate,
            COUNT(time) AS TotalNumberOfCalls
            FROM log GROUP BY CallDate)
            , notFoundsByDate AS
            (SELECT to_char(time, 'FMMonth DD, YYYY') AS CallDate,
            COUNT(time) AS TotalNumberOfCalls
            FROM log WHERE status = '404 NOT FOUND' GROUP BY CallDate)
            , finalQuery AS
            (SELECT t.CallDate,
            cast(100.0* coalesce(nf.TotalNumberOfCalls,0)/t.TotalNumberOfCalls
            as numeric(5,2))
            as ErrorPercent
            FROM totalCallsByDate t LEFT JOIN
            notFoundsByDate nf ON
            t.CallDate = nf.CallDate
            ORDER BY ErrorPercent desc)
            SELECT * FROM finalQuery
            WHERE ErrorPercent > 1;
            """)

        result = cur.fetchall()

        print(" ")
        print("The days when more than 1 percent of requests lead to errors: ")
        print("-------------------------------------------------------------")

        for date, error in result:
            print(str(date) + " - " + str(error) + "% errors.")
            print(" ")

        conn.close
