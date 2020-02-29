# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6219, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SubscriptionOperationOperations(object):
    """SubscriptionOperationOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~subscription_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get(
        self,
        operation_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SubscriptionCreationResult"
        """Get the status of the pending Microsoft.Subscription API operations.

        :param operation_id: The operation ID, which can be found from the Location field in the
         generate recommendation response header.
        :type operation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SubscriptionCreationResult or  or the result of cls(response)
        :rtype: ~subscription_client.models.SubscriptionCreationResult or None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.SubscriptionCreationResult"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-10-01-preview"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'operationId': self._serialize.url("operation_id", operation_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SubscriptionCreationResult', pipeline_response)

        if response.status_code == 202:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))

        if cls:
          return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get.metadata = {'url': '/providers/Microsoft.Subscription/subscriptionOperations/{operationId}'}