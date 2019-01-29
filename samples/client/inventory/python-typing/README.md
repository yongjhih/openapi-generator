# Documentation for Device inventory

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://docker.mender.io/api/management/v1/inventory*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**devices_get**](Apis/DefaultApi.md#devices_get) | **GET** /devices | List devices
*DefaultApi* | [**devices_id_delete**](Apis/DefaultApi.md#devices_id_delete) | **DELETE** /devices/{id} | Remove selected device
*DefaultApi* | [**devices_id_get**](Apis/DefaultApi.md#devices_id_get) | **GET** /devices/{id} | Get a selected device
*DefaultApi* | [**devices_id_group_get**](Apis/DefaultApi.md#devices_id_group_get) | **GET** /devices/{id}/group | Get a selected device's group
*DefaultApi* | [**devices_id_group_name_delete**](Apis/DefaultApi.md#devices_id_group_name_delete) | **DELETE** /devices/{id}/group/{name} | Remove a device from a group
*DefaultApi* | [**devices_id_group_put**](Apis/DefaultApi.md#devices_id_group_put) | **PUT** /devices/{id}/group | Add a device to a group
*DefaultApi* | [**groups_get**](Apis/DefaultApi.md#groups_get) | **GET** /groups | List groups
*DefaultApi* | [**groups_name_devices_get**](Apis/DefaultApi.md#groups_name_devices_get) | **GET** /groups/{name}/devices | List the devices belonging to a given group


<a name="documentation-for-models"></a>
## Documentation for Models

 - [models.Attribute](Models/Attribute.md)
 - [models.Device](Models/Device.md)
 - [models.Error](Models/Error.md)
 - [models.Group](Models/Group.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.
