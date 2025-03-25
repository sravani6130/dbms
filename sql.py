import pymysql

# ANSI escape codes for colors
GREEN = "\033[32m"    # Green text
MAGENTA = "\033[35m"  # Magenta text
BLUE = "\033[34m"     # Blue text
RESET = "\033[0m"     # Reset to default color

# Establish connection to the MySQL server
def get_connection(database=None):
    connection = pymysql.connect(
        host='localhost',  # Replace with your host, e.g., 'localhost' or '127.0.0.1'
        user='root',       # Replace with your MySQL username
        password='Arshiya@1119',  # Replace with your MySQL password
        database=database,    # Connect directly to the `Dbb` database
        connect_timeout=10,  # Timeout in seconds
        cursorclass=pymysql.cursors.DictCursor
        
    )
    return connection
try:
    connection = get_connection()
    with connection.cursor() as cursor:
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS `Music_Database`")

    connection.close()  # Close the previous connection
    connection = get_connection('Music_Database')
    with connection.cursor() as cursor:
        cursor.execute("USE `Music_Database`")
        # Create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Artist (
            Name VARCHAR(255),
            Stage_name VARCHAR(255) PRIMARY KEY
        )""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ArtistStatistics (
            Stage_name VARCHAR(255) PRIMARY KEY,
            Hits INT,
            Flops INT,
            FOREIGN KEY (Stage_name) REFERENCES Artist(Stage_name)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ArtistRole (
            Stage_name VARCHAR(255),
            Role VARCHAR(255),
            PRIMARY KEY (Stage_name, Role),
            FOREIGN KEY (Stage_name) REFERENCES Artist(Stage_name)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ArtistUpcomingProjects (
            Stage_name VARCHAR(255),
            Project VARCHAR(255),
            PRIMARY KEY (Stage_name, Project),
            FOREIGN KEY (Stage_name) REFERENCES Artist(Stage_name)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Producer (
            Name VARCHAR(255) PRIMARY KEY,
            Debut_Year YEAR
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ProducerStatistics (
            Name VARCHAR(255) PRIMARY KEY,
            Hits INT,
            Flops INT,
            FOREIGN KEY (Name) REFERENCES Producer(Name)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Distribution (
            Name VARCHAR(255),
            No_of_platforms INT,
            Release_date YEAR,
            PRIMARY KEY (Name, Release_date)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Award (
            Name VARCHAR(255),
            Level INT,
            Year YEAR,
            Album_ID INT,
            PRIMARY KEY (Name, Year)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Album (
            Album_ID INT PRIMARY KEY,
            Release_year YEAR,
            Duration INT,
            Budget INT,
            Stage_Name VARCHAR(255),
            Distribution_Name VARCHAR(255),
            Release_date YEAR,
            FOREIGN KEY (Stage_Name) REFERENCES Artist(Stage_name),
            FOREIGN KEY (Distribution_Name, Release_date) REFERENCES Distribution(Name, Release_date)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS AlbumStatistics (
            Album_ID INT PRIMARY KEY,
            Collections INT,
            FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS AlbumAwards (
            Album_ID INT,
            Award_Name VARCHAR(255),
            Award_Year YEAR,
            PRIMARY KEY (Album_ID, Award_Name, Award_Year),
            FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID),
            FOREIGN KEY (Award_Name, Award_Year) REFERENCES Award(Name, Year)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS AlbumGenre (
            Album_ID INT,
            Genre VARCHAR(255),
            PRIMARY KEY (Album_ID, Genre),
            FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Song (
            Name VARCHAR(255) PRIMARY KEY,
            Artist VARCHAR(255),
            Producer_Name VARCHAR(255),
            FOREIGN KEY (Artist) REFERENCES Artist(Stage_name),
            FOREIGN KEY (Producer_Name) REFERENCES Producer(Name)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS SongLyrics (
            Lyrics_ID INT PRIMARY KEY,
            Song_Name VARCHAR(255),
            Lyric_Line VARCHAR(255),
            Line_Number INT,
            FOREIGN KEY (Song_Name) REFERENCES Song(Name)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS SongMedia (
            Media_ID INT PRIMARY KEY,
            Song_Name VARCHAR(255),
            Media_Type VARCHAR(255),
            Media_URL VARCHAR(255),
            FOREIGN KEY (Song_Name) REFERENCES Song(Name)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ProducerAlbumIDs (
            Name VARCHAR(255),
            Album_ID INT,
            PRIMARY KEY (Name, Album_ID),
            FOREIGN KEY (Name) REFERENCES Producer(Name),
            FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ProducerUpcomingProjects (
            Name VARCHAR(255),
            Project VARCHAR(255),
            PRIMARY KEY (Name, Project),
            FOREIGN KEY (Name) REFERENCES Producer(Name)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Album_Review (
            Review_ID INT,
            Review_Date DATE,
            Rating FLOAT,
            Comments VARCHAR(255),
            Album_ID INT,
            PRIMARY KEY (Review_ID, Review_Date),
            FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Song_Review (
            Review_ID INT,
            Review_Date DATE,
            Rating FLOAT,
            Comments VARCHAR(255),
            Song_Name VARCHAR(255),
            PRIMARY KEY (Review_ID, Review_Date),
            FOREIGN KEY (Song_Name) REFERENCES Song(Name)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Concert (
            Concert_ID INT PRIMARY KEY,
            Date DATE,
            Location VARCHAR(255),
            Stage_Name VARCHAR(255),
            Album_ID INT,
            FOREIGN KEY (Stage_Name) REFERENCES Artist(Stage_name),
            FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Performs (
            Stagename VARCHAR(255),
            Song_name VARCHAR(255),
            Producer_name VARCHAR(255),
            PRIMARY KEY (Stagename, Song_name, Producer_name),
            FOREIGN KEY (Stagename) REFERENCES Artist(Stage_name),
            FOREIGN KEY (Song_name) REFERENCES Song(Name),
            FOREIGN KEY (Producer_name) REFERENCES Producer(Name)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS BelongsTo (
            BelongsTo_ID INT PRIMARY KEY,
            Song_name VARCHAR(255),
            Producer_name VARCHAR(255),
            Album_id INT,
            FOREIGN KEY (Song_name) REFERENCES Song(Name),
            FOREIGN KEY (Producer_name) REFERENCES Producer(Name),
            FOREIGN KEY (Album_id) REFERENCES Album(Album_ID)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ProducedBy (
            ProducedBy_ID INT PRIMARY KEY,
            Album_id INT,
            Producer_name VARCHAR(255),
            FOREIGN KEY (Album_id) REFERENCES Album(Album_ID),
            FOREIGN KEY (Producer_name) REFERENCES Producer(Name)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Features (
            Feature_ID INT PRIMARY KEY,
            Stagename VARCHAR(255),
            Song_name VARCHAR(255),
            Producer_name VARCHAR(255),
            Album_id INT,
            FOREIGN KEY (Stagename) REFERENCES Artist(Stage_name),
            FOREIGN KEY (Song_name) REFERENCES Song(Name),
            FOREIGN KEY (Producer_name) REFERENCES Producer(Name),
            FOREIGN KEY (Album_id) REFERENCES Album(Album_ID)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ConcertBy (
            ConcertBy_ID INT PRIMARY KEY,
            Stagename VARCHAR(255),
            Album_id INT,
            Concert_ID INT,
            FOREIGN KEY (Stagename) REFERENCES Artist(Stage_name),
            FOREIGN KEY (Album_id) REFERENCES Album(Album_ID),
            FOREIGN KEY (Concert_ID) REFERENCES Concert(Concert_ID)
        )""")
        
        
        # Insert into Artist
        cursor.execute("INSERT INTO Artist (Name, Stage_name) VALUES ('Ed Sheeran', 'EdSheer'), ('Billie Eilish', 'Billie')")
            
        # Insert into Producer
        cursor.execute("INSERT INTO Producer (Name, Debut_Year) VALUES ('Max Martin', 1990), ('Finneas', 2015)")
            
        # Insert into Distribution
        cursor.execute("INSERT INTO Distribution (Name, No_of_platforms, Release_date) VALUES ('Universal Music', 20, 2021), ('Atlantic Records', 18, 2022)")
            
        # Insert into Award
        cursor.execute("INSERT INTO Award (Name, Level, Year, Album_ID) VALUES ('Grammy', 1, 2022, 1), ('Billboard Music Award', 2, 2021, 2)")
            
        # Insert into Album
        cursor.execute("INSERT INTO Album (Album_ID, Release_year, Duration, Budget, Stage_Name, Distribution_Name, Release_date) VALUES (1, 2021, 45, 500000, 'EdSheer', 'Universal Music', 2021), (2, 2022, 40, 600000, 'Billie', 'Atlantic Records', 2022)")
            
        # Insert into ArtistStatistics
        cursor.execute("INSERT INTO ArtistStatistics (Stage_name, Hits, Flops) VALUES ('EdSheer', 10, 2), ('Billie', 8, 1)")
            
        # Insert into ArtistRole
        cursor.execute("INSERT INTO ArtistRole (Stage_name, Role) VALUES ('EdSheer', 'Singer'), ('EdSheer', 'Songwriter'), ('Billie', 'Singer'), ('Billie', 'Songwriter')")
            
        # Insert into ArtistUpcomingProjects
        cursor.execute("INSERT INTO ArtistUpcomingProjects (Stage_name, Project) VALUES ('EdSheer', 'World Tour 2024'), ('Billie', 'New Album Release')")
            
        # Insert into ProducerStatistics
        cursor.execute("INSERT INTO ProducerStatistics (Name, Hits, Flops) VALUES ('Max Martin', 50, 5), ('Finneas', 15, 2)")
            
        # Insert into AlbumStatistics
        cursor.execute("INSERT INTO AlbumStatistics (Album_ID, Collections) VALUES (1, 1000000), (2, 1200000)")
            
        # Insert into AlbumAwards
        cursor.execute("INSERT INTO AlbumAwards (Album_ID, Award_Name, Award_Year) VALUES (1, 'Grammy', 2022), (2, 'Billboard Music Award', 2021)")
            
        # Insert into AlbumGenre
        cursor.execute("INSERT INTO AlbumGenre (Album_ID, Genre) VALUES (1, 'Pop'), (2, 'Alternative')")
            
        # Insert into Song
        cursor.execute("INSERT INTO Song (Name, Artist, Producer_Name) VALUES ('Perfect', 'EdSheer', 'Max Martin'), ('Bad Guy', 'Billie', 'Finneas')")
            
        # Insert into SongLyrics
        cursor.execute("INSERT INTO SongLyrics (Lyrics_ID, Song_Name, Lyric_Line, Line_Number) VALUES (1, 'Perfect', 'I found a love for me', 1), (2, 'Bad Guy', 'White shirt, now red', 1)")
            
        # Insert into SongMedia
        cursor.execute("INSERT INTO SongMedia (Media_ID, Song_Name, Media_Type, Media_URL) VALUES (1, 'Perfect', 'Music Video', 'https://youtu.be/2Vv-BfVoq4g'), (2, 'Bad Guy', 'Music Video', 'https://youtu.be/HUHC9tYz8ik')")
            
        # Insert into ProducerAlbumIDs
        cursor.execute("INSERT INTO ProducerAlbumIDs (Name, Album_ID) VALUES ('Max Martin', 1), ('Finneas', 2)")
            
        # Insert into ProducerUpcomingProjects
        cursor.execute("INSERT INTO ProducerUpcomingProjects (Name, Project) VALUES ('Max Martin', 'Pop Collaboration'), ('Finneas', 'Sister Album')")
            
        cursor.execute("""INSERT INTO Album_Review (Review_ID, Review_Date, Rating, Comments, Album_ID) VALUES (1, '2021-06-15', 4.5, 'Excellent album', 1),(2, '2022-07-20', 4.7, 'Groundbreaking work', 2),(3, '2021-07-10', 4.8, 'Masterpiece!', 1),(4, '2021-08-01', 4.6, 'Great composition', 1),(5, '2022-08-15', 4.6, 'Impressive production', 2),(6, '2022-09-10', 4.3, 'Well crafted!', 2);""")
        # Insert into Song_Review
        cursor.execute("INSERT INTO Song_Review (Review_ID, Review_Date, Rating, Comments, Song_Name) VALUES (1, '2021-05-10', 4.8, 'Beautiful composition', 'Perfect'), (2, '2022-06-15', 4.6, 'Unique sound', 'Bad Guy')")
            
        # Insert into Concert
        cursor.execute("INSERT INTO Concert (Concert_ID, Date, Location, Stage_Name, Album_ID) VALUES (1, '2023-01-15', 'London', 'EdSheer', 1), (2, '2023-02-20', 'Los Angeles', 'Billie', 2)")
            
        # Insert into Performs
        cursor.execute("INSERT INTO Performs (Stagename, Song_name, Producer_name) VALUES ('EdSheer', 'Perfect', 'Max Martin'), ('Billie', 'Bad Guy', 'Finneas')")
            
        # Insert into BelongsTo
        cursor.execute("INSERT INTO BelongsTo (BelongsTo_ID, Song_name, Producer_name, Album_id) VALUES (1, 'Perfect', 'Max Martin', 1), (2, 'Bad Guy', 'Finneas', 2)")
            
        # Insert into ProducedBy
        cursor.execute("INSERT INTO ProducedBy (ProducedBy_ID, Album_id, Producer_name) VALUES (1, 1, 'Max Martin'), (2, 2, 'Finneas')")
            
        # Insert into Features
        cursor.execute("INSERT INTO Features (Feature_ID, Stagename, Song_name, Producer_name, Album_id) VALUES (1, 'EdSheer', 'Perfect', 'Max Martin', 1), (2, 'Billie', 'Bad Guy', 'Finneas', 2)")
            
        # Insert into ConcertBy
        cursor.execute("INSERT INTO ConcertBy (ConcertBy_ID, Stagename, Album_id, Concert_ID) VALUES (1, 'EdSheer', 1, 1), (2, 'Billie', 2, 2)")


        connection.commit()
        
        
except Exception as e:
    print()

finally:
    if 'connection' in locals() and connection.open:
        connection.close()

# Function to execute a query and fetch the results
def execute_query(query, params=None):
    try:
        connection = get_connection('Music_Database')
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        connection.close()


# 1. Get Artists With Name Starting with B
def get_artists_starting_with_b():
    query = "SELECT * FROM Artist WHERE Name LIKE 'B%'"
    return execute_query(query)


# 2. Get Song Reviews for a Specific Song
def get_song_reviews(song_name):
    query = "SELECT Review_Date, Rating, Comments FROM Song_Review WHERE Song_Name = %s"
    return execute_query(query, (song_name,))


# 3. Get Producer’s Upcoming Projects
def get_producer_upcoming_projects(producer_name):
    query = "SELECT Project FROM ProducerUpcomingProjects WHERE Name = %s"
    return execute_query(query, (producer_name,))


# 4. Get the Average Rating for an Album
def get_average_album_rating(album_id):
    query = "SELECT AVG(Rating) AS Avg_Rating FROM Album_Review WHERE Album_ID = %s"
    return execute_query(query, (album_id,))


# 5. Get Total Collections of All Albums
def get_total_album_collections():
    query = "SELECT SUM(Collections) AS Total_Collections FROM AlbumStatistics"
    return execute_query(query)


#6. Find Artists Matching With Partial Name
def find_artists_matching_name(partial_name):
    query = "SELECT * FROM Artist WHERE Name LIKE %s"
    return execute_query(query, (f"%{partial_name}%",))


#7.  Get Songs Above Average Rating
def get_songs_above_average_by_rating():
    query = """
    SELECT Song_Name, COUNT(Review_ID) AS NumberOfReviews
    FROM Song_Review
    WHERE Rating > (SELECT AVG(Rating) FROM Song_Review)
    GROUP BY Song_Name
    """
    return execute_query(query)


# 8. Update Rating for a Song Review
def update_song_review_rating(review_id, new_rating):
    query = "UPDATE Song_Review SET Rating = %s WHERE Review_ID = %s"
    
    try:
        connection = get_connection('Music_Database')
        with connection.cursor() as cursor:
            cursor.execute(query, (new_rating, review_id))
            connection.commit()  # Commit the transaction
            print(f"{GREEN}Updated rating for review ID {review_id} to {new_rating}.{RESET}")
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        connection.close()


# 9. Update the Number of Platforms for a Distribution
def update_distribution_platforms(distribution_name, new_platform_count):
    query = "UPDATE Distribution SET No_of_platforms = %s WHERE Name = %s"
    
    try:
        connection = get_connection('Music_Database')
        with connection.cursor() as cursor:
            cursor.execute(query, (new_platform_count, distribution_name))
            connection.commit()  # Commit the transaction
            print(f"{GREEN}Updated platform count for {distribution_name}.{RESET}")
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        connection.close()


# 10. Update Role of an Artist
def update_artist_role(stage_name, old_role, new_role):
    query = "UPDATE ArtistRole SET Role = %s WHERE Stage_name = %s AND Role = %s"
    try:
        connection = get_connection('Music_Database')
        with connection.cursor() as cursor:
            cursor.execute(query, (new_role, stage_name, old_role))
            connection.commit()  # Commit the transaction to save the changes
            print(f"{GREEN}Updated role for {stage_name} from {old_role} to {new_role}.{RESET}")
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        connection.close()


# 11. Insert a New Artist
def insert_new_artist(name, stage_name):
    query = "INSERT INTO Artist (Name, Stage_name) VALUES (%s, %s)"
    
    try:
        connection = get_connection('Music_Database')
        with connection.cursor() as cursor:
            cursor.execute(query, (name, stage_name))
            connection.commit()  # Commit the transaction
            print(f"{GREEN}Inserted new artist {name} with stage name {stage_name}.{RESET}")
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        connection.close()


#12 Insert a New Song
def insert_new_song(name, artist, producer_name):
    query = """INSERT INTO Song (Name, Artist, Producer_Name)
               VALUES (%s, %s, %s)"""
    
    try:
        connection = get_connection('Music_Database')
        with connection.cursor() as cursor:
            cursor.execute(query, (name, artist, producer_name))
            connection.commit()  # Commit the transaction
            print(f"{GREEN}Inserted new song {name}.{RESET}")
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        connection.close()


# 13. Insert a New Song Review
def insert_new_song_review(review_id, review_date, rating, comments, song_name):
    query = """INSERT INTO Song_Review (Review_ID, Review_Date, Rating, Comments, Song_Name)
               VALUES (%s, %s, %s, %s, %s)"""
    
    try:
        connection = get_connection('Music_Database')
        with connection.cursor() as cursor:
            cursor.execute(query, (review_id, review_date, rating, comments, song_name))
            connection.commit()  # Commit the transaction
            print(f"{GREEN}Inserted new review for song {song_name}.{RESET}")
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        connection.close()


#14 Delete a Song Review
def delete_song_review(review_id):
    query = """DELETE FROM Song_Review WHERE Review_ID = %s"""
    
    try:
        connection = get_connection('Music_Database')
        with connection.cursor() as cursor:
            cursor.execute(query, (review_id,))
            connection.commit()  # Commit the transaction
            print(f"{GREEN}Deleted review with ID {review_id}{RESET}.")
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        connection.close()


# Function to display the menu and allow user selection
def display_menu():
    print("Select a query to execute:")
    print(f"{BLUE}Selection Queries{RESET}")
    print("1.View Artists with Stage Name Starting with 'B'")

    print(f"{BLUE}Projection Queries{RESET}")
    print("2. Get Reviews of a Song")
    print("3. Get Producer's Future Projects")

    print(f"{BLUE}Aggregrate function Queries{RESET}")
    print("4. Get the Average Rating for an Album")
    print("5. Get Total Collections of All Albums")

    print(f"{BLUE}Search Queries{RESET}")
    print("Analysis Queries")
    print("7. Get all songs with above average rating")

    print("Updation Queries")
    print(f"{BLUE}Updation Queries{RESET}")
    print("8. Update Rating for a Song Review")
    print("9. Update the Number of Platforms for a Distribution")
    print("10. Update Role of an Artist")

    print(f"{BLUE}Insertion Queries{RESET}")
    print("11. Insert a New Artist")
    print("12. Insert a New Song")
    print("12. Insert a New Song Review")

    print(f"{BLUE}Deletion Queries{RESET}")
    print("14. Delete a Song Review")
    choice = input(f"{MAGENTA}Enter the number of the query to execute (1-15): {RESET}")

    return choice

# Function to handle user input and execute the appropriate query
def handle_user_choice(choice):
    if choice == "1":
        result = get_artists_starting_with_b()
        print(f"{GREEN}{result}{RESET}")

    elif choice == "2":
        song_name = input(f"{MAGENTA}Enter the song's name: {RESET}")
        result = get_song_reviews(song_name)
        print(f"{GREEN}{result}{RESET}")

    elif choice == "3":
        producer_name = input(f"{MAGENTA}Enter the producer's name: {RESET}")
        result = get_producer_upcoming_projects(producer_name)
        print(f"{GREEN}{result}{RESET}")
    
    elif choice == "4":
        album_id = input(f"{MAGENTA}Enter the album ID: {RESET}")
        result = get_average_album_rating(album_id)
        print(f"{GREEN}{result}{RESET}")
    
    elif choice == "5":
        result = get_total_album_collections()
        print(f"{GREEN}{result}{RESET}")

    elif choice == "6":
        name_partial = input(f"{MAGENTA}Enter a partial name to search: {RESET}")
        result = find_artists_matching_name(name_partial)
        print(f"{GREEN}{result}{RESET}")
    
    elif choice == "7":
        result = get_songs_above_average_by_rating()
        print(f"Songs above average rating:")
        print(f"{GREEN}{result}{RESET}")
        
    elif choice == "8":
        review_id = input(f"{MAGENTA}Enter the review ID to update: {RESET}")
        new_rating = input(f"{MAGENTA}Enter the new rating: {RESET}")
        update_song_review_rating(review_id, new_rating)
    
    elif choice == "9":
        distribution_name = input(f"{MAGENTA}Enter the distribution name: {RESET}")
        new_platform_count = input(f"{MAGENTA}Enter the new platform count: {RESET}")
        update_distribution_platforms(distribution_name, new_platform_count)
   
    elif choice == "10":
        stage_name = input(f"{MAGENTA}Enter the artist's stage name: {RESET}")
        old_role = input(f"{MAGENTA}Enter the old role: {RESET}")
        new_role = input(f"{MAGENTA}Enter the new role: {RESET}")
        update_artist_role(stage_name, old_role, new_role)
    
    elif choice == "11":
        name = input(f"{MAGENTA}Enter the artist's name: {RESET}")
        stage_name = input(f"{MAGENTA}Enter the artist's stage name: {RESET}")
        insert_new_artist(name, stage_name)

    elif choice == "12":
        name = input(f"{MAGENTA}Enter the song name: {RESET}")
        artist = input(f"{MAGENTA}Enter the artist's name: {RESET}")
        producer_name = input(f"{MAGENTA}Enter the producer's name: {RESET}")
        insert_new_song(name, artist, producer_name)
    
    elif choice == "13":
        review_id = input(f"{MAGENTA}Enter the review ID: {RESET}")
        review_date = input(f"{MAGENTA}Enter the review date: {RESET}")
        rating = input(f"{MAGENTA}Enter the rating: {RESET}")
        comments = input(f"{MAGENTA}Enter comments: {RESET}")
        song_name = input(f"{MAGENTA}Enter the song name: {RESET}")
        insert_new_song_review(review_id, review_date, rating, comments, song_name)

    elif choice == "14":
        review_id = input(f"{MAGENTA}Enter the review ID to delete: {RESET}")
        delete_song_review(review_id)


# Main function to run the script
def main():
    while True:
        choice = display_menu()
        handle_user_choice(choice)
        cont = input(f"{MAGENTA}Do you want to execute another query? (yes/no): {RESET}").strip().lower()
        if cont != 'yes':
            print("Goodbye!")
            break

# Execute the main function
if __name__ == '__main__':
    main()

