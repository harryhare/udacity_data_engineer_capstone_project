* dim_airport

| column name | description | comment |
| :--- | :--- | :--- | 
| id | airport id |  primary key |
| type | airport type |
| name | airport full name |
| elevation_ft | elevation of airport in foot |
| state_code | state code |
| municipality | the city where airport is build |
| city_id | the city id of municipality | foreign key |
| gps_code | gps code |
| iata_code | iata code |
| local_code | local code |
| longitude | longitude of the airport |
| latitude | latitude of the airport |

* dim_city

| column name | description | comment |
| :--- | :--- | :--- | 
| city_id | city id | auto generate, unique, primary key |
| city | city name|
| state_code | state code |
| state | state full name |
| median_age | median age |
| male | male population |
| female | female population |
| total | total population|
| veterans | veterans population|
| foreign_born | foreign born population |
| average_household | average household number |

* dim_date

| column name | description | comment |
| :--- | :--- | :--- | 
| date | date | DateType, primary key, unique
| year | year |
| month | month |
| day | day |


* dim_country

| column name | description | comment |
| :--- | :--- | :--- | 
| id | id | id, primary key , unique |
| country | country full name|


* fact_immigration:

| column name | description | comment |
| :--- | :--- | :--- |
| cicid | id | primary key |
| i94yr | year |
| i94mon | month |
| i94cit | country of citizenship | foreign key (dim_county) |
| i94res | country of residency | foreign key (dim_county) |
| i94port | port of arrival |
| arrdate | arrival date |
| i94mode | transportation mode |
| i94addr | state of arrival |
| depdate | departure date |
| i94bir | age|
| i94visa | visa category |
| count | number of people |
| dtadfile | character date | foreign key (dim_date)|
| visapost | department issuing visa |
| occup | occupation |
| entdepa | arrival flag |
| entdepd | departure flag |
| entdepu | update flag |
| matflag | match flag |
| biryear | year of birth |
| dtaddto | character date |
| gender | gender |
| insnum | ins number |
| airline | airline |
| admnum | admission number |
| fltno | flight number |
| visatype | visa type |
| city_id | city id | foreign key(dim_city) |
| airport_id | airport id | foreigi_key(dim_airport) |

