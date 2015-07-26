
CREATE SCHEMA `trektip` ;


create table User
(
	ID int NOT NULL auto_increment, 
    userName varchar(50) NOT NULL UNIQUE,
    userType varchar(50) NOT NULL,
    firstName varchar(50) NOT NULL,
    lastName varchar(50) NOT NULL,
    passKey varchar(50) NOT NULL UNIQUE,
    email varchar(50),
--    placeID INT ,
--    commentID INT , 
    
	PRIMARY KEY (ID)
--    foreign key(placeID) references Place(ID),
--    foreign key(commentID) references Comment(ID)

);

insert into trektip.User (userName, userType, firstName, lastName, passKey)
values ('root','admin','Bruce','Wayne','pass0');
insert into User (userName, userType, firstName, lastName, passKey)
values ('test','admin','Jim','Gordon','pass1');

create table Comment
(
	ID INT NOT NULL AUTO_INCREMENT,
    rating INT,
    userName varchar(50) NOT NULL,
    infoID INT,
  
    foreign key(userName) references User(userName),
    Primary Key (ID)
);

alter table Comment
add foreign key (infoID)
references Information(ID);

alter table Comment
drop foreign key Comment_ibfk_2;

insert into Comment(rating, userName)
values (5,'root');

create table Place
(
	ID int NOT NULL AUTO_INCREMENT, 
    placeType varchar(50) NOT NULL,
    placeName varchar(50) NOT NULL UNIQUE,
    userName varchar (50) NOT NULL,
    address varchar (100),
    latitude INT,
    longitude INT,
    googleID varchar (50), 
    
    primary key(ID),
	foreign key(userName) references User(userName)
    
    
);

insert into Place( placeType, placeName,userName)
values ('club','Miami','root');

insert into Place( placeType, placeName,userName)
values ('bar','Blue Note','test');


create table Attraction
(
	ID int NOT NULL AUTO_INCREMENT,
    attractionName varchar(50) NOT NULL UNIQUE,
    placeName varchar(50) not null,
    
    
    
    primary key (ID),
    foreign key(placeName) references Place(placeName)
);

insert into Attraction(attractionName,placeName)
values ('dummyAttraction1','Miami');

insert into Attraction(attractionName,placeName)
values ('dummyAttraction2','Miami');

insert into Attraction(attractionName,placeName)
values ('dummyAttraction3','Miami');

insert into Attraction(attractionName,placeName)
values ('dummyAttraction Blue Note 1','Blue Note');

insert into Attraction(attractionName,placeName)
values ('dummyAttraction Blue Note 2','Blue Note');

create table Information
(
	ID INT NOT NULL AUTO_INCREMENT,
    infoName varchar(50) NOT NULL ,
-- infoName= comment,placeDescription,attractionDescription;
-- infoType=user,static;
    infoType varchar(50) NOT NULL,
    infoText varchar(500),
    placeName varchar(50),
    attractionName varchar(50),
    commentID INT UNIQUE,
    image longblob,
    video longblob,
    
    primary  key(ID),
    foreign key (placeName) references Place(placeName),
    foreign key (attractionName) references Attraction (attractionName),
    foreign key (commentID) references Comment(ID)
    
);

insert into Information (infoName,infoType,infoText, commentID)
values ('dummy','comment','user',1);
insert into Information (infoName,infoType,infoText, commentID)
values ('dummy2','comment','user',2);
insert into Information (infoName,infoType,infoText, commentID)
values ('dummy3','comment','user',1);

commit;
