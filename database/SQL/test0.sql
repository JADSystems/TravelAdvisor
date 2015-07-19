SELECT MAX(i.ID) FROM trektip.Information i;

SELECT * FROM trektip.Information;

SELECT * FROM trektip.Comment;

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