""" Python test functions to check the MorseCoder class

Run with pytest -v
"""

from morse_class import MorseCoder

def test_for_sample_message_encrypted_message():
    m = MorseCoder()
    message = "- .... .. ... / .. ... / .- / - . ... - / -- . ... ... .- --. ."
    expected_result = "THIS IS A TEST MESSAGE"

    assert m.decrypt(message) == expected_result

def test_for_sample_message_plain_message():
    m = MorseCoder()
    message = 'Hello world'
    expected_result = '.... . .-.. .-.. --- / .-- --- .-. .-.. -.. '

    assert m.encrypt(message.upper()) == expected_result
