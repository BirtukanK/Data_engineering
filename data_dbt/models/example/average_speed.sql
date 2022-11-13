with stored_data as (
    select *
    from {{ source('traffic_db', 'traffic_table') }}
),

avg_data as (
    select
        v_type,
        AVG(speed)
    from stored_data
    group by v_type
)
SELECT *
FROM avg_data