SELECT MAX(i.ID) FROM trektip.Information i;

SELECT * FROM trektip.Information;


SELECT * FROM trektip.Place;

SELECT * FROM trektip.User;

commit;

SELECT * FROM trektip.Place p
where p.ID='13L';

SELECT * FROM trektip.Attraction;

insert into trektip.Attraction (attractionName,placeName,placeID,description)
values ('%s','%s','%s','%s');

insert into trektip.Attraction (attractionName,placeName,placeID,description)
values ('JzzyParty','Blue Note','1L','This was Great jazz')
where 

alter table trektip.Attraction
add column description varchar(150);

alter table trektip.Attraction
drop column attractionShortDesc;

alter table trektip.Attraction
drop column attractionLongDesc;

SELECT distinct p.placeName, p.placeType,p.description
FROM trektip.Place p, trektip.User u
where p.userName='root';

SELECT  a.placeName 
from trektip.Attraction a;


alter table trektip.Place
drop column shortDesc;


alter table trektip.Place
drop column LongDesc;

-- insert into trektip.Place (placeType, placeName,userName, latitude,longitude)
-- values ('%s','%s','%s','%d','%d');

insert into trektip.Place (placeType, placeName,userName, latitude,longitude,shortDesc)
values ('Bar','BatBar2','root','10.322','3.2522','another bar on earth');

delete from trektip.User
where User.userName='';

SELECT * FROM trektip.Comment;

SELECT * FROM trektip.Attraction a
where a.ID='1L';

select u.userName, p.placeName, a.ID, a.attractionName 
from trektip.Attraction a, trektip.Place p, trektip.User u
where u.userName='test'
and p.userName='test'
and a.placeName='Blue Note';

SELECT distinct c.ID, c.rating, c.infoID, i.infoText
FROM trektip.Comment c, trektip.User u, trektip.Information i
where c.userName='root'
and u.userName='root'
and c.ID=i.commentID;

update trektip.Information as info
set info.infoText='dummy1',
info.infoName='user'
where info.ID=1;

update trektip.Comment as c
set c.infoID=1
where c.ID=1;

update trektip.Comment as c
set c.infoID=
(SELECT MAX(i.ID) FROM trektip.Information i)
where c.ID=2;

SELECT * FROM trektip.User;


select User.firstName from User
where User.userName='root';

select User.lastName from User
where User.userName='root';

select * from Place;

select  trektip.Information.infoName, trektip.Information.infoText 
from trektip.Information
where trektip.Information.infoName='dummy';



update trektip.Information as info
set info.infoType='image0',
info.infoText='test0'
where info.ID=1;



commit;