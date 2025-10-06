IoT Basics  

CONTENTS:  

  IoT pipeline:  

  Tehtävät 1:  
    Ask name: Just a test; asks a name from user and responds depending on the name.  
    Blink the led: Blinks the onboar led on and off.  
    Blink the external led: Blinks the led connected to the board.  
    Burglary alarm: Detects motion with PIR-sensor, alerts when motion is detected.  
    Interrupt: Measures reaction time, led goes off randomly and user presses the button attached to the board. LCD-screen shows reaction time.  
    Lcd-screen: Prints "Hello student!" on LCD-screen that's connected to the board.  
    Led on by pressing button: The led goes on by pressing the button connected to the board.  
    Optimized blink: Optimized on board led blink.  
    Test: Just a test; prints number from 1 to 10.  
    Trafficlights: Basic trafficlights with a button to interrupt the normal flow of the lights. When pressing the button down, the red one stays on and the buzzer connected to the board makes a sound.  
    Weather: First basic version of weather station; DHT-22 connected to the board. Informs user about current temperature and humidity.   
    Weather backend: Next version of the weather station. DHT-22 connected to the board. Connects to the wi-fi and send temperature and humidity data to Thingspeak channels.  
    
  Tehtävät 2:  
    Server: A minimal Express-based API server that simulates sensor data. It runs on port 3000 and provides a single endpoint.  
    
  Tehtävät 3:  
    Server: A simple Node.js REST API built using Express and SQLite3. It serves as a minimal backend service for managing users and retrieving sensor data.  
    
  Tehtävät 4:  
    Fetch: fetches real-time temperature and humidity data from a public ThingSpeak channel using the Fetch API. It processes the data and displays it in the browser.  
    Webhook  
    Websocket  
