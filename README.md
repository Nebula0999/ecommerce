# ecommerce
Capstone project for backend development
# Cloned a repository to vscode
## Initialized a new django project called ecommerce using django-admin startproject ecommerce
# Created an initial app products

# Users app
It manages users and user permissions
1. Adding users 
    Users will be added by admin
2. Defining user permissions
    Users can be placed into different groups that define the permissions for them
3. Changing user permissions
    User permissions can be changed by simply changing their groups
4. Deleting users
    Only admins can delete users
I used ReadOnlyModelViewset for users to restrict creation of users by admins only

# Products app
Contains models that handle
1. Products addition, updating, and deleting
    1. Adding products
    User uses the POSt method to add products to the API.
    The user must be authenticated to perform this action.
    When succesfully created it should return status 201 created
    2. Updating products
    User can use the PUT method to update product details
    User must be authenticated to perform this
    When succesfully created it should return status 201 created
    3. Deleting products
    User can use the DELETE method to destroy a product
    Only authenticated users can perform this
2. Order creation, updating and deleting
    Only authenticated users can create, update or delete orders
    When succesfully created it should return status 201 created
3. Category addition and deletion
    Only authenticated users can add or delete categories 
    When succesfully created it should return status 201 created
4. Order item CRUD operations
    Only authenticated users can perform this operation
    When succesfully created it should return status 201 created
5. Product Reviews
    Only authenticated users can perform this operations
    When succesfully created it should return status 201 created

It also contains the views that define the viewsets for the models
For viewsets, i used model viewsets for products as it can handle all the GET, UPDATE, and DELETE methods instead of hanling these methods singularly.

# api app
Contains the links to the API views of products and users
1. Serializes the views
    I used model serializers to handle serialization of models
2. Contains the links to the various views of the api
    I used routers to map the paths to specific views and generate the api views

# Configuring the api
I added the apps to installed apps in the settings.py
I also added the rest-framework packages i used to settings.py

# securing the API
I set debug to false to restrict modifying the api from the browser.
I also implemented measures to protect against http injection and XSS attacks
