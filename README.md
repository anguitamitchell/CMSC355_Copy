![](images/drugs.jpg)

# Welcome to PharmaSense AI!

- [Welcome to PharmaSense AI!](#welcome-to-pharmasense-ai)
  - [Overview](#overview)
  - [Presentation Slides](#presentation-slides)
  - [Set-up Instructions](#set-up-instructions)
  - [Group Members](#group-members)


## Overview

"Admissions due to DRPs have been reported as growing over the past decades. In United States, estimates suggested that Drug-related problems (DRPs) accounted for 17 million emergency department visits and 8.7 million hospital admissions annually." -NIH

Pharmasense AI aims to use AI to detect potential drug interactions, alerting both the patient and healthcare providers about any potential complications with any combination of medications or supplements.

This is for the purpose of reducing risk of adverse drug events, enhancing patient safety, supporting accurate and informed prescribing, improving efficiency in clinical decision-making, and strengthening provider-patient communication.

## Presentation Slides

Here are our presentation slides: <https://docs.google.com/presentation/d/16ZitUTX_etUuWYf-bBnUbBZGRjUFJhW70R-tifPpJEw/edit?usp=sharing>

## Set-up Instructions

Ensure you have your own openrouter api key: <https://openrouter.ai/settings/keys>

Run from the terminal
- cd AssignmentRepoDemo (from YashSonar20's GitHub)
- install nodejs npm 
- cd AiMedTracker 
- cd backend 
- pip3 install -r requirements.txt
- ADD YOUR API KEY: touch .env, nano.env, "OPENROUTER_API_KEY=(YOUR API KEY)"
- cd ..
- cd frontend
- npm install
- npm run dev
- ctrl + click the link in the terminal


For windows OS users:

1. Navigate to the project directory:
Open the terminal in VSCode.
Run the following command to clone or navigate to the repository: cd AssignmentRepoDemo
2. Install Node.js and npm:
You can install Node.js and npm via the official Node.js website: https://nodejs.org/
Download and install the LTS version (Long Term Support). This will automatically install both Node.js and npm.
3. Navigate to the AiMedTracker/backend folder:
In the terminal, run: cd AiMedTracker cd backend
4. Install Python dependencies:
Ensure you have Python installed (check by running python --version in the terminal).
Run the following command to install the dependencies: pip install -r requirements.txt
5. Set up your API key:
Create a .env file by running: type nul > .env
Open the .env file in a text editor (you can use VSCode or Notepad) and add your API key like so: OPENROUTER_API_KEY=(YOUR API KEY)
6. Navigate to the frontend folder:
Run the following command to go to the frontend directory: cd .. cd frontend
7. Install the frontend dependencies using npm:
Run the following commands to install the necessary npm packages: npm install
8. Run the frontend app:
Once the dependencies are installed, run the development server: npm run dev
9. Access the application:
The terminal will provide a link to open the app in your browser. You can either click the link directly in the terminal or copy and paste it into your browser to access the running app.



## Group Members

- Thomas Yang
- Yash Sonar
- Ayush Purankar
- Leiliani Clark
- Trinitey Tran
