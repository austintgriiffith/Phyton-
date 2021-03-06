"""
    CryptoAPIs

    Crypto APIs 2.0 is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs 2.0 can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs 2.0 provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: developers@cryptoapis.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import cryptoapis
from cryptoapis.api.omni_layer_api import OmniLayerApi  # noqa: E501


class TestOmniLayerApi(unittest.TestCase):
    """OmniLayerApi unit test stubs"""

    def setUp(self):
        self.api = OmniLayerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_omni_transaction_details_by_transaction_id__txid(self):
        """Test case for get_omni_transaction_details_by_transaction_id__txid

        Get Omni Transaction Details By Transaction ID (Txid)  # noqa: E501
        """
        pass

    def test_get_unconfirmed_omni_transaction_by_transaction_id__txid(self):
        """Test case for get_unconfirmed_omni_transaction_by_transaction_id__txid

        Get Unconfirmed Omni Transaction By Transaction ID (Txid)  # noqa: E501
        """
        pass

    def test_list_omni_tokens_by_address(self):
        """Test case for list_omni_tokens_by_address

        List Omni Tokens By Address  # noqa: E501
        """
        pass

    def test_list_omni_transactions_by_address(self):
        """Test case for list_omni_transactions_by_address

        List Omni Transactions By Address  # noqa: E501
        """
        pass

    def test_list_omni_transactions_by_block_hash(self):
        """Test case for list_omni_transactions_by_block_hash

        List Omni Transactions By Block Hash  # noqa: E501
        """
        pass

    def test_list_omni_transactions_by_block_height(self):
        """Test case for list_omni_transactions_by_block_height

        List Omni Transactions By Block Height  # noqa: E501
        """
        pass

    def test_list_unconfirmed_omni_transactions_by_address(self):
        """Test case for list_unconfirmed_omni_transactions_by_address

        List Unconfirmed Omni Transactions By Address  # noqa: E501
        """
        pass

    def test_list_unconfirmed_omni_transactions_by_property_id(self):
        """Test case for list_unconfirmed_omni_transactions_by_property_id

        List Unconfirmed Omni Transactions By Property ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
