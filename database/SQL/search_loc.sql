CREATE DEFINER=`root`@`%` PROCEDURE `search_loc`(in searchLat double,
    searchLong double)
begin
	SET @buffer = CONCAT_WS('',
		'select a.attractionName,
			    p.placeName from Attraction a
		join Place p
		on a.placeID = p.ID
		where ', searchLat, ' <= latitude + 0.5 and ',searchLong, ' <= longitude + 0.5 and
			  ', searchLat, ' >= latitude - 0.5 and ',searchLong, ' >= longitude - 0.5');
    PREPARE stmt FROM @buffer;
    EXECUTE stmt;

    DEALLOCATE PREPARE stmt;

end