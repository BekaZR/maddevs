# MADDEVS

# Start project:
  1) Start docker machine on your PC
  2) Change main project directory in terminal
  3) Create .env file early core directory by .env.example 
  4) Enter command "sudo docker-compose up --build" in your terminal
  5) Go to localhost in your browser (without port 8000, nginx was connected)
  6) Project was successful started

# API
  1) Go to **http://localhost/api/registration/** in Postman and set to body this
     - {
        "username": "Your username",
        "password": "Your password",
        "is_doctor": true/false
      }
     - Select POST method
     
  2) Go to **http://localhost/api/token/** in Postman and set to body this
     - {
        "username": "Your username",
        "password": "Your password"
      }
     - Select POST method
     
  3) Go to **http://localhost/api/diagnoses/** in Postman and set to body this
     - {
        "name_diagnos": "Diagnos name"
      }
     - Select POST method
     
  4) Go to **http://localhost/api/pacients/** in Postman and set to body this
     - In field diagnoses set array with id diagnoses
     - Copy access token from 2 paragraph and set him to headers for this router
     - If user is not doctor you get error message about this
     - If user is doctor you can create new pacient
     - {
        "date_of_birth": "2017-01-01",
        "diagnoses": [1, 3]
     }
     - Select POST method
     
  5) Go to **http://localhost/api/pacients/** in Postman and set to body this
     - Copy access token from 2 paragraph and set him to headers for this router
     - If user is not doctor you get error message about this
     - If user is doctor you get list from 3 pacients
     - Select GET method 
