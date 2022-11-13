with stored_data as (
    select *
    from {{ source('traffic_db', 'traffic_table') }}
),

time_data as (
    select
        d_time,
        COUNT(*)
    from {{ source('traffic_db', 'traffic_table') }}
    group by d_time
)
SELECT * FROM time_data


