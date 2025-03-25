-- Create Database
CREATE DATABASE IF NOT EXISTS MusicDatabase;
USE MusicDatabase;

-- Artist Table
CREATE TABLE Artist (
  Name VARCHAR(255),
  Stage_name VARCHAR(255) PRIMARY KEY
);

-- ArtistStatistics Table
CREATE TABLE ArtistStatistics (
  Stage_name VARCHAR(255) PRIMARY KEY,
  Hits INT,
  Flops INT,
  FOREIGN KEY (Stage_name) REFERENCES Artist(Stage_name)
);

-- ArtistRole Table
CREATE TABLE ArtistRole (
  Stage_name VARCHAR(255),
  Role VARCHAR(255),
  PRIMARY KEY (Stage_name, Role),
  FOREIGN KEY (Stage_name) REFERENCES Artist(Stage_name)
);

-- ArtistUpcomingProjects Table
CREATE TABLE ArtistUpcomingProjects (
  Stage_name VARCHAR(255),
  Project VARCHAR(255),
  PRIMARY KEY (Stage_name, Project),
  FOREIGN KEY (Stage_name) REFERENCES Artist(Stage_name)
);

-- Producer Table
CREATE TABLE Producer (
  Name VARCHAR(255) PRIMARY KEY,
  Debut_Year YEAR
);

-- ProducerStatistics Table
CREATE TABLE ProducerStatistics (
  Name VARCHAR(255) PRIMARY KEY,
  Hits INT,
  Flops INT,
  FOREIGN KEY (Name) REFERENCES Producer(Name)
);

-- Distribution Table
CREATE TABLE Distribution (
  Name VARCHAR(255),
  No_of_platforms INT,
  Release_date YEAR,
  PRIMARY KEY (Name, Release_date)
);

-- Award Table
CREATE TABLE Award (
  Name VARCHAR(255),
  Level INT,
  Year YEAR,
  Album_ID INT,
  PRIMARY KEY (Name, Year)
);

-- Album Table
CREATE TABLE Album (
  Album_ID INT PRIMARY KEY,
  Release_year YEAR,
  Duration INT,
  Budget INT,
  Stage_Name VARCHAR(255),
  Distribution_Name VARCHAR(255),
  Release_date YEAR,
  FOREIGN KEY (Stage_Name) REFERENCES Artist(Stage_name),
  FOREIGN KEY (Distribution_Name, Release_date) REFERENCES Distribution(Name, Release_date)
);

-- AlbumStatistics Table
CREATE TABLE AlbumStatistics (
  Album_ID INT PRIMARY KEY,
  Collections INT,
  FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID)
);

-- AlbumAwards Table
CREATE TABLE AlbumAwards (
  Album_ID INT,
  Award_Name VARCHAR(255),
  Award_Year YEAR,
  PRIMARY KEY (Album_ID, Award_Name, Award_Year),
  FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID),
  FOREIGN KEY (Award_Name, Award_Year) REFERENCES Award(Name, Year)
);

-- AlbumGenre Table
CREATE TABLE AlbumGenre (
  Album_ID INT,
  Genre VARCHAR(255),
  PRIMARY KEY (Album_ID, Genre),
  FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID)
);

-- Song Table
CREATE TABLE Song (
  Name VARCHAR(255) PRIMARY KEY,
  Artist VARCHAR(255),
  Producer_Name VARCHAR(255),
  FOREIGN KEY (Artist) REFERENCES Artist(Stage_name),
  FOREIGN KEY (Producer_Name) REFERENCES Producer(Name)
);

-- SongLyrics Table
CREATE TABLE SongLyrics (
  Lyrics_ID INT PRIMARY KEY,
  Song_Name VARCHAR(255),
  Lyric_Line VARCHAR(255),
  Line_Number INT,
  FOREIGN KEY (Song_Name) REFERENCES Song(Name)
);

-- SongMedia Table
CREATE TABLE SongMedia (
  Media_ID INT PRIMARY KEY,
  Song_Name VARCHAR(255),
  Media_Type VARCHAR(255),
  Media_URL VARCHAR(255),
  FOREIGN KEY (Song_Name) REFERENCES Song(Name)
);

-- ProducerAlbumIDs Table
CREATE TABLE ProducerAlbumIDs (
  Name VARCHAR(255),
  Album_ID INT,
  PRIMARY KEY (Name, Album_ID),
  FOREIGN KEY (Name) REFERENCES Producer(Name),
  FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID)
);

-- ProducerUpcomingProjects Table
CREATE TABLE ProducerUpcomingProjects (
  Name VARCHAR(255),
  Project VARCHAR(255),
  PRIMARY KEY (Name, Project),
  FOREIGN KEY (Name) REFERENCES Producer(Name)
);

-- Album_Review Table
CREATE TABLE Album_Review (
  Review_ID INT,
  Review_Date DATE,
  Rating FLOAT,
  Comments VARCHAR(255),
  Album_ID INT,
  PRIMARY KEY (Review_ID, Review_Date),
  FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID)
);

-- Song_Review Table
CREATE TABLE Song_Review (
  Review_ID INT,
  Review_Date DATE,
  Rating FLOAT,
  Comments VARCHAR(255),
  Song_Name VARCHAR(255),
  PRIMARY KEY (Review_ID, Review_Date),
  FOREIGN KEY (Song_Name) REFERENCES Song(Name)
);

-- Concert Table
CREATE TABLE Concert (
  Concert_ID INT PRIMARY KEY,
  Date DATE,
  Location VARCHAR(255),
  Stage_Name VARCHAR(255),
  Album_ID INT,
  FOREIGN KEY (Stage_Name) REFERENCES Artist(Stage_name),
  FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID)
);

-- Performs Table
CREATE TABLE Performs (
  Stagename VARCHAR(255),
  Song_name VARCHAR(255),
  Producer_name VARCHAR(255),
  PRIMARY KEY (Stagename, Song_name, Producer_name),
  FOREIGN KEY (Stagename) REFERENCES Artist(Stage_name),
  FOREIGN KEY (Song_name) REFERENCES Song(Name),
  FOREIGN KEY (Producer_name) REFERENCES Producer(Name)
);

-- BelongsTo Table
CREATE TABLE BelongsTo (
  BelongsTo_ID INT PRIMARY KEY,
  Song_name VARCHAR(255),
  Producer_name VARCHAR(255),
  Album_id INT,
  FOREIGN KEY (Song_name) REFERENCES Song(Name),
  FOREIGN KEY (Producer_name) REFERENCES Producer(Name),
  FOREIGN KEY (Album_id) REFERENCES Album(Album_ID)
);

-- ProducedBy Table
CREATE TABLE ProducedBy (
  ProducedBy_ID INT PRIMARY KEY,
  Album_id INT,
  Producer_name VARCHAR(255),
  FOREIGN KEY (Album_id) REFERENCES Album(Album_ID),
  FOREIGN KEY (Producer_name) REFERENCES Producer(Name)
);

-- Features Table
CREATE TABLE Features (
  Feature_ID INT PRIMARY KEY,
  Stagename VARCHAR(255),
  Song_name VARCHAR(255),
  Producer_name VARCHAR(255),
  Album_id INT,
  FOREIGN KEY (Stagename) REFERENCES Artist(Stage_name),
  FOREIGN KEY (Song_name) REFERENCES Song(Name),
  FOREIGN KEY (Producer_name) REFERENCES Producer(Name),
  FOREIGN KEY (Album_id) REFERENCES Album(Album_ID)
);

-- ConcertBy Table
CREATE TABLE ConcertBy (
  ConcertBy_ID INT PRIMARY KEY,
  Stagename VARCHAR(255),
  Album_id INT,
  Concert_ID INT,
  FOREIGN KEY (Stagename) REFERENCES Artist(Stage_name),
  FOREIGN KEY (Album_id) REFERENCES Album(Album_ID),
  FOREIGN KEY (Concert_ID) REFERENCES Concert(Concert_ID)
);

-- Artist Table
INSERT INTO Artist (Name, Stage_name) VALUES 
('Ed Sheeran', 'EdSheer'),
('Billie Eilish', 'Billie');

-- Producer Table
INSERT INTO Producer (Name, Debut_Year) VALUES 
('Max Martin', 1990),
('Finneas', 2015);

-- Distribution Table
INSERT INTO Distribution (Name, No_of_platforms, Release_date) VALUES 
('Universal Music', 20, 2021),
('Atlantic Records', 18, 2022);

-- Award Table
INSERT INTO Award (Name, Level, Year, Album_ID) VALUES 
('Grammy', 1, 2022, 1),
('Billboard Music Award', 2, 2021, 2);

-- Album Table
INSERT INTO Album (Album_ID, Release_year, Duration, Budget, Stage_Name, Distribution_Name, Release_date) VALUES 
(1, 2021, 45, 500000, 'EdSheer', 'Universal Music', 2021),
(2, 2022, 40, 600000, 'Billie', 'Atlantic Records', 2022);

-- ArtistStatistics Table
INSERT INTO ArtistStatistics (Stage_name, Hits, Flops) VALUES 
('EdSheer', 10, 2),
('Billie', 8, 1);

-- ArtistRole Table
INSERT INTO ArtistRole (Stage_name, Role) VALUES 
('EdSheer', 'Singer'),
('EdSheer', 'Songwriter'),
('Billie', 'Singer'),
('Billie', 'Songwriter');

-- ArtistUpcomingProjects Table
INSERT INTO ArtistUpcomingProjects (Stage_name, Project) VALUES 
('EdSheer', 'World Tour 2024'),
('Billie', 'New Album Release');

-- ProducerStatistics Table
INSERT INTO ProducerStatistics (Name, Hits, Flops) VALUES 
('Max Martin', 50, 5),
('Finneas', 15, 2);

-- AlbumStatistics Table
INSERT INTO AlbumStatistics (Album_ID, Collections) VALUES 
(1, 1000000),
(2, 1200000);

-- AlbumAwards Table
INSERT INTO AlbumAwards (Album_ID, Award_Name, Award_Year) VALUES 
(1, 'Grammy', 2022),
(2, 'Billboard Music Award', 2021);

-- AlbumGenre Table
INSERT INTO AlbumGenre (Album_ID, Genre) VALUES 
(1, 'Pop'),
(2, 'Alternative');

-- Song Table
INSERT INTO Song (Name, Artist, Producer_Name) VALUES 
('Perfect', 'EdSheer', 'Max Martin'),
('Bad Guy', 'Billie', 'Finneas');

-- SongLyrics Table
INSERT INTO SongLyrics (Lyrics_ID, Song_Name, Lyric_Line, Line_Number) VALUES 
(1, 'Perfect', 'I found a love for me', 1),
(2, 'Bad Guy', 'White shirt, now red', 1);

-- SongMedia Table
INSERT INTO SongMedia (Media_ID, Song_Name, Media_Type, Media_URL) VALUES 
(1, 'Perfect', 'Music Video', 'https://youtu.be/2Vv-BfVoq4g'),
(2, 'Bad Guy', 'Music Video', 'https://youtu.be/HUHC9tYz8ik');

-- ProducerAlbumIDs Table
INSERT INTO ProducerAlbumIDs (Name, Album_ID) VALUES 
('Max Martin', 1),
('Finneas', 2);

-- ProducerUpcomingProjects Table
INSERT INTO ProducerUpcomingProjects (Name, Project) VALUES 
('Max Martin', 'Pop Collaboration'),
('Finneas', 'Sister Album');

-- Album_Review Table
INSERT INTO Album_Review (Review_ID, Review_Date, Rating, Comments, Album_ID) VALUES 
(1, '2021-06-15', 4.5, 'Excellent album', 1),
(2, '2022-07-20', 4.7, 'Groundbreaking work', 2);

-- Song_Review Table
INSERT INTO Song_Review (Review_ID, Review_Date, Rating, Comments, Song_Name) VALUES 
(1, '2021-05-10', 4.8, 'Beautiful composition', 'Perfect'),
(2, '2022-06-15', 4.6, 'Unique sound', 'Bad Guy');

-- Concert Table
INSERT INTO Concert (Concert_ID, Date, Location, Stage_Name, Album_ID) VALUES 
(1, '2023-01-15', 'London', 'EdSheer', 1),
(2, '2023-02-20', 'Los Angeles', 'Billie', 2);

-- Performs Table
INSERT INTO Performs (Stagename, Song_name, Producer_name) VALUES 
('EdSheer', 'Perfect', 'Max Martin'),
('Billie', 'Bad Guy', 'Finneas');

-- BelongsTo Table
INSERT INTO BelongsTo (BelongsTo_ID, Song_name, Producer_name, Album_id) VALUES 
(1, 'Perfect', 'Max Martin', 1),
(2, 'Bad Guy', 'Finneas', 2);

-- ProducedBy Table
INSERT INTO ProducedBy (ProducedBy_ID, Album_id, Producer_name) VALUES 
(1, 1, 'Max Martin'),
(2, 2, 'Finneas');

-- Features Table
INSERT INTO Features (Feature_ID, Stagename, Song_name, Producer_name, Album_id) VALUES 
(1, 'EdSheer', 'Perfect', 'Max Martin', 1),
(2, 'Billie', 'Bad Guy', 'Finneas', 2);

-- ConcertBy Table
INSERT INTO ConcertBy (ConcertBy_ID, Stagename, Album_id, Concert_ID) VALUES 
(1, 'EdSheer', 1, 1),
(2, 'Billie', 2, 2);