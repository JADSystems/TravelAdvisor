


create table Information
(
	ID INT NOT NULL UNIQUE,
    infoType varchar(50),
    infoText varchar(500),
    image longblob,
    video longblob,
    
    primary  key(ID)
    
);

insert into Information (ID,infoType,infoText,image,video)
values (0,'','','','');
insert into Information (ID,infoType,infoText,image,video)
values (1,'','','','');


create table Comment
(
	ID INT UNIQUE NOT NULL,
    contentID INT UNIQUE,
    rating INT,
    
    foreign key(contentID) references Information(ID)
);

insert into Comment( ID, contentID, rating)
values (0,0,0);

create table Attraction
(
	ID int NOT NULL AUTO_INCREMENT,
    attractionName varchar(50) UNIQUE,
    staticInfoID INT UNIQUE,
    userInfoID INT UNIQUE,
    
    
    primary key (ID),
    foreign key(staticInfoID) references Information(ID),
    foreign key(userInfoID) references Information(ID)
);

insert into Attraction(ID, attractionName,staticInfoID,userInfoID)
values (0,'dummy',0,0);

insert into Attraction(ID, attractionName,staticInfoID,userInfoID)
values (2,'dummy2',1,1);

create table Place
(
	ID int NOT NULL UNIQUE, 
    placeType varchar(50),
    placeName varchar(50),
    staticInfoID INT UNIQUE,
    userInfoID INT UNIQUE,
    attractionID INT unique,
    
    primary key(ID),
    foreign key(staticInfoID) references Information(ID),
    foreign key(userInfoID) references Information(ID),
    foreign key (attractionID) references Attraction(ID)
    
    
);

insert into Place(ID, placeType, placeName, staticInfoID, userInfoID, attractionID)
values (0,'','',0,0,1);

insert into Place(ID, placeType, placeName, staticInfoID, userInfoID, attractionID)
values (1,'State','Florida',1,1,2);

create table User
(
	ID int NOT NULL auto_increment, 
    userName varchar(50) NOT NULL UNIQUE,
    userType varchar(50) NOT NULL,
    firstName varchar(50) NOT NULL,
    lastName varchar(50) NOT NULL,
    passKey varchar(50) NOT NULL UNIQUE,
    placeID INT UNIQUE,
    commentID INT UNIQUE, 
    
	PRIMARY KEY (ID),
    foreign key(placeID) references Place(ID),
    foreign key(commentID) references Comment(ID)

);

insert into User (ID, userName, userType, firstName, lastName, passKey, placeID, commentID)
values (1, 'root','admin','Bruce','Wayne','pass0',0,0);

commit;
