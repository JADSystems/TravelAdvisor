


create table Information
(
	ID INT NOT NULL AUTO_INCREMENT,
    infoName varchar(50),
    infoType varchar(50),
    infoText varchar(500),
    image longblob,
    video longblob,
    
    primary  key(ID)
    
);

insert into Information (infoName,infoType,infoText,image,video)
values ('dummy','','','','');
insert into Information (infoName,infoType,infoText,image,video)
values ('dummy2','','','','');
insert into Information (infoName,infoType,infoText,image,video)
values ('','','','','');


create table Comment
(
	ID INT NOT NULL AUTO_INCREMENT,
    contentID INT ,
    rating INT,
    
    foreign key(contentID) references Information(ID),
    Primary Key (ID)
);

insert into Comment( ID, contentID, rating)
values (0,0,0);

create table Attraction
(
	ID int NOT NULL AUTO_INCREMENT,
    attractionName varchar(50) UNIQUE,
    staticInfoID INT ,
    userInfoID INT ,
    
    
    primary key (ID),
    foreign key(staticInfoID) references Information(ID),
    foreign key(userInfoID) references Information(ID)
);

insert into Attraction(attractionName)
values ('dummyAttraction1');

insert into Attraction(attractionName)
values ('dummyAttraction2');

create table Place
(
	ID int NOT NULL AUTO_INCREMENT, 
    placeType varchar(50),
    placeName varchar(50),
    staticInfoID INT,
    userInfoID INT,
    attractionID INT,
    
    primary key(ID),
    foreign key(staticInfoID) references Information(ID),
    foreign key(userInfoID) references Information(ID),
    foreign key (attractionID) references Attraction(ID)
    
    
);

insert into Place( placeType, placeName)
values ('city','Miami');

insert into Place( placeType, placeName)
values ('state','Florida');

create table User
(
	ID int NOT NULL auto_increment, 
    userName varchar(50) NOT NULL UNIQUE,
    userType varchar(50) NOT NULL,
    firstName varchar(50) NOT NULL,
    lastName varchar(50) NOT NULL,
    passKey varchar(50) NOT NULL UNIQUE,
    placeID INT ,
    commentID INT , 
    
	PRIMARY KEY (ID),
    foreign key(placeID) references Place(ID),
    foreign key(commentID) references Comment(ID)

);

insert into User (userName, userType, firstName, lastName, passKey)
values ('root','admin','Bruce','Wayne','pass0');
insert into User (userName, userType, firstName, lastName, passKey)
values ('test','admin','Jim','Gordon','pass1');

commit;
