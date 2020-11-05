Hello

This repository contains a django project which marks attendance using facial recognition using opencv for python.

Working:
- The project contains an app named registration, all the work done is in this app.
- There are 4 modules viz. Product_Key, Admin_Detail(an organisation), Employee Registration, Employee login.
- Every organisation should have a product key to register and admin gets to register all their employees with their details along with their image.
- Employees can log in using their employee id under employee login.
- Once they enter their employee id and press enter, camera starts and takes a photo of employee.
- After that the model trains itself with the training data which was given to it while registration.
- Finally it detects the face, creates an excel sheet and records entry along with date time.
- Admin of organisation can log in and download the excel to see who all marked their attendance for the day and at what time.

The project is live on:
https://damp-beyond-74784.herokuapp.com/
