# Documentation for User administration and authentication

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://docker.mender.io/api/management/v1/useradm*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**auth_login_post**](Apis/DefaultApi.md#auth_login_post) | **POST** /auth/login | Log in to Mender
*DefaultApi* | [**settings_get**](Apis/DefaultApi.md#settings_get) | **GET** /settings | Get user settings
*DefaultApi* | [**settings_post**](Apis/DefaultApi.md#settings_post) | **POST** /settings | Set user settings
*DefaultApi* | [**users_get**](Apis/DefaultApi.md#users_get) | **GET** /users | List users
*DefaultApi* | [**users_id_delete**](Apis/DefaultApi.md#users_id_delete) | **DELETE** /users/{id} | Remove user from the system
*DefaultApi* | [**users_id_get**](Apis/DefaultApi.md#users_id_get) | **GET** /users/{id} | Get user information
*DefaultApi* | [**users_id_put**](Apis/DefaultApi.md#users_id_put) | **PUT** /users/{id} | Update user information
*DefaultApi* | [**users_post**](Apis/DefaultApi.md#users_post) | **POST** /users | Create user


<a name="documentation-for-models"></a>
## Documentation for Models

 - [models.Error](Models/Error.md)
 - [models.User](Models/User.md)
 - [models.UserNew](Models/UserNew.md)
 - [models.UserUpdate](Models/UserUpdate.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.
