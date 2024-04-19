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


class PublicAdsSearchFilter(object):
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
    openapi_types = {"search_terms": "list[str]", "entity_type": "str", "ad_network": "str", "search_term_type": "str", "filter_type": "str", "operator": "str"}

    attribute_map = {"search_terms": "searchTerms", "entity_type": "entityType", "ad_network": "adNetwork", "search_term_type": "searchTermType", "filter_type": "filterType", "operator": "operator"}

    def __init__(self, search_terms=None, entity_type=None, ad_network=None, search_term_type=None, filter_type="ADS_SEARCH", operator=None, local_vars_configuration=None):  # noqa: E501
        """PublicAdsSearchFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._search_terms = None
        self._entity_type = None
        self._ad_network = None
        self._search_term_type = None
        self._filter_type = None
        self._operator = None
        self.discriminator = None

        self.search_terms = search_terms
        self.entity_type = entity_type
        self.ad_network = ad_network
        self.search_term_type = search_term_type
        self.filter_type = filter_type
        self.operator = operator

    @property
    def search_terms(self):
        """Gets the search_terms of this PublicAdsSearchFilter.  # noqa: E501


        :return: The search_terms of this PublicAdsSearchFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._search_terms

    @search_terms.setter
    def search_terms(self, search_terms):
        """Sets the search_terms of this PublicAdsSearchFilter.


        :param search_terms: The search_terms of this PublicAdsSearchFilter.  # noqa: E501
        :type search_terms: list[str]
        """
        if self.local_vars_configuration.client_side_validation and search_terms is None:  # noqa: E501
            raise ValueError("Invalid value for `search_terms`, must not be `None`")  # noqa: E501

        self._search_terms = search_terms

    @property
    def entity_type(self):
        """Gets the entity_type of this PublicAdsSearchFilter.  # noqa: E501


        :return: The entity_type of this PublicAdsSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this PublicAdsSearchFilter.


        :param entity_type: The entity_type of this PublicAdsSearchFilter.  # noqa: E501
        :type entity_type: str
        """
        if self.local_vars_configuration.client_side_validation and entity_type is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def ad_network(self):
        """Gets the ad_network of this PublicAdsSearchFilter.  # noqa: E501


        :return: The ad_network of this PublicAdsSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._ad_network

    @ad_network.setter
    def ad_network(self, ad_network):
        """Sets the ad_network of this PublicAdsSearchFilter.


        :param ad_network: The ad_network of this PublicAdsSearchFilter.  # noqa: E501
        :type ad_network: str
        """
        if self.local_vars_configuration.client_side_validation and ad_network is None:  # noqa: E501
            raise ValueError("Invalid value for `ad_network`, must not be `None`")  # noqa: E501

        self._ad_network = ad_network

    @property
    def search_term_type(self):
        """Gets the search_term_type of this PublicAdsSearchFilter.  # noqa: E501


        :return: The search_term_type of this PublicAdsSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._search_term_type

    @search_term_type.setter
    def search_term_type(self, search_term_type):
        """Sets the search_term_type of this PublicAdsSearchFilter.


        :param search_term_type: The search_term_type of this PublicAdsSearchFilter.  # noqa: E501
        :type search_term_type: str
        """
        if self.local_vars_configuration.client_side_validation and search_term_type is None:  # noqa: E501
            raise ValueError("Invalid value for `search_term_type`, must not be `None`")  # noqa: E501

        self._search_term_type = search_term_type

    @property
    def filter_type(self):
        """Gets the filter_type of this PublicAdsSearchFilter.  # noqa: E501


        :return: The filter_type of this PublicAdsSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this PublicAdsSearchFilter.


        :param filter_type: The filter_type of this PublicAdsSearchFilter.  # noqa: E501
        :type filter_type: str
        """
        if self.local_vars_configuration.client_side_validation and filter_type is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ADS_SEARCH"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and filter_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `filter_type` ({0}), must be one of {1}".format(filter_type, allowed_values))  # noqa: E501

        self._filter_type = filter_type

    @property
    def operator(self):
        """Gets the operator of this PublicAdsSearchFilter.  # noqa: E501


        :return: The operator of this PublicAdsSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this PublicAdsSearchFilter.


        :param operator: The operator of this PublicAdsSearchFilter.  # noqa: E501
        :type operator: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

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
        if not isinstance(other, PublicAdsSearchFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicAdsSearchFilter):
            return True

        return self.to_dict() != other.to_dict()