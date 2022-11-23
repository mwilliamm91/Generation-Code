Owner: William

This app is to be used in a pop up cafe to manage all aspects related to the business data i.e. products, couriers, orders etc.

Client Requirements:

Client requested an app that logs and keeps track of the orders.
The app should contain a collection of products and couriers
All data handled in the app should persisted on exit and loaded when app is started
The app should create, update and delete orders to a csv file as well as a database
The app should be tested prior to handing over as well receive regular software updates

I followed a pseudo code which made sure I didn't stray away from the client specification. I managed to meet most of the client specification although some features are have not been completed. 

Given more time, I would carry out some test driven development to make sure all featured work as intended and I would also create a database to save the data in addition to the csv files. Make use of oop in my code.

I enjoyed implementing new complex features and refactoring the code depending on the features.




file tree

|-Data-- -couriers.csv
|        -orders.csv
|        -products.csv
|-src--  |-db-- -database.py
         |-file_handler-- -couriers.py
         |                -orders.py
         |                -products.py
         |-main.py
         |-utils.py