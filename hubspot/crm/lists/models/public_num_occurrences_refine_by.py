# coding: utf-8

"""
    Lists

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.crm.lists.configuration import Configuration


class PublicNumOccurrencesRefineBy(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"max_occurrences": "int", "type": "str", "min_occurrences": "int"}

    attribute_map = {"max_occurrences": "maxOccurrences", "type": "type", "min_occurrences": "minOccurrences"}

    def __init__(self, max_occurrences=None, type="NUM_OCCURRENCES", min_occurrences=None, local_vars_configuration=None):  # noqa: E501
        """PublicNumOccurrencesRefineBy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._max_occurrences = None
        self._type = None
        self._min_occurrences = None
        self.discriminator = None

        if max_occurrences is not None:
            self.max_occurrences = max_occurrences
        self.type = type
        if min_occurrences is not None:
            self.min_occurrences = min_occurrences

    @property
    def max_occurrences(self):
        """Gets the max_occurrences of this PublicNumOccurrencesRefineBy.  # noqa: E501


        :return: The max_occurrences of this PublicNumOccurrencesRefineBy.  # noqa: E501
        :rtype: int
        """
        return self._max_occurrences

    @max_occurrences.setter
    def max_occurrences(self, max_occurrences):
        """Sets the max_occurrences of this PublicNumOccurrencesRefineBy.


        :param max_occurrences: The max_occurrences of this PublicNumOccurrencesRefineBy.  # noqa: E501
        :type max_occurrences: int
        """

        self._max_occurrences = max_occurrences

    @property
    def type(self):
        """Gets the type of this PublicNumOccurrencesRefineBy.  # noqa: E501


        :return: The type of this PublicNumOccurrencesRefineBy.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PublicNumOccurrencesRefineBy.


        :param type: The type of this PublicNumOccurrencesRefineBy.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["NUM_OCCURRENCES"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `type` ({0}), must be one of {1}".format(type, allowed_values))  # noqa: E501

        self._type = type

    @property
    def min_occurrences(self):
        """Gets the min_occurrences of this PublicNumOccurrencesRefineBy.  # noqa: E501


        :return: The min_occurrences of this PublicNumOccurrencesRefineBy.  # noqa: E501
        :rtype: int
        """
        return self._min_occurrences

    @min_occurrences.setter
    def min_occurrences(self, min_occurrences):
        """Sets the min_occurrences of this PublicNumOccurrencesRefineBy.


        :param min_occurrences: The min_occurrences of this PublicNumOccurrencesRefineBy.  # noqa: E501
        :type min_occurrences: int
        """

        self._min_occurrences = min_occurrences

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublicNumOccurrencesRefineBy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicNumOccurrencesRefineBy):
            return True

        return self.to_dict() != other.to_dict()