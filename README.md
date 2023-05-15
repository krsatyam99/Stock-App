
# Stock Tracker App

This Django project provides a stock tracker application that displays the real-time stock price for a selected stock. The project utilizes various technologies such as Celery, Redis, Channels, multithreading, Yahoo Finance library, and web scraping.  
[Quick Demo ](www.wikepedia.com)


## Prerequisites

 - Python 3.x
 - Django
 - Celery
- Redis
 - Channels
 - yfinance 0.2.18




## Set Up
 - Clone the repository:  
 - git@github.com:krsatyam99/Stock-App.git

- Navigate to the project directory  
    cd stockapp


- Install the required dependencies:  
    pip install -r requirements.txt

- Start the Redis server:  
    redis-server -> This will start the Redis server on the default port 6379. 
  ### Redis configuration  verification 
     Verify Redis server is running: You can check if the Redis server is running by running the redis-cli ping command. If the server is running, it will respond with PONG.
-  Start the Celery worker:  
    celery -A stockapp.celery worker --pool=solo -l info
- Start the ASGI server:  
     daphne -p 8000 -b 0.0.0.0 stockapp.asgi:application
 

## Usage   
- Access the web application by opening your browser and entering the following URL: 
    http://localhost:8000/  
- On the picker page, select a stock whatever you want and click on submit.  
- The application will display the real-time stock price on the tracker page.

    

## Celery and Redis Configuration  
The CELERY_BROKER_URL setting in settings.py specifies the Redis URL for the Celery broker. By default, it uses redis://localhost:6379/0.   
![celry stockapp](https://github.com/krsatyam99/Stock-App/assets/103446420/39dc2d27-a788-438d-b216-a847d7d02279)   

## Channels with Celery and Django Admin  

![websocket stockapp](https://github.com/krsatyam99/Stock-App/assets/103446420/78706348-556e-4be3-8d55-39b81aa6cafc)
## channels configuration  

![channels](https://github.com/krsatyam99/Stock-App/assets/103446420/1360905b-9691-4608-84ec-74a81bfc6e72)


## Additional  Information  
- The tasks.py file in the tracker app contains the Celery task that fetches the stock price using the Yahoo Finance library and web scraping techniques.  
 - The stock price is updated automatically on the tracker page using Channels, which provides real-time communication between the server and the client.    
- Multithreading can be used in the Celery task or other parts of the project to handle concurrent requests efficiently.    
Please note that this README provides an overview of the project and its components. For detailed implementation and code, refer to the source code files in the project repository.
