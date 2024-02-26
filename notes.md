# 2024-02-25
Checking for categorical features
    1. Pos
    2. Player-additional
How to handle cat features?
    Pos
        OHE - low dimensionality. positions should have some relationship
        Target encoding - positions should have some relationship with target
    Player-additional: will be dropped before training
OHE Pos
    Just realized the positions are not just PG,G,SF,PF,C. There are combos.
    Knowing this, I will drop pos because I don't have a good way to decide what positions
    Maybe in the future, we will group them using a clustering method

Fitted the model with just all the columns
Result
    - RMSE: 5.75 i.e. predictions were off by 5.75 on average

Highest priority variables
* Age
* Number of years in league
* Number of years on current team

# Default Points Categories
Official NBA
Points: 1
Rebounds: 1.2
Assists: 1.5
Steals: 3
Blocks: 3
Turnovers: -1

Point weights can differ between fantasy leagues.
New categories can be added e.g. 3FGM

# Design
Regression problem
Target: Fantasy Points

Data Set
    - each row is an arbitrary player's previous season metrics + feature engineering, with a target col of their fantasy points (calculated from their end of season stat totals)
    - feature: number of games missed. drop rows after a certain threshold. We cannot predict missed games, so we do not want our inference to account for that
    - is number 1 option
    - is duo option
    - is big 3 option   
    - age
    - is hungry/motivated
        - contract year, fiba/olympic year, just on fiba/olympic, deep playoff run
    - won championship before
        - championship teams tend to coast/relax
        - too little of rows will have it, not good for ml
    - number of all star teammates
    - number of all nba teammates
    - new coach
        - https://www.basketball-reference.com/leagues/NBA_2023_coaches.html

Data Pipeline
    - drop rows with "abnormal circumstances" e.g. injuries, personal leave, traded(?)
        - we want only rows where the player had the full opportunity to showcase their skill because that's what we can only assume with our picks

Time series problem?
"blind quarters" == "blind seasons", with last year being the validation season

# Features
<stat> per game
    - multiplied by pt factor
Row
    - target: next year fantasy points avg
    - previous year stats
    - age
    - number of years on team
    - is new team
    - number of years in nba
    - number of years college/international
    - has new head coach
    - has new defense coordinator
    - has new offensive coordinator
    - current team's offensive rating last year
    - current team's defensive rating last
    - was injured for extended amount of time last year
    - started last year
    - expected to start
        - maybe a way to classify this is if the starters from previous years have stayed?
    - was 1st option
    - was 2nd option
    - was 3rd option
    - will be 1st option
    - will be 2nd option
    - will be 3rd option
    - there is new starter on team
    - made all nba
    - made all nba defense
    - if new team, previous team offense and defense rating

Separate Model for Rookies