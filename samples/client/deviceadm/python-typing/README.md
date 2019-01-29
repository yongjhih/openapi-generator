# Documentation for Device admission

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://docker.mender.io/api/management/v1/admission*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**devices_get**](Apis/DefaultApi.md#devices_get) | **GET** /devices | List known device data sets
*DefaultApi* | [**devices_id_delete**](Apis/DefaultApi.md#devices_id_delete) | **DELETE** /devices/{id} | Remove device authentication data set
*DefaultApi* | [**devices_id_get**](Apis/DefaultApi.md#devices_id_get) | **GET** /devices/{id} | Get the details of a selected device authentication data set
*DefaultApi* | [**devices_id_put**](Apis/DefaultApi.md#devices_id_put) | **PUT** /devices/{id} | Submit a device authentication data set for admission
*DefaultApi* | [**devices_id_status_get**](Apis/DefaultApi.md#devices_id_status_get) | **GET** /devices/{id}/status | Check the admission status of a selected device authentication data set
*DefaultApi* | [**devices_id_status_put**](Apis/DefaultApi.md#devices_id_status_put) | **PUT** /devices/{id}/status | Update the admission status of a selected device
*DefaultApi* | [**devices_post**](Apis/DefaultApi.md#devices_post) | **POST** /devices | Submit a preauthorized device authentication data set


<a name="documentation-for-models"></a>
## Documentation for Models

 - [models.Attributes](Models/Attributes.md)
 - [models.AuthSet](Models/AuthSet.md)
 - [models.Device](Models/Device.md)
 - [models.Error](Models/Error.md)
 - [models.NewDevice](Models/NewDevice.md)
 - [models.Status](Models/Status.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.
