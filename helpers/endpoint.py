import requests
from utils import merge_headers

"""
endpoint.py
===========

Description:

Endpoint offers basic Request functionality using the Requests library.

"""


class Endpoint:
    def __init__(self, base_uri, default_headers=None):
        """
        :param base_uri:            is a String, such as "https://the.server.com/" trailing / included
        :param default_headers:     is a dict, which is merged with any headers specifically provided;
                                     the default, if nothing is provided, is the Content-Type used for hoodoo requests.
        """
        self.base_uri = base_uri
        self.default_headers = default_headers

    def post(self, path, body, headers=None):
        """
        POST method.

        :param path:       is the path as a String to the endpoint or resource following the
                            base_uri, such as "foo/some_endpoint/" (Note: trailing / included)
        :param body:       is the string body content
        :param headers:    are a dictionary of strings; they are merged to the default_headers
                            merged dictionaries in Python mean that headers takes precedence over
                            duplicates in default_headers
        :return:           a Response object as per http://docs.python-requests.org/en/master/api/#requests.Response
        """
        if headers is not None:
            merged_headers = merge_headers(self.default_headers, headers)
        else:
            merged_headers = self.default_headers
        full_path_name = self.base_uri + path
        return requests.post(full_path_name, headers=merged_headers, data=body)

    def patch(self, path, identifier, body, headers=None):
        """
        PATCH method.

        :param path:       is the path as a String to the endpoint or resource following the
                            base_uri, such as "foo/baz_endpoint/" trailing / included
        :param identifier:         is the identifier of the resource to update
        :param body:       is the string body content
        :param headers:    are a dictionary of strings; they are merged to the default_headers
                            merged dictionaries in Python mean that headers takes precedence over
                            duplicates in default_headers
        :return:           a Response object as per http://docs.python-requests.org/en/master/api/#requests.Response
        """
        if headers is not None:
            merged_headers = merge_headers(self.default_headers, headers)
        else:
            merged_headers = self.default_headers
        full_path_name = self.base_uri = path + "/" + identifier
        return requests.patch(full_path_name, headers=merge_headers, data=body)
    
    def put(self, path, identifier, body, headers=None):
        """
        PUT is typically used to overwrite an identified instance
        
        :param path:        is the path as a String to the endpoint or resource following the
                                base_uri, such as "foo/baz_endpoint/" trailing / included
        :param identifier:  the identifier of the resource to update
        :param body:        the body to PUT
        :param headers:     are a dictionary of strings; they are merged to the default_headers
                                merged dictionaries in Python mean that headers takes precedence over
                                duplicates in default_headers
        :return:            a Response object as per http://docs.python-requests.org/en/master/api/#requests.Response
        """
        if headers is not None:
            merged_headers = merge_headers(self.default_headers, headers)
        else:
            merged_headers = self.default_headers
        full_path_name = self.base_uri + path
        return requests.post(full_path_name, headers=merged_headers, data=body)

    def get(self, path, identifier, headers=None):
        """
        GET an item by its identifier.
        
        :param path:            is the path as a String to the endpoint or resource following the
                                    base_uri, such as "foo/baz_endpoint/" trailing / included
        :param identifier:      is the identifier of the resource to show
        :param headers:         are a dictionary of strings; they are merged to the default_headers
                                    merged dictionaries in Python mean that headers takes precedence over
                                    duplicates in default_headers
        :return:                a Response object as per http://docs.python-requests.org/en/master/api/#requests.Response
        """
        if headers is not None:
            merged_headers = merge_headers(self.default_headers, headers)
        else:
            merged_headers = self.default_headers
        full_path_name = self.base_uri + path + identifier
        return requests.get(full_path_name, headers=merged_headers)

    def get_with_params(self, path, headers=None, params=None):
        """
        Fot use when query parameters is supported using GET method.
        Query parameters are supported using requests library, where you pass parameters as a dict.

        :param path:            is the path as a String to the endpoint or resource following the
                                    base_uri, such as "foo/baz_endpoint/" trailing / included
        :param headers:         are a dictionary of strings; they are merged to the default_headers
                                    merged dictionaries in Python mean that headers takes precedence over
                                    duplicates in default_headers
        :param params           are a dictionary of (string) parameters that should be used in the query string
        :return:                a Response object as per http://docs.python-requests.org/en/master/api/#requests.Response
        """
        if params is None:
            raise RuntimeError("Params is a required field and can not be None.")
        if headers is not None:
            merged_headers = merge_headers(self.default_headers, headers)
        else:
            merged_headers = self.default_headers
        full_path_name = self.base_uri + path
        return requests.get(full_path_name, headers=merged_headers, params=params)

    def delete(self, path, identifier, headers=None):
        """
        The DELETE method. Specify the identifier to be deleted.

        :param path:            is the path as a String to the endpoint or resource following the
                                    base_uri, such as "foo/baz_endpoint/" trailing / included
        :param identifier:      is the identifier of the resource to delete
        :param headers:         are a dictionary of strings; they are merged to the default_headers
                                    merged dictionaries in Python mean that headers takes precedence over
                                    duplicates in default_headers
        :return:                a Response object as per http://docs.python-requests.org/en/master/api/#requests.Response
        """
        if headers is not None:
            merged_headers = merge_headers(self.default_headers, headers)
        else:
            merged_headers = self.default_headers
        full_path_name = self.base_uri + path + identifier
        return requests.delete(full_path_name, headers=merged_headers)
