from mysqlconnection import connectToMySQL

DATABASE = "seocnd_flask"

class User:
        def __init__( self , data ):
                self.id = data['id']
                self.first_name = data['first_name']
                self.last_name = data['last_name']
                self.email = data['email']
                self.created_at = data['created_at']
                self.updated_at = data['updated_at']

        @classmethod
        def get_all(cls):
                query = "SELECT * FROM users;"
# make sure to call the connectToMySQL function with the schema you are targeting.
                results = connectToMySQL(DATABASE).query_db(query)
# Create an empty list to append our instances of friends
                users = []
# Iterate over the db results and create instances of friends with cls.
                for user in results:
                        users.append( cls(user) )
                return users

#to save our user to the database
        @classmethod
        def save(cls, data ):
                query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
#data is a dictionary that will be passed into the save method from server.py
                return connectToMySQL(DATABASE).query_db( query, data )


                


                