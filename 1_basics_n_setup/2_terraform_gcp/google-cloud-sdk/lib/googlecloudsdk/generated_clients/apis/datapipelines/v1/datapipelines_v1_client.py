"""Generated client library for datapipelines version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.datapipelines.v1 import datapipelines_v1_messages as messages


class DatapipelinesV1(base_api.BaseApiClient):
  """Generated client library for service datapipelines version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://datapipelines.googleapis.com/'
  MTLS_BASE_URL = 'https://datapipelines.mtls.googleapis.com/'

  _PACKAGE = 'datapipelines'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'DatapipelinesV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new datapipelines handle."""
    url = url or self.BASE_URL
    super(DatapipelinesV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_pipelines_jobs = self.ProjectsLocationsPipelinesJobsService(self)
    self.projects_locations_pipelines = self.ProjectsLocationsPipelinesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsPipelinesJobsService(base_api.BaseApiService):
    """Service class for the projects_locations_pipelines_jobs resource."""

    _NAME = 'projects_locations_pipelines_jobs'

    def __init__(self, client):
      super(DatapipelinesV1.ProjectsLocationsPipelinesJobsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists jobs for a given pipeline. Throws a "FORBIDDEN" error if the caller doesn't have permission to access it.

      Args:
        request: (DatapipelinesProjectsLocationsPipelinesJobsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatapipelinesV1ListJobsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/pipelines/{pipelinesId}/jobs',
        http_method='GET',
        method_id='datapipelines.projects.locations.pipelines.jobs.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+parent}/jobs',
        request_field='',
        request_type_name='DatapipelinesProjectsLocationsPipelinesJobsListRequest',
        response_type_name='GoogleCloudDatapipelinesV1ListJobsResponse',
        supports_download=False,
    )

  class ProjectsLocationsPipelinesService(base_api.BaseApiService):
    """Service class for the projects_locations_pipelines resource."""

    _NAME = 'projects_locations_pipelines'

    def __init__(self, client):
      super(DatapipelinesV1.ProjectsLocationsPipelinesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a pipeline. For a batch pipeline, you can pass scheduler information. Data Pipelines uses the scheduler information to create an internal scheduler that runs jobs periodically. If the internal scheduler is not configured, you can use RunPipeline to run jobs.

      Args:
        request: (DatapipelinesProjectsLocationsPipelinesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatapipelinesV1Pipeline) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/pipelines',
        http_method='POST',
        method_id='datapipelines.projects.locations.pipelines.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/pipelines',
        request_field='googleCloudDatapipelinesV1Pipeline',
        request_type_name='DatapipelinesProjectsLocationsPipelinesCreateRequest',
        response_type_name='GoogleCloudDatapipelinesV1Pipeline',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a pipeline. If a scheduler job is attached to the pipeline, it will be deleted.

      Args:
        request: (DatapipelinesProjectsLocationsPipelinesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/pipelines/{pipelinesId}',
        http_method='DELETE',
        method_id='datapipelines.projects.locations.pipelines.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DatapipelinesProjectsLocationsPipelinesDeleteRequest',
        response_type_name='GoogleProtobufEmpty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Looks up a single pipeline. Returns a "NOT_FOUND" error if no such pipeline exists. Returns a "FORBIDDEN" error if the caller doesn't have permission to access it.

      Args:
        request: (DatapipelinesProjectsLocationsPipelinesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatapipelinesV1Pipeline) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/pipelines/{pipelinesId}',
        http_method='GET',
        method_id='datapipelines.projects.locations.pipelines.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DatapipelinesProjectsLocationsPipelinesGetRequest',
        response_type_name='GoogleCloudDatapipelinesV1Pipeline',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists pipelines. Returns a "FORBIDDEN" error if the caller doesn't have permission to access it.

      Args:
        request: (DatapipelinesProjectsLocationsPipelinesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatapipelinesV1ListPipelinesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/pipelines',
        http_method='GET',
        method_id='datapipelines.projects.locations.pipelines.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/pipelines',
        request_field='',
        request_type_name='DatapipelinesProjectsLocationsPipelinesListRequest',
        response_type_name='GoogleCloudDatapipelinesV1ListPipelinesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a pipeline. If successful, the updated Pipeline is returned. Returns `NOT_FOUND` if the pipeline doesn't exist. If UpdatePipeline does not return successfully, you can retry the UpdatePipeline request until you receive a successful response.

      Args:
        request: (DatapipelinesProjectsLocationsPipelinesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatapipelinesV1Pipeline) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/pipelines/{pipelinesId}',
        http_method='PATCH',
        method_id='datapipelines.projects.locations.pipelines.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='googleCloudDatapipelinesV1Pipeline',
        request_type_name='DatapipelinesProjectsLocationsPipelinesPatchRequest',
        response_type_name='GoogleCloudDatapipelinesV1Pipeline',
        supports_download=False,
    )

    def Run(self, request, global_params=None):
      r"""Creates a job for the specified pipeline directly. You can use this method when the internal scheduler is not configured and you want to trigger the job directly or through an external system. Returns a "NOT_FOUND" error if the pipeline doesn't exist. Returns a "FORBIDDEN" error if the user doesn't have permission to access the pipeline or run jobs for the pipeline.

      Args:
        request: (DatapipelinesProjectsLocationsPipelinesRunRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatapipelinesV1RunPipelineResponse) The response message.
      """
      config = self.GetMethodConfig('Run')
      return self._RunMethod(
          config, request, global_params=global_params)

    Run.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/pipelines/{pipelinesId}:run',
        http_method='POST',
        method_id='datapipelines.projects.locations.pipelines.run',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:run',
        request_field='googleCloudDatapipelinesV1RunPipelineRequest',
        request_type_name='DatapipelinesProjectsLocationsPipelinesRunRequest',
        response_type_name='GoogleCloudDatapipelinesV1RunPipelineResponse',
        supports_download=False,
    )

    def Stop(self, request, global_params=None):
      r"""Freezes pipeline execution permanently. If there's a corresponding scheduler entry, it's deleted, and the pipeline state is changed to "ARCHIVED". However, pipeline metadata is retained.

      Args:
        request: (DatapipelinesProjectsLocationsPipelinesStopRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatapipelinesV1Pipeline) The response message.
      """
      config = self.GetMethodConfig('Stop')
      return self._RunMethod(
          config, request, global_params=global_params)

    Stop.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/pipelines/{pipelinesId}:stop',
        http_method='POST',
        method_id='datapipelines.projects.locations.pipelines.stop',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:stop',
        request_field='googleCloudDatapipelinesV1StopPipelineRequest',
        request_type_name='DatapipelinesProjectsLocationsPipelinesStopRequest',
        response_type_name='GoogleCloudDatapipelinesV1Pipeline',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(DatapipelinesV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(DatapipelinesV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
