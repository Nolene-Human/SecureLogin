
# Secure Login
This exercise is to create various login pages using Flask. Each .py file will have a corresponding .html template to make it easy.
Each project will add a security layer to the login function.

## Simple Login

This is a basic login page implementation using Flask. The purpose of this project is to demonstrate a simple login functionality without any additional security measures.

## Session Login

This file contains the implementation of the session login functionality.

The session_login module provides functions for handling user login sessions. It includes functions for validating user credentials, creating session tokens, and managing session expiration.

## Cross-Site Request Forgery Prevention login

To prevent CSRF attacks when user authentication is when logging into a web application where their session is authenticated using cookies the following file will be implemented:

a) CSRF Tokens: Include a unique token the server validates in each form submission.

### Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.x
- Flask
- Flask-WTF

### Getting Started

1. Clone this repository to your local machine.
2. Navigate to the project directory: `/workspaces/SecureLogin`.
3. Install the required dependencies by running the following command:
    ```
    pip install -r requirements.txt
    ```
4. Start the Flask development server:
    ```
    flask run
    ```
5. Open your web browser and visit `http://localhost:5000` to access the login page.

### Usage

- Enter your username and password in the provided fields.
- Click the "Login" button to submit the form.
- If the credentials are valid, you will be redirected to the home page.
- If the credentials are invalid, an error message will be displayed.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
