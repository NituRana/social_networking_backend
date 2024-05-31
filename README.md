**Project: Social Networking Django Backend Project**

**Overview:**
This project aims to develop a Django backend for a social networking application, providing a RESTful API to manage user authentication, friend requests, and user search functionalities.

**Features:**

1. **User Authentication:**

    i. Users can sign up with their email addresses and passwords.\
    ii. Login functionality is provided using email and password authentication, with tokens generated upon successful authentication.\
    iii. API endpoints are protected with token-based authentication to ensure secure access.

3. **Friendship Management:**

    i. Users can send, accept, and reject friend requests.\
    ii. Users can list their friends and pending friend requests.\
    iii. Rate limiting is implemented to prevent abuse, such as sending too many friend requests within a short period.

**User Search:**

  i. Users can search for other users by email and full_name.\
  ii. The search API returns a paginated list of matching users, with options to search by email or partial name matches.

**Components:**

**Models:**

  1. User: Represents a user of the social networking platform.
  2. FriendRequest: Represents a friend request sent from one user to another.

**Serializers:**

  1. UserSerializer: Serializes user data for API interactions.
  2. FriendRequestSerializer: Serializes friend request data for API interactions.
   
**Views:**

1. **SignupView:** Handles user registration and signup process.
2. **LoginView:** Manages user login, authentication, and token generation.
3. **FriendRequestViewSet:** Manages friend request functionalities including sending, accepting, and rejecting requests.
4. **FriendListView:** Lists friends of a user based on accepted friend requests.
5. **PendingFriendRequestsView:** Lists pending friend requests received by a user, allowing them to accept or reject.
6. **UserSearchView:** Handles user search functionalities based on email or full name.

**Pagination:**

**UserSearchPagination:** Custom pagination class for paginating user search results.
  
  **Tools and Technologies:**
  
  **Django**: Python-based web framework for building web applications.\
  **Django REST Framework (DRF)**: Extends Django to simplify building RESTful APIs.\
  **PostgreSQL**: Database management system used to store user and friend request data.\
  **Docker**: Containerization platform used to package the application for deployment.

Deployment:
The application can be deployed using Docker containers for easy deployment and scalability.

Conclusion:
This project provides a robust backend solution for a social networking application, offering essential functionalities such as user authentication, friend management, and user search. With its RESTful API, developers can build rich front-end applications while ensuring data security and scalability.



** Project Installation**\
Follow these steps to set up and run the project locally:\
**1. Clone the Repository**

    git clone <repository-url>
    cd socialnetworking
**2. Create and Activate Virtual Environment (Optional but Recommended)**

    python -m venv venv
    source venv/bin/activate
  
**3. Install Dependencies**

    pip install -r requirements.txt

**4. Access PostgreSQL Shell**

    psql -U postgres

**5. Create Database in Your local machine**
  a. Install PostgreSQL:
    
    sudo apt-get install postgresql
    
  b. Create Database:
  
    CREATE DATABASE your_database_name;
    #example
    CREATE DATABASE socialnetworking_db;

  c. Create a User:
  
    CREATE USER your_username WITH PASSWORD 'your_password';
    #example
    CREATE USER CRUD_USER WITH PASSWORD 'accuknoxtestbd';
    
  d. Grant Privileges:

    GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_username;
    #example
    GRANT ALL PRIVILEGES ON DATABASE socialnetworking_db TO CRUD_USER;
      
**6. Update Django Settings and Configure Database**\
a. Set Up Database Settings\
In the settings.py file, configure the database settings according to your requirements. You can find the database settings in the DATABASES dictionary. Here's an example configuration for a PostgreSQL database:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
Replace your_database_name, your_database_user, and your_database_password with your actual database name, user, and password.

b. Migrate Database\
Once you have configured the database settings, run migrations to create database tables:

    python manage.py migrate
    
**7. Create Superuser (Optional)**
If you need an admin user, create one using the following command:\
    
    python manage.py createsuperuser
    
**8. Run the Development Server**

Start the Django development server:

    python manage.py runserver
The server should start running at **http://127.0.0.1:8000/**.


