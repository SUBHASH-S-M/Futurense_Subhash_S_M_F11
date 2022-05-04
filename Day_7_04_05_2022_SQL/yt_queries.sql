create database youtube_data;
use youtube_data;
show tables;
select * from video_details;

select category_id,max(views) from video_details 
group by category_id;
