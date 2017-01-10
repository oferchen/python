# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1-660c2a2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1alpha1ClusterRoleBinding(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_version=None, kind=None, metadata=None, role_ref=None, subjects=None):
        """
        V1alpha1ClusterRoleBinding - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_version': 'str',
            'kind': 'str',
            'metadata': 'V1ObjectMeta',
            'role_ref': 'V1alpha1RoleRef',
            'subjects': 'list[V1alpha1Subject]'
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'kind': 'kind',
            'metadata': 'metadata',
            'role_ref': 'roleRef',
            'subjects': 'subjects'
        }

        self._api_version = api_version
        self._kind = kind
        self._metadata = metadata
        self._role_ref = role_ref
        self._subjects = subjects


    @property
    def api_version(self):
        """
        Gets the api_version of this V1alpha1ClusterRoleBinding.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1alpha1ClusterRoleBinding.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1alpha1ClusterRoleBinding.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1alpha1ClusterRoleBinding.
        :type: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """
        Gets the kind of this V1alpha1ClusterRoleBinding.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1alpha1ClusterRoleBinding.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1alpha1ClusterRoleBinding.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1alpha1ClusterRoleBinding.
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """
        Gets the metadata of this V1alpha1ClusterRoleBinding.
        Standard object's metadata.

        :return: The metadata of this V1alpha1ClusterRoleBinding.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1alpha1ClusterRoleBinding.
        Standard object's metadata.

        :param metadata: The metadata of this V1alpha1ClusterRoleBinding.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def role_ref(self):
        """
        Gets the role_ref of this V1alpha1ClusterRoleBinding.
        RoleRef can only reference a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error.

        :return: The role_ref of this V1alpha1ClusterRoleBinding.
        :rtype: V1alpha1RoleRef
        """
        return self._role_ref

    @role_ref.setter
    def role_ref(self, role_ref):
        """
        Sets the role_ref of this V1alpha1ClusterRoleBinding.
        RoleRef can only reference a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error.

        :param role_ref: The role_ref of this V1alpha1ClusterRoleBinding.
        :type: V1alpha1RoleRef
        """
        if role_ref is None:
            raise ValueError("Invalid value for `role_ref`, must not be `None`")

        self._role_ref = role_ref

    @property
    def subjects(self):
        """
        Gets the subjects of this V1alpha1ClusterRoleBinding.
        Subjects holds references to the objects the role applies to.

        :return: The subjects of this V1alpha1ClusterRoleBinding.
        :rtype: list[V1alpha1Subject]
        """
        return self._subjects

    @subjects.setter
    def subjects(self, subjects):
        """
        Sets the subjects of this V1alpha1ClusterRoleBinding.
        Subjects holds references to the objects the role applies to.

        :param subjects: The subjects of this V1alpha1ClusterRoleBinding.
        :type: list[V1alpha1Subject]
        """
        if subjects is None:
            raise ValueError("Invalid value for `subjects`, must not be `None`")

        self._subjects = subjects

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
