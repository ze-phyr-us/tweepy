import tests

def setup_module(module):
    module.client = tests.create_test_client()

def test_public_timeline():
    assert client.public_timeline()

