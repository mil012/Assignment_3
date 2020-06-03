
if __name__ == '__main__':
    # Import MySQL Connector Driver
    import mysql.connector as mysql

    # Load the credentials from the secured .env file
    import os
    from dotenv import load_dotenv
    load_dotenv('credentials.env')

    db_user = os.environ['MYSQL_USER']
    db_pass = os.environ['MYSQL_PASSWORD']
    db_name = os.environ['MYSQL_DATABASE']
    db_host = '192.168.99.100' 
    # different than inside the container and assumes default port of 3306
    #db_host = os.environ['MYSQL_HOST']


    # Connect to the database
    db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
    cursor = db.cursor()
    print("OKOK")

    #Uncomment and Run to clear all users
    #cursor.execute("drop table if exists Users;")

    #Uncomment and Run to clear all moves
    #cursor.execute("drop table if exists Moves;")

    # Create a TStudents table (wrapping it in a try-except is good practice)
    try:
        cursor.execute("""
        CREATE TABLE Letters (
        id integer  AUTO_INCREMENT PRIMARY KEY,
        first_name  VARCHAR(30) NOT NULL,
        last_name       VARCHAR(50) NOT NULL,
        email        VARCHAR(30) NOT NULL
        );
        """)

    except:
        print("Letters exists. Not recreating it.")

    try:
        cursor.execute("""
        CREATE TABLE Visits (
        id integer  AUTO_INCREMENT PRIMARY KEY,
        session  VARCHAR(30) NOT NULL,
        page       VARCHAR(50) NOT NULL
        );
        """)

    except:
        print("Analytics exists, Not recreating it.")

    try:
        cursor.execute("""
        CREATE TABLE Users (
        id integer  AUTO_INCREMENT PRIMARY KEY,
        email  VARCHAR(30) NOT NULL,
        password       VARCHAR(50) NOT NULL
        );
        """)

    except:
        print("Users exists. Not recreating it.")




    try:
        cursor.execute("""
        CREATE TABLE Coordinates (
        id integer  AUTO_INCREMENT PRIMARY KEY,
        1_lat  VARCHAR(50) NOT NULL,
        1_long  VARCHAR(50) NOT NULL,
        2_lat  VARCHAR(50) NOT NULL,
        2_long  VARCHAR(50) NOT NULL,
        3_lat  VARCHAR(50) NOT NULL,
        3_long  VARCHAR(50) NOT NULL

        );
        """)
        
    except:
        print("Coordinates exists. Not recreating it.")

    try:
        cursor.execute("""
        CREATE TABLE Progress (
        id integer  AUTO_INCREMENT PRIMARY KEY,
        Frontend  VARCHAR(50) NOT NULL,
        Backend  VARCHAR(50) NOT NULL,
        Hardware  VARCHAR(50) NOT NULL,
        Business  VARCHAR(50) NOT NULL
        
        );
        """)
        
    except:
        print("Coordinates exists. Not recreating it.")
    

    try:
        cursor.execute("""
        CREATE TABLE News (
        id integer  AUTO_INCREMENT PRIMARY KEY,
        Date  VARCHAR(50) NOT NULL,
        News  VARCHAR(500) NOT NULL
        );
        """)
    except:
        print("NEWS EXISTS ALREADY")

    #try:
        cursor.execute("""
        INSERT INTO News (Date, News)
        VALUE ('May 21, 2020', 'We are close to putting all the components of the project together');""")
        print("ADDED NEWSS SDSDSDSD")
        
        cursor.execute("""
        INSERT INTO News (Date, News)
        VALUE ('May 20, 2020', "The Hardware progress is almost finished");""")

        cursor.execute("""
        INSERT INTO News (Date, News)
        VALUE ('May 14, 2020', 'Introducing the Beta version of the planner page! You can use this tab to plan your missions, and it will visually show you where your waypoints are. Check it out!');""")
        
        cursor.execute("""
        INSERT INTO News (Date, News)
        VALUE ('May 11, 2020', 'Amir managed to get the basic frameworks of the Vision algorithm working');""")

        cursor.execute("""
        INSERT INTO News (Date, News)
        VALUE ('May 11, 2020', 'The Firewatch team presented their pitch to the ECE 140B class, to great acclaim');""")


    #except:
    #    print("Failed to add news Not recreating it.")

    cursor.execute("""
        INSERT INTO Letters (first_name, last_name, email)
        VALUE ('admin_first','admin_last','admin_email');""")

    cursor.execute("""
        INSERT INTO Progress (Frontend, Backend, Hardware, Business)
        VALUE ('75%','60%','80%','50%');""")

    cursor.execute("""
        INSERT INTO Users (email, password)
        VALUE ('mil012@ucsd.edu','password');""")


    db.commit()
    print("done")
    db.close()