COPY traffic_data(id,track_id, v_type, traveled_d, avg_speed, lat, lon, speed, lon_acc, lat_acc, d_time)
FROM '/Home/Documents/data_engineering/data/data_1.csv'
DELIMITER ','
CSV HEADER;