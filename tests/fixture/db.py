import psycopg2

from data.add_review import testdata


class DbFixture:
    
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

        self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
        )
        

    def destroy(self):
        self.connection.close()

    def get_review_name(self):
        list_review = []
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name FROM reviews_reviews;")
            for row in cursor:
                list_review.append(row[0])
        finally:
            cursor.close()
        print(list_review)
        return list_review

    def get_creations_list(self):
        creation_list = []
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM reviews_creations;").fetchall()
            for row in cursor:
                creation_list.append(row[0])
        finally:
            cursor.close()
        return creation_list
    """
    def delete_testdata(self):
        testdata_review_name = [x.get("review_name") for x in (testdata)]
        name_review = ''
        try:
            cursor = self.connection.cursor()
            for row in testdata_review_name:
                name_review = f'{row}'
                cursor.execute("DELETE FROM reviews_reviews WHERE name=name_review;")
        finally:
            cursor.close()
    """
