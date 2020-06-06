### star schema 

* dim_airport

| field | type | comment |
|:--- |:---|:--- |
| id | string |  primary key |
| type | string |  |
| name | string |  |
| elevation_ft | integer |  |
| state_code | string |  |
| municipality | string |  |
| city_id | long | foreign key (dim_city) |
| gps_code | string |  |
| iata_code | string |  |
| local_code | string |  |
| longitude | double |  |
| latitude | double |  |



* dim_city


| field | type | comment |
|:--- |:---|:--- |
| city_id | long | primary key  |
| city | string |  |
| state_code | string |  |
| state | string |  |
 | median_age | decimal(4,1) | |
| female | integer |  |
| total | integer |  |
| veterans | integer |  |
| foreign_born | integer |  |
 |average_household | decimal(4,2) | |



* dim_date

| field | type | comment |
|:--- |:---|:--- |
| date | date |  primary key  |
| year | integer |  |
| month | integer |  |
| day | integer |  |


* dim_country

| field | type | comment |
|:--- |:---|:--- |
| id | integer |  |
| country | string |  |

* fact_immigration

| field | type | comment |
|:--- |:---|:--- |
| cicid | integer | primary key  |
| i94yr | integer |  |
| i94mon | integer |  |
| i94cit | integer | foreign key ( dim_country) |
| i94res | integer | foreign key ( dim_country) |
| i94port | string |  |
| arrdate | integer |  |
| i94mode | integer |  |
| i94addr | string |  |
| depdate | integer |  |
| i94visa | string |  |
| count | integer |  |
| dtadfile | date | foreign key (dim_date) |
| visapost | string |  |
| occup | string |  |
| entdepa | string |  |
| entdepd | string |  |
| entdepu | string |  |
| matflag | string |  |
| biryear | integer |  |
| dtaddto | date |  |
| gender | string |  |
| insnum | string |  |
| airline | string |  |
| admnum | integer |  |
| fltno | string |  |
| visatype | string |  |
| city_id | long | foreign key (dim_city) |
| airport_id | string | foreign key (dim_airport) |