USE WAREHOUSE NYC_TAXI_WH;
USE DATABASE NYC_TAXI_DB;
USE SCHEMA ANALYTICS;

-- =====================================================
-- DIM_DATE
-- =====================================================

CREATE OR REPLACE TABLE DIM_DATE (

    DATE_KEY INTEGER PRIMARY KEY,

    FULL_DATE DATE,

    YEAR INTEGER,

    QUARTER INTEGER,

    MONTH INTEGER,

    MONTH_NAME STRING,

    WEEK INTEGER,

    DAY INTEGER,

    DAY_NAME STRING,

    DAY_OF_WEEK INTEGER,

    IS_WEEKEND BOOLEAN

);

-- =====================================================
-- DIM_VENDOR
-- =====================================================

CREATE OR REPLACE TABLE DIM_VENDOR (

    VENDOR_KEY INTEGER PRIMARY KEY,

    VENDOR_NAME STRING

);

-- =====================================================
-- DIM_PAYMENT
-- =====================================================

CREATE OR REPLACE TABLE DIM_PAYMENT (

    PAYMENT_KEY INTEGER PRIMARY KEY,

    PAYMENT_NAME STRING

);

-- =====================================================
-- DIM_LOCATION
-- =====================================================

CREATE OR REPLACE TABLE DIM_LOCATION (

    LOCATION_KEY INTEGER PRIMARY KEY,

    BOROUGH STRING,

    ZONE STRING,

    SERVICE_ZONE STRING

);

-- =====================================================
-- FACT_DAILY
-- =====================================================

CREATE OR REPLACE TABLE FACT_DAILY (

    DATE_KEY INTEGER,

    TRIP_COUNT INTEGER,

    TOTAL_PASSENGERS INTEGER,

    TOTAL_DISTANCE FLOAT,

    AVG_DISTANCE FLOAT,

    TOTAL_FARE FLOAT,

    AVG_FARE FLOAT,

    TOTAL_TIP FLOAT,

    AVG_TIP FLOAT,

    TOTAL_REVENUE FLOAT,

    AVG_REVENUE FLOAT,

    AVG_TRIP_DURATION FLOAT

);

-- =====================================================
-- FACT_TRIP
-- =====================================================

CREATE OR REPLACE TABLE FACT_TRIP (

    DATE_KEY INTEGER,

    VENDOR_KEY INTEGER,

    PAYMENT_KEY INTEGER,

    PICKUP_LOCATION_KEY INTEGER,

    DROPOFF_LOCATION_KEY INTEGER,

    PASSENGER_COUNT INTEGER,

    TRIP_DISTANCE FLOAT,

    TRIP_DURATION_MINUTES FLOAT,

    FARE_AMOUNT FLOAT,

    TIP_AMOUNT FLOAT,

    TOTAL_AMOUNT FLOAT

);