# Back-End MakeUpMate

This repository contains the source code for the MakeUpMate Back-end application.

## List API 
(Full Documentation you can read at https://makeupmate-5ss3p3jbsq-as.a.run.app/api-doc)
- Login
- Predict

## How to run in your local

- Clone this github
- Create virtual enviroment & active it (optional)
- Install dependencies "pip install -r requirements.txt"
- Request access for config.json and serviceAccounts.json in this link (https://drive.google.com/drive/folders/1dW84JJL-ME2_k9zLYH45v6rkqYrhYUpL?usp=sharing)
- Put the two files into the BE_MakeUpMate folder
- Create file .env and add "PORT=8080" (you can change your port)
- run "python app.py" 
- You can check in http://localhost:8080 (match your ports to those in the .env file)

## Deployment Link
https://makeupmate-5ss3p3jbsq-as.a.run.app

## Note
Please don't share config.json and serviceAccounts.json to public because there is a credentials token.
