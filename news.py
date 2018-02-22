import psycopg2

class SqlPython:

    def most_popular_articlex3(self):
        conn = psycopg2.connect("dbname=news")
        cur = conn.cursor()
        cur.execute("""
            SELECT articles.title, COUNT(articles.title) AS totalnumber FROM articles LEFT JOIN log
            ON articles.slug = substr(log.path, 10, 25)
            GROUP BY articles.title
            ORDER BY totalnumber desc limit 3;
            """)

        result = cur.fetchall()
        print("The three most popular articles of all time: ")
        print("--------------------------------------------")
        for title, count in result:
            print('"'  + title + '" -- ' + str(count) + " views.")
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
            ;
            """)

        result = cur.fetchall()

        print(" ")
        print("The days with more than 1 percent of requests lead to errors: ")
        print("-------------------------------------------------------------")

        for title, count in result:
            print(title + " -- " + str(count) + " views.")
            print(" ")

        conn.close
