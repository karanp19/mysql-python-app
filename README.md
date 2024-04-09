# User Authentication App

This Django application provides user authentication functionality including sign up, login, and a success page. Users can sign up with a unique username, password, and email address, and then log in using their credentials.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd user_auth
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

5. Access the application at [http://localhost:8000/](http://localhost:8000/)

## Usage

- Sign Up: Navigate to [http://localhost:8000/signup/](http://localhost:8000/signup/) to create a new account. Provide a unique username, password, and email address.
- Login: After signing up, navigate to [http://localhost:8000/login/](http://localhost:8000/login/) to log in with your credentials.
- Success: Upon successful login, you'll be redirected to [http://localhost:8000/success/](http://localhost:8000/success/).

## Project Structure

- `user_auth/`: Django project directory.
    - `accounts/`: Django app for user authentication.
        - `models.py`: Defines the User model.
        - `views.py`: Contains view functions for sign up, login, and success pages.
        - `forms.py`: Defines forms for sign up and login.
        - `urls.py`: URL patterns for the accounts app.
        - `templates/`: HTML templates for rendering pages.
    - `user_auth/`: Django project settings.
    - `manage.py`: Django management script.

## Dependencies

- Django: [https://www.djangoproject.com/](https://www.djangoproject.com/)
- MySQL database: [https://www.mysql.com/](https://www.mysql.com/)

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
