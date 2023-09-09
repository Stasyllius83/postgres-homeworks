"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

# connect to db
with psycopg2.connect(host="localhost", database='north', user='postgres', password='12345') as conn:
    with conn.cursor() as cur:
        # execute query
        # cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", [(1, "Nancy", "Davolio",
        #                                                                            "Sales Representative", "1948-12-08",
        #                                                                            "Education includes a BA in "
        #                                                                            "psychology from Colorado State "
        #                                                                            "University in 1970.  She also "
        #                                                                            "completed The Art of the Cold "
        #                                                                            "Call.  Nancy is a member of "
        #                                                                            "Toastmasters International."),
        #                                                                           (2, "Andrew", "Fuller",
        #                                                                            "Vice President, Sales",
        #                                                                            "1952-02-19",
        #                                                                            "Andrew received his BTS "
        #                                                                            "commercial in 1974 and a Ph.D. in "
        #                                                                            "international marketing from the "
        #                                                                            "University of Dallas in 1981.  He "
        #                                                                            "is fluent in French and Italian "
        #                                                                            "and reads German.  He joined the "
        #                                                                            "company as a sales "
        #                                                                            "representative, was promoted to "
        #                                                                            "sales manager in January 1992 and "
        #                                                                            "to vice president of sales in "
        #                                                                            "March 1993.  Andrew is a member "
        #                                                                            "of the Sales Management "
        #                                                                            "Roundtable, the Seattle Chamber "
        #                                                                            "of Commerce, and the Pacific Rim "
        #                                                                            "Importers Association."),
        #                                                                           (3, "Janet", "Leverling",
        #                                                                            "Sales Representative", "1963-08-30",
        #                                                                            "Janet has a BS degree in "
        #                                                                            "chemistry from Boston College ("
        #                                                                            "1984).  She has also completed a "
        #                                                                            "certificate program in food "
        #                                                                            "retailing management.  Janet was "
        #                                                                            "hired as a sales associate in "
        #                                                                            "1991 and promoted to sales "
        #                                                                            "representative in February 1992."),
        #                                                                           (4, "Margaret", "Peacock",
        #                                                                            "Sales Representative", "1937-09-19",
        #                                                                            "Margaret holds a BA in English "
        #                                                                            "literature from Concordia College "
        #                                                                            "(1958) and an MA from the "
        #                                                                            "American Institute of Culinary "
        #                                                                            "Arts (1966).  She was assigned to "
        #                                                                            "the London office temporarily "
        #                                                                            "from July through November 1992."),
        #                                                                           (5, "Steven", "Buchanan",
        #                                                                            "Sales Manager", "1955-03-04",
        #                                                                            "Steven Buchanan graduated from "
        #                                                                            "St. Andrews University, Scotland, "
        #                                                                            "with a BSC degree in 1976.  Upon "
        #                                                                            "joining the company as a sales "
        #                                                                            "representative in 1992, "
        #                                                                            "he spent 6 months in an "
        #                                                                            "orientation program at the "
        #                                                                            "Seattle office and then returned "
        #                                                                            "to his permanent post in London.  "
        #                                                                            "He was promoted to sales manager "
        #                                                                            "in March 1993.  Mr. Buchanan has "
        #                                                                            "completed the courses Successful "
        #                                                                            "Telemarketing and International "
        #                                                                            "Sales Management.  He is fluent "
        #                                                                            "in French."),
        #                                                                           (6, "Michael", "Suyama",
        #                                                                            "Sales Representative", "1963-07-02",
        #                                                                            "Michael is a graduate of Sussex "
        #                                                                            "University (MA, economics, "
        #                                                                            "1983) and the University of "
        #                                                                            "California at Los Angeles (MBA, "
        #                                                                            "marketing, 1986).  He has also "
        #                                                                            "taken the courses Multi-Cultural "
        #                                                                            "Selling and Time Management for "
        #                                                                            "the Sales Professional.  He is "
        #                                                                            "fluent in Japanese and can read "
        #                                                                            "and write French, Portuguese, "
        #                                                                            "and Spanish."),
        #                                                                           (7, "Robert", "King",
        #                                                                            "Sales Representative", "1960-05-29",
        #                                                                            "Robert King served in the Peace "
        #                                                                            "Corps and traveled extensively "
        #                                                                            "before completing his degree in "
        #                                                                            "English at the University of "
        #                                                                            "Michigan in 1992, the year he "
        #                                                                            "joined the company.  After "
        #                                                                            "completing a course entitled "
        #                                                                            "Selling in Europe, "
        #                                                                            "he was transferred to the London "
        #                                                                            "office in March 1993."),
        #                                                                           (8, "Laura", "Callahan",
        #                                                                            "Inside Sales Coordinator",
        #                                                                            "1958-01-09",
        #                                                                            "Laura received a BA in psychology "
        #                                                                            "from the University of "
        #                                                                            "Washington.  She has also "
        #                                                                            "completed a course in business "
        #                                                                            "French.  She reads and writes "
        #                                                                            "French."),
        #                                                                           (9, "Anne", "Dodsworth",
        #                                                                            "Sales Representative", "1966-01-27",
        #                                                                            "Anne has a BA degree in English "
        #                                                                            "from St. Lawrence College.  She "
        #                                                                            "is fluent in French and German.")])
        # cur.execute("SELECT * FROM employees")

        cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", [("ALFKI", "Alfreds Futterkiste", "Maria Anders"),
                                                                      ("ANATR", "Ana Trujillo Emparedados y helados",
                                                                       "Ana Trujillo"),
                                                                      ("ANTON", "Antonio Moreno Taquería",
                                                                       "Antonio Moreno"),
                                                                      ("AROUT", "Around the Horn", "Thomas Hardy"),
                                                                      ("BERGS", "Berglunds snabbköp",
                                                                       "Christina Berglund"),
                                                                      (
                                                                      "BLAUS", "Blauer See Delikatessen", "Hanna Moos"),
                                                                      ("BLONP", "Blondesddsl père et fils",
                                                                       "Frédérique Citeaux"),
                                                                      ("BOLID", "Bólido Comidas preparadas",
                                                                       "Martín Sommer"),
                                                                      ("BONAP", "Bon app'", "Laurence Lebihan"),
                                                                      ("BOTTM", "Bottom-Dollar Markets",
                                                                       "Elizabeth Lincoln"),
                                                                      ("BSBEV", "B's Beverages", "Victoria Ashworth"),
                                                                      ("CACTU", "Cactus Comidas para llevar",
                                                                       "Patricio Simpson"),
                                                                      ("CENTC", "Centro comercial Moctezuma",
                                                                       "Francisco Chang"),
                                                                      ("CHOPS", "Chop-suey Chinese", "Yang Wang"),
                                                                      ("COMMI", "Comércio Mineiro", "Pedro Afonso"),
                                                                      ("CONSH", "Consolidated Holdings",
                                                                       "Elizabeth Brown")])
        cur.execute("SELECT * FROM customers")

        # cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", [(10248,"VINET",5,"1996-07-04","Reims"),
        #                                                                    (10249,"TOMSP",6,"1996-07-05","Münster"),
        #                                                                    (10250,"HANAR",4,"1996-07-08","Rio de Janeiro"),
        #                                                                    (10251,"VICTE",3,"1996-07-08","Lyon"),
        #                                                                    (10252,"SUPRD",4,"1996-07-09","Charleroi"),
        #                                                                    (10253,"HANAR",3,"1996-07-10","Rio de Janeiro"),
        #                                                                    (10254,"CHOPS",5,"1996-07-11","Bern"),
        #                                                                    (10255,"RICSU",9,"1996-07-12","Genève"),
        #                                                                    (10256,"WELLI",3,"1996-07-15","Resende"),
        #                                                                    (10257,"HILAA",4,"1996-07-16","San Cristóbal")])
        #
        # cur.execute("SELECT * FROM orders")


        rows = cur.fetchall()
        for row in rows:
            print(row)

conn.close()
