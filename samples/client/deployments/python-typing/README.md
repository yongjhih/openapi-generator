# Documentation for Deployments

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://docker.mender.io/api/management/v1/deployments*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**artifacts_get**](Apis/DefaultApi.md#artifacts_get) | **GET** /artifacts | List known artifacts
*DefaultApi* | [**artifacts_id_delete**](Apis/DefaultApi.md#artifacts_id_delete) | **DELETE** /artifacts/{id} | Delete the artifact
*DefaultApi* | [**artifacts_id_download_get**](Apis/DefaultApi.md#artifacts_id_download_get) | **GET** /artifacts/{id}/download | Get the download link of a selected artifact
*DefaultApi* | [**artifacts_id_get**](Apis/DefaultApi.md#artifacts_id_get) | **GET** /artifacts/{id} | Get the details of a selected artifact
*DefaultApi* | [**artifacts_id_put**](Apis/DefaultApi.md#artifacts_id_put) | **PUT** /artifacts/{id} | Update description of a selected artifact
*DefaultApi* | [**artifacts_post**](Apis/DefaultApi.md#artifacts_post) | **POST** /artifacts | Upload mender artifact
*DefaultApi* | [**deployments_deployment_id_devices_device_id_log_get**](Apis/DefaultApi.md#deployments_deployment_id_devices_device_id_log_get) | **GET** /deployments/{deployment_id}/devices/{device_id}/log | Get the log of a selected device's deployment
*DefaultApi* | [**deployments_deployment_id_devices_get**](Apis/DefaultApi.md#deployments_deployment_id_devices_get) | **GET** /deployments/{deployment_id}/devices | List devices of a deployment
*DefaultApi* | [**deployments_deployment_id_statistics_get**](Apis/DefaultApi.md#deployments_deployment_id_statistics_get) | **GET** /deployments/{deployment_id}/statistics | Get the statistics of a selected deployment
*DefaultApi* | [**deployments_deployment_id_status_put**](Apis/DefaultApi.md#deployments_deployment_id_status_put) | **PUT** /deployments/{deployment_id}/status | Abort the deployment
*DefaultApi* | [**deployments_devices_id_delete**](Apis/DefaultApi.md#deployments_devices_id_delete) | **DELETE** /deployments/devices/{id} | Remove device from all deployments
*DefaultApi* | [**deployments_get**](Apis/DefaultApi.md#deployments_get) | **GET** /deployments | Find all deployments
*DefaultApi* | [**deployments_id_get**](Apis/DefaultApi.md#deployments_id_get) | **GET** /deployments/{id} | Get the details of a selected deployment
*DefaultApi* | [**deployments_post**](Apis/DefaultApi.md#deployments_post) | **POST** /deployments | Create a deployment
*DefaultApi* | [**deployments_releases_get**](Apis/DefaultApi.md#deployments_releases_get) | **GET** /deployments/releases | List releases
*DefaultApi* | [**limits_storage_get**](Apis/DefaultApi.md#limits_storage_get) | **GET** /limits/storage | Get storage limit and current storage usage


<a name="documentation-for-models"></a>
## Documentation for Models

 - [models.Artifact](Models/Artifact.md)
 - [models.ArtifactInfo](Models/ArtifactInfo.md)
 - [models.ArtifactLink](Models/ArtifactLink.md)
 - [models.ArtifactTypeInfo](Models/ArtifactTypeInfo.md)
 - [models.ArtifactUpdate](Models/ArtifactUpdate.md)
 - [models.Deployment](Models/Deployment.md)
 - [models.DeploymentStatistics](Models/DeploymentStatistics.md)
 - [models.Device](Models/Device.md)
 - [models.Error](Models/Error.md)
 - [models.InlineObject](Models/InlineObject.md)
 - [models.NewDeployment](Models/NewDeployment.md)
 - [models.Release](Models/Release.md)
 - [models.StorageLimit](Models/StorageLimit.md)
 - [models.Update](Models/Update.md)
 - [models.UpdateFile](Models/UpdateFile.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.
