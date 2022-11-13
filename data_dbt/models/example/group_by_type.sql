with stored_data as (
    select *
    from {{ source('traffic_db', 'traffic_table') }}
),

type_data as (
    select
        v_type
        
    from stored_data
    group by v_type
)
SELECT *
FROM type_data