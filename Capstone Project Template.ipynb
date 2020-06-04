{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "editable": true
   },
   "source": [
    "# Project Title\n",
    "### Data Engineering Capstone Project\n",
    "\n",
    "#### Project Summary\n",
    "\n",
    "The project uses spark to load and do etl with U.S. immigration data. \n",
    "\n",
    "The project saves the processed result locally with parquet format.\n",
    "\n",
    "The project follows the follow steps:\n",
    "* Step 1: Scope the Project and Gather Data\n",
    "* Step 2: Explore and Assess the Data\n",
    "* Step 3: Define the Data Model\n",
    "* Step 4: Run ETL to Model the Data\n",
    "* Step 5: Complete Project Write Up"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from pyspark.sql import SparkSession\n",
    "from pyspark.sql.functions import udf, col\n",
    "from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format,dayofweek\n",
    "from pyspark.sql.functions import expr\n",
    "from pyspark.sql.functions import unix_timestamp,from_unixtime\n",
    "from pyspark.sql.types import IntegerType,TimestampType\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": [
    "# init spark\n",
    "spark = SparkSession.builder.\\\n",
    "config(\"spark.jars.packages\",\"saurfang:spark-sas7bdat:2.0.0-s_2.11\")\\\n",
    ".enableHiveSupport().getOrCreate()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "editable": true
   },
   "source": [
    "### Step 1: Scope the Project and Gather Data\n",
    "\n",
    "#### Scope \n",
    "\n",
    "* goals: processed the date to fact tables and dimesion tables \n",
    "\n",
    "* tools: Spark\n",
    "\n",
    "#### Describe and Gather Data \n",
    "\n",
    "| data | from | local dir | link |   \n",
    "|:---|:---|:---|:---|\n",
    "| I94 Immigration Data | US National Tourism and Trade Office |/data/18-83510-I94-Data-2016/ | https://travel.trade.gov/research/reports/i94/historical/2016.html |\n",
    "| World Temperature Data | Kaggle | /data2/GlobalLandTemperaturesByCity.csv | https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data |\n",
    "| U.S. City Demographic Data | OpenSoft| /home/workspace/us-cities-demographics.csv  | https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/ |\n",
    "| Airport Code Table | datahub.io | /home/workspace/airport-codes_csv.csv  | https://datahub.io/core/airport-codes#data |"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": [
    "airport_file = \"/home/workspace/airport-codes_csv.csv\"\n",
    "city_fiele = \"/home/workspace/us-cities-demographics.csv\"\n",
    "temperature_file = \"/data2/GlobalLandTemperaturesByCity.csv\"\n",
    "immigration_dir = \"/data/18-83510-I94-Data-2016/\"\n",
    "immigration_dimesions= \"/data/I94_SAS_Labels_Descriptions.SAS\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "editable": true
   },
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'NoneType' object has no attribute 'lower'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-10-dd71b018e884>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mpd_immigration_dimesions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_sas\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mimmigration_dimesions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/opt/conda/lib/python3.6/site-packages/pandas/io/sas/sasreader.py\u001b[0m in \u001b[0;36mread_sas\u001b[0;34m(filepath_or_buffer, format, index, encoding, chunksize, iterator)\u001b[0m\n\u001b[1;32m     50\u001b[0m             \u001b[0;32mpass\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     51\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 52\u001b[0;31m     \u001b[0;32mif\u001b[0m \u001b[0mformat\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlower\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'xport'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     53\u001b[0m         \u001b[0;32mfrom\u001b[0m \u001b[0mpandas\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mio\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msas\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msas_xport\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mXportReader\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     54\u001b[0m         reader = XportReader(filepath_or_buffer, index=index,\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'NoneType' object has no attribute 'lower'"
     ]
    }
   ],
   "source": [
    "pd_immigration_dimesions=pd.read_sas(immigration_dimesions)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": [
    "# Read in the data here\n",
    "pd_airport = pd.read_csv(airport_file,header=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "editable": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ident</th>\n",
       "      <th>type</th>\n",
       "      <th>name</th>\n",
       "      <th>elevation_ft</th>\n",
       "      <th>continent</th>\n",
       "      <th>iso_country</th>\n",
       "      <th>iso_region</th>\n",
       "      <th>municipality</th>\n",
       "      <th>gps_code</th>\n",
       "      <th>iata_code</th>\n",
       "      <th>local_code</th>\n",
       "      <th>coordinates</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>00A</td>\n",
       "      <td>heliport</td>\n",
       "      <td>Total Rf Heliport</td>\n",
       "      <td>11.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>US</td>\n",
       "      <td>US-PA</td>\n",
       "      <td>Bensalem</td>\n",
       "      <td>00A</td>\n",
       "      <td>NaN</td>\n",
       "      <td>00A</td>\n",
       "      <td>-74.93360137939453, 40.07080078125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>00AA</td>\n",
       "      <td>small_airport</td>\n",
       "      <td>Aero B Ranch Airport</td>\n",
       "      <td>3435.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>US</td>\n",
       "      <td>US-KS</td>\n",
       "      <td>Leoti</td>\n",
       "      <td>00AA</td>\n",
       "      <td>NaN</td>\n",
       "      <td>00AA</td>\n",
       "      <td>-101.473911, 38.704022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>00AK</td>\n",
       "      <td>small_airport</td>\n",
       "      <td>Lowell Field</td>\n",
       "      <td>450.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>US</td>\n",
       "      <td>US-AK</td>\n",
       "      <td>Anchor Point</td>\n",
       "      <td>00AK</td>\n",
       "      <td>NaN</td>\n",
       "      <td>00AK</td>\n",
       "      <td>-151.695999146, 59.94919968</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>00AL</td>\n",
       "      <td>small_airport</td>\n",
       "      <td>Epps Airpark</td>\n",
       "      <td>820.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>US</td>\n",
       "      <td>US-AL</td>\n",
       "      <td>Harvest</td>\n",
       "      <td>00AL</td>\n",
       "      <td>NaN</td>\n",
       "      <td>00AL</td>\n",
       "      <td>-86.77030181884766, 34.86479949951172</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>00AR</td>\n",
       "      <td>closed</td>\n",
       "      <td>Newport Hospital &amp; Clinic Heliport</td>\n",
       "      <td>237.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>US</td>\n",
       "      <td>US-AR</td>\n",
       "      <td>Newport</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-91.254898, 35.6087</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  ident           type                                name  elevation_ft  \\\n",
       "0   00A       heliport                   Total Rf Heliport          11.0   \n",
       "1  00AA  small_airport                Aero B Ranch Airport        3435.0   \n",
       "2  00AK  small_airport                        Lowell Field         450.0   \n",
       "3  00AL  small_airport                        Epps Airpark         820.0   \n",
       "4  00AR         closed  Newport Hospital & Clinic Heliport         237.0   \n",
       "\n",
       "  continent iso_country iso_region  municipality gps_code iata_code  \\\n",
       "0       NaN          US      US-PA      Bensalem      00A       NaN   \n",
       "1       NaN          US      US-KS         Leoti     00AA       NaN   \n",
       "2       NaN          US      US-AK  Anchor Point     00AK       NaN   \n",
       "3       NaN          US      US-AL       Harvest     00AL       NaN   \n",
       "4       NaN          US      US-AR       Newport      NaN       NaN   \n",
       "\n",
       "  local_code                            coordinates  \n",
       "0        00A     -74.93360137939453, 40.07080078125  \n",
       "1       00AA                 -101.473911, 38.704022  \n",
       "2       00AK            -151.695999146, 59.94919968  \n",
       "3       00AL  -86.77030181884766, 34.86479949951172  \n",
       "4        NaN                    -91.254898, 35.6087  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd_airport.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": [
    "df_airport=spark.read.csv(\"airport-codes_csv.csv\",header=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-----+-------------+--------------------+------------+---------+-----------+----------+------------+--------+---------+----------+--------------------+\n",
      "|ident|         type|                name|elevation_ft|continent|iso_country|iso_region|municipality|gps_code|iata_code|local_code|         coordinates|\n",
      "+-----+-------------+--------------------+------------+---------+-----------+----------+------------+--------+---------+----------+--------------------+\n",
      "|  00A|     heliport|   Total Rf Heliport|          11|       NA|         US|     US-PA|    Bensalem|     00A|     null|       00A|-74.9336013793945...|\n",
      "| 00AA|small_airport|Aero B Ranch Airport|        3435|       NA|         US|     US-KS|       Leoti|    00AA|     null|      00AA|-101.473911, 38.7...|\n",
      "| 00AK|small_airport|        Lowell Field|         450|       NA|         US|     US-AK|Anchor Point|    00AK|     null|      00AK|-151.695999146, 5...|\n",
      "| 00AL|small_airport|        Epps Airpark|         820|       NA|         US|     US-AL|     Harvest|    00AL|     null|      00AL|-86.7703018188476...|\n",
      "| 00AR|       closed|Newport Hospital ...|         237|       NA|         US|     US-AR|     Newport|    null|     null|      null| -91.254898, 35.6087|\n",
      "| 00AS|small_airport|      Fulton Airport|        1100|       NA|         US|     US-OK|        Alex|    00AS|     null|      00AS|-97.8180194, 34.9...|\n",
      "| 00AZ|small_airport|      Cordes Airport|        3810|       NA|         US|     US-AZ|      Cordes|    00AZ|     null|      00AZ|-112.165000915527...|\n",
      "| 00CA|small_airport|Goldstone /Gts/ A...|        3038|       NA|         US|     US-CA|     Barstow|    00CA|     null|      00CA|-116.888000488, 3...|\n",
      "| 00CL|small_airport| Williams Ag Airport|          87|       NA|         US|     US-CA|       Biggs|    00CL|     null|      00CL|-121.763427, 39.4...|\n",
      "| 00CN|     heliport|Kitchen Creek Hel...|        3350|       NA|         US|     US-CA| Pine Valley|    00CN|     null|      00CN|-116.4597417, 32....|\n",
      "+-----+-------------+--------------------+------------+---------+-----------+----------+------------+--------+---------+----------+--------------------+\n",
      "only showing top 10 rows\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "55075"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_airport.show(10)\n",
    "df_airport.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": [
    "df_city=spark.read.option(\"header\", True).option(\"delimiter\", \";\").csv(\"us-cities-demographics.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+----------------+-------------+----------+---------------+-----------------+----------------+------------------+------------+----------------------+----------+--------------------+-----+\n",
      "|            City|        State|Median Age|Male Population|Female Population|Total Population|Number of Veterans|Foreign-born|Average Household Size|State Code|                Race|Count|\n",
      "+----------------+-------------+----------+---------------+-----------------+----------------+------------------+------------+----------------------+----------+--------------------+-----+\n",
      "|   Silver Spring|     Maryland|      33.8|          40601|            41862|           82463|              1562|       30908|                   2.6|        MD|  Hispanic or Latino|25924|\n",
      "|          Quincy|Massachusetts|      41.0|          44129|            49500|           93629|              4147|       32935|                  2.39|        MA|               White|58723|\n",
      "|          Hoover|      Alabama|      38.5|          38040|            46799|           84839|              4819|        8229|                  2.58|        AL|               Asian| 4759|\n",
      "|Rancho Cucamonga|   California|      34.5|          88127|            87105|          175232|              5821|       33878|                  3.18|        CA|Black or African-...|24437|\n",
      "|          Newark|   New Jersey|      34.6|         138040|           143873|          281913|              5829|       86253|                  2.73|        NJ|               White|76402|\n",
      "+----------------+-------------+----------+---------------+-----------------+----------------+------------------+------------+----------------------+----------+--------------------+-----+\n",
      "only showing top 5 rows\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "2891"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_city.show(5)\n",
    "df_city.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": [
    "df_temperature=spark.read.option(\"header\", True).csv(\"/data2/GlobalLandTemperaturesByCity.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+----------+------------------+-----------------------------+-----+-------+--------+---------+\n",
      "|        dt|AverageTemperature|AverageTemperatureUncertainty| City|Country|Latitude|Longitude|\n",
      "+----------+------------------+-----------------------------+-----+-------+--------+---------+\n",
      "|1743-11-01|             6.068|           1.7369999999999999|Århus|Denmark|  57.05N|   10.33E|\n",
      "|1743-12-01|              null|                         null|Århus|Denmark|  57.05N|   10.33E|\n",
      "|1744-01-01|              null|                         null|Århus|Denmark|  57.05N|   10.33E|\n",
      "|1744-02-01|              null|                         null|Århus|Denmark|  57.05N|   10.33E|\n",
      "|1744-03-01|              null|                         null|Århus|Denmark|  57.05N|   10.33E|\n",
      "+----------+------------------+-----------------------------+-----+-------+--------+---------+\n",
      "only showing top 5 rows\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "8599212"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_temperature.show(5)\n",
    "df_temperature.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": [
    "#df_spark =spark.read.format('com.github.saurfang.sas.spark').load('../../data/18-83510-I94-Data-2016/i94_apr16_sub.sas7bdat')\n",
    "#df_spark.write.parquet(\"sas_data\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": [
    "#write to parquet\n",
    "df_spark=spark.read.parquet(\"sas_data\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+---------+------+------+------+------+-------+-------+-------+-------+-------+------+-------+-----+--------+--------+-----+-------+-------+-------+-------+-------+--------+------+------+-------+--------------+-----+--------+\n",
      "|    cicid| i94yr|i94mon|i94cit|i94res|i94port|arrdate|i94mode|i94addr|depdate|i94bir|i94visa|count|dtadfile|visapost|occup|entdepa|entdepd|entdepu|matflag|biryear| dtaddto|gender|insnum|airline|        admnum|fltno|visatype|\n",
      "+---------+------+------+------+------+-------+-------+-------+-------+-------+------+-------+-----+--------+--------+-----+-------+-------+-------+-------+-------+--------+------+------+-------+--------------+-----+--------+\n",
      "|5748517.0|2016.0|   4.0| 245.0| 438.0|    LOS|20574.0|    1.0|     CA|20582.0|  40.0|    1.0|  1.0|20160430|     SYD| null|      G|      O|   null|      M| 1976.0|10292016|     F|  null|     QF|9.495387003E10|00011|      B1|\n",
      "+---------+------+------+------+------+-------+-------+-------+-------+-------+------+-------+-----+--------+--------+-----+-------+-------+-------+-------+-------+--------+------+------+-------+--------------+-----+--------+\n",
      "only showing top 1 row\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "3096313"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_spark.show(1)\n",
    "df_spark.take(1)\n",
    "df_spark.head()\n",
    "df_spark.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "editable": true
   },
   "source": [
    "### Step 2: Explore and Assess the Data\n",
    "#### Explore the Data \n",
    "Identify data quality issues, like missing values, duplicate data, etc.\n",
    "\n",
    "#### Cleaning Steps\n",
    "Document steps necessary to clean the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "editable": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3096313"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_spark.select(\"cicid\").distinct().count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-------+------+\n",
      "|i94port| count|\n",
      "+-------+------+\n",
      "|    NYC|485916|\n",
      "|    MIA|343941|\n",
      "|    LOS|310163|\n",
      "|    SFR|152586|\n",
      "|    ORL|149195|\n",
      "|    HHW|142720|\n",
      "|    NEW|136122|\n",
      "|    CHI|130564|\n",
      "|    HOU|101481|\n",
      "|    FTL| 95977|\n",
      "|    ATL| 92579|\n",
      "|    LVG| 89280|\n",
      "|    AGA| 80919|\n",
      "|    WAS| 74835|\n",
      "|    DAL| 71809|\n",
      "|    BOS| 57354|\n",
      "|    SEA| 47719|\n",
      "|    PHO| 38890|\n",
      "|    DET| 37832|\n",
      "|    TAM| 25632|\n",
      "+-------+------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df_spark.groupby(\"i94port\").count().orderBy(col(\"count\"),ascending=False).show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------+-------+\n",
      "|visatype|  count|\n",
      "+--------+-------+\n",
      "|      WT|1309059|\n",
      "|      B2|1117897|\n",
      "|      WB| 282983|\n",
      "|      B1| 212410|\n",
      "|     GMT|  89133|\n",
      "|      F1|  39016|\n",
      "|      E2|  19383|\n",
      "|      CP|  14758|\n",
      "|      E1|   3743|\n",
      "|       I|   3176|\n",
      "|      F2|   2984|\n",
      "|      M1|   1317|\n",
      "|      I1|    234|\n",
      "|     GMB|    150|\n",
      "|      M2|     49|\n",
      "|     SBP|     11|\n",
      "|     CPL|     10|\n",
      "+--------+-------+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df_spark.groupby(\"visatype\").count().orderBy(col(\"count\"),ascending=False).show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-------+-------+\n",
      "|i94mode|  count|\n",
      "+-------+-------+\n",
      "|    1.0|2994505|\n",
      "|    3.0|  66660|\n",
      "|    2.0|  26349|\n",
      "|    9.0|   8560|\n",
      "|   null|    239|\n",
      "+-------+-------+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df_spark.groupby(\"i94mode\").count().orderBy(col(\"count\"),ascending=False).show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "editable": true
   },
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+--------+-------+\n",
      "|visapost|  count|\n",
      "+--------+-------+\n",
      "|    null|1881250|\n",
      "|     MEX|  84720|\n",
      "|     SPL|  65678|\n",
      "|     BNS|  62032|\n",
      "|     GUZ|  48298|\n",
      "|     BGT|  46074|\n",
      "|     CRS|  37137|\n",
      "|     BEJ|  36703|\n",
      "|     SHG|  35507|\n",
      "|     GDL|  30970|\n",
      "|     RDJ|  29943|\n",
      "|     TLV|  28903|\n",
      "|     BMB|  28108|\n",
      "|     MDR|  26497|\n",
      "|     GYQ|  26231|\n",
      "|     SDO|  20924|\n",
      "|     MNL|  19513|\n",
      "|     MTR|  18105|\n",
      "|     LMA|  17479|\n",
      "|     SNJ|  16717|\n",
      "+--------+-------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df_spark.groupby(\"visapost\").count().orderBy(col(\"count\"),ascending=False).show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+------+-------+\n",
      "|gender|  count|\n",
      "+------+-------+\n",
      "|     M|1377224|\n",
      "|     F|1302743|\n",
      "|  null| 414269|\n",
      "|     X|   1610|\n",
      "|     U|    467|\n",
      "+------+-------+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df_spark.groupby(\"gender\").count().orderBy(col(\"count\"),ascending=False).show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-------+-----+\n",
      "|biryear|count|\n",
      "+-------+-----+\n",
      "|   null|  802|\n",
      "| 1902.0|    1|\n",
      "| 1905.0|    1|\n",
      "| 1906.0|    1|\n",
      "| 1907.0|    2|\n",
      "| 1908.0|    2|\n",
      "| 1909.0|    1|\n",
      "| 1911.0|    2|\n",
      "| 1913.0|    1|\n",
      "| 1914.0|    4|\n",
      "| 1915.0|    2|\n",
      "| 1916.0|   24|\n",
      "| 1917.0|   19|\n",
      "| 1918.0|   26|\n",
      "| 1919.0|   52|\n",
      "| 1920.0|   46|\n",
      "| 1921.0|   88|\n",
      "| 1922.0|  104|\n",
      "| 1923.0|  185|\n",
      "| 1924.0|  241|\n",
      "| 1925.0|  319|\n",
      "| 1926.0|  463|\n",
      "| 1927.0|  638|\n",
      "| 1928.0|  884|\n",
      "| 1929.0| 1204|\n",
      "| 1930.0| 1594|\n",
      "| 1931.0| 1999|\n",
      "| 1932.0| 2500|\n",
      "| 1933.0| 2965|\n",
      "| 1934.0| 3784|\n",
      "| 1935.0| 4629|\n",
      "| 1936.0| 5635|\n",
      "| 1937.0| 6813|\n",
      "| 1938.0| 8019|\n",
      "| 1939.0| 9340|\n",
      "| 1940.0|10897|\n",
      "| 1941.0|12305|\n",
      "| 1942.0|14198|\n",
      "| 1943.0|16238|\n",
      "| 1944.0|18559|\n",
      "| 1945.0|19988|\n",
      "| 1946.0|24891|\n",
      "| 1947.0|28451|\n",
      "| 1948.0|29576|\n",
      "| 1949.0|32063|\n",
      "| 1950.0|33667|\n",
      "| 1951.0|34141|\n",
      "| 1952.0|37002|\n",
      "| 1953.0|38333|\n",
      "| 1954.0|41352|\n",
      "| 1955.0|43914|\n",
      "| 1956.0|45950|\n",
      "| 1957.0|44921|\n",
      "| 1958.0|45853|\n",
      "| 1959.0|47674|\n",
      "| 1960.0|49722|\n",
      "| 1961.0|50288|\n",
      "| 1962.0|53865|\n",
      "| 1963.0|55673|\n",
      "| 1964.0|56579|\n",
      "| 1965.0|57312|\n",
      "| 1966.0|58946|\n",
      "| 1967.0|56041|\n",
      "| 1968.0|57420|\n",
      "| 1969.0|58127|\n",
      "| 1970.0|59730|\n",
      "| 1971.0|62075|\n",
      "| 1972.0|62001|\n",
      "| 1973.0|61430|\n",
      "| 1974.0|62150|\n",
      "| 1975.0|62622|\n",
      "| 1976.0|66568|\n",
      "| 1977.0|63035|\n",
      "| 1978.0|64262|\n",
      "| 1979.0|66494|\n",
      "| 1980.0|67960|\n",
      "| 1981.0|69626|\n",
      "| 1982.0|70251|\n",
      "| 1983.0|70415|\n",
      "| 1984.0|69809|\n",
      "| 1985.0|70409|\n",
      "| 1986.0|71958|\n",
      "| 1987.0|67762|\n",
      "| 1988.0|65566|\n",
      "| 1989.0|60340|\n",
      "| 1990.0|54301|\n",
      "| 1991.0|46335|\n",
      "| 1992.0|39451|\n",
      "| 1993.0|31976|\n",
      "| 1994.0|27102|\n",
      "| 1995.0|23899|\n",
      "| 1996.0|20613|\n",
      "| 1997.0|18865|\n",
      "| 1998.0|19117|\n",
      "| 1999.0|20326|\n",
      "| 2000.0|21153|\n",
      "| 2001.0|19401|\n",
      "| 2002.0|17435|\n",
      "| 2003.0|16490|\n",
      "| 2004.0|16840|\n",
      "+-------+-----+\n",
      "only showing top 100 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df_spark.groupby(\"biryear\").count().orderBy(col(\"biryear\")).show(100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-------+------+\n",
      "|airline| count|\n",
      "+-------+------+\n",
      "|     AA|310091|\n",
      "|     UA|264271|\n",
      "|     DL|252526|\n",
      "|     BA|190997|\n",
      "|     LH|120556|\n",
      "|     VS|113384|\n",
      "|   null| 83627|\n",
      "|     AF| 81113|\n",
      "|     KE| 71047|\n",
      "|     JL| 69075|\n",
      "+-------+------+\n",
      "only showing top 10 rows\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "535"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_airline=df_spark.groupby(\"airline\").count().orderBy(col(\"count\"),ascending=False)\n",
    "df_airline.show(10)\n",
    "df_airline.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": [
    "# clean\n",
    "\n",
    "# converse data tyep\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "editable": true
   },
   "source": [
    "### Step 3: Define the Data Model\n",
    "#### 3.1 Conceptual Data Model\n",
    "Map out the conceptual data model and explain why you chose that model\n",
    "\n",
    "#### 3.2 Mapping Out Data Pipelines\n",
    "List the steps necessary to pipeline the data into the chosen data model"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "editable": true
   },
   "source": [
    "### Step 4: Run Pipelines to Model the Data \n",
    "#### 4.1 Create the data model\n",
    "Build the data pipelines to create the data model."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": [
    "# Write code here"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "editable": true
   },
   "source": [
    "#### 4.2 Data Quality Checks\n",
    "Explain the data quality checks you'll perform to ensure the pipeline ran as expected. These could include:\n",
    " * Integrity constraints on the relational database (e.g., unique key, data type, etc.)\n",
    " * Unit tests for the scripts to ensure they are doing the right thing\n",
    " * Source/Count checks to ensure completeness\n",
    " \n",
    "Run Quality Checks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": [
    "# Perform quality checks here"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "editable": true
   },
   "source": [
    "#### 4.3 Data dictionary \n",
    "Create a data dictionary for your data model. For each field, provide a brief description of what the data is and where it came from. You can include the data dictionary in the notebook or in a separate file."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "editable": true
   },
   "source": [
    "#### Step 5: Complete Project Write Up\n",
    "* Clearly state the rationale for the choice of tools and technologies for the project.\n",
    "* Propose how often the data should be updated and why.\n",
    "* Write a description of how you would approach the problem differently under the following scenarios:\n",
    " * The data was increased by 100x.\n",
    " * The data populates a dashboard that must be updated on a daily basis by 7am every day.\n",
    " * The database needed to be accessed by 100+ people."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "editable": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
