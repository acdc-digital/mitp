# M.I.T.P.
Medical Information Training and Personalization

This project provides a Flask application that allows users to upload their medical information and chat with the Medex assistant to better understand their data. The application also implements a privacy filter to protect sensitive information.


## Project Structure

```
MITP
│   app.py
│   create_app.py
│   database.py
│   main.py
│   medex_exec_assistant.py
│   README.md
│
├───Instance
│       medex.db
│
├───medex_project
│   ├───data
│   │       medical_corpus.py
│   │       privacy_data.py
│   │       user_data_corpus.py
│   │
│   ├───model_parameters
│   │       medex_evaluation.py
│   │       medex_hyperparameters.py
│   │       medex_language_model.py
│   │       medex_training.py
│   │
│   ├───preprocessing
│   │       clean_data.py
│   │       split_data.py
│   │       tokenize_data.py
│   │
│   └───utils
│           interpretation.py
│           privacy_filter.py
│           save_load_model.py
│
└───templates
    ├───index
    ├───login
    └───protected
```

## Installation and Local Deployment

1. Make sure Python 3.7+ is installed on your system.
2. Install the required packages:

```
pip install flask
pip install flask_sqlalchemy
pip install flask_bcrypt
pip install flask_login
pip install flask_sslify
pip install transformers
pip install torch
pip install scikit-learn
pip install nltk
pip install flask-sqlalchemy 
pip install psycopg2-binary
pip install pandas
```

3. Clone the project repository and navigate to the project folder:

```
cd /Users/matthewsimon/Documents/mitp/Medical_Information_Training_Personalization 
```

4. Set up the database:

```
python database.py
```

5. Run the main.py file to train and evaluate the model, apply the privacy filter, and interpret medical data:

```
python main.py
```

6. Run the app.py file to start the Flask application:

```
python app.py
```

7. Open a web browser and navigate to http://127.0.0.1:5000/ to access the Medex application.

## Usage

Once the application is running, users can upload their medical information and chat with the Medex assistant to understand their data better. Users can also choose which information to share with others, allowing them to chat against their data or comments without direct communication.

The Medex assistant uses a trained language model to interpret medical terms and abbreviations, providing users with a better understanding of their medical data. The application also implements a privacy filter to protect sensitive information.

## Debugging and Improvements

As a junior developer, you should focus on understanding the code structure, functionality, and dependencies. To debug and improve the application, follow these steps:

1. Familiarize yourself with the Flask framework, SQLAlchemy, and the Transformers library.
2. Review the code in each file, understanding the purpose of each function and class.
3. Identify any potential issues or areas for improvement in the code, such as performance bottlenecks, security vulnerabilities, or code readability.
4. Make the necessary changes to the code, ensuring that you maintain the existing functionality and adhere to best practices.
5. Test your changes thoroughly, ensuring that the application still functions correctly and that any improvements have the desired effect.
6. Document your changes and any issues you encountered during the debugging process.
7. Submit your updated code and documentation to the project lead for review and integration into the main project.

By following these steps, you will contribute to the overall quality and functionality of the Medex application, helping to create a valuable tool for users to better understand and manage their medical data.