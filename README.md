# CI/CD Automated Exam Paper Generation

This project implements a CI/CD workflow to automatically generate exam papers using a Python script and MySQL database.

## Overview

The provided Python script connects to a MySQL database, retrieves random questions, and creates an HTML exam paper with shuffled options. The generated papers are then archived into a zip file and stored as artifacts.

## Prerequisites

- Python 3.x
- MySQL server
- [Add any additional prerequisites]

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/YourUsername/YourRepository.git
   cd YourRepository
   
2. Install dependencies:

       pip install -r requirements.txt

# CI/CD Workflow

# The CI/CD workflow is triggered on each push to the main branch. It performs the following steps:

    Checks out the code.
    Sets up Python and starts the MySQL service.
    Installs project dependencies.
    Generates exam papers using the provided Python script.
    Archives the generated exam papers into a zip file.
    Uploads the zip file as artifacts.




 IMPORTANT CHANGES TO MAKE  

    Make sure to replace placeholders like `YourUsername`, `YourRepository`, and update the sections as needed to fit your project's details and requirements. If you have additional files like `CONTRIBUTING.md` or `LICENSE`, make sure to include them in your repository and link them appropriately in the README.
  
       

