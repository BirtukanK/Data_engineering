
create table if not exists traffic_data
(id int primary key,
track_id int not null,
v_type varchar(120) NOT null,
traveled_d varchar(120) NOT null,
avg_speed float NOT null,
lat float NOT null,
lon float NOT null,
speed float NOT null,
lon_acc float NOT null,
lat_acc float NOT null,
d_time float NOT null);