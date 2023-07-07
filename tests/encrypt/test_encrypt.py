# from challenges.challenge_encrypt_message import encrypt_message

import pytest
from challenges.challenge_encrypt_message import encrypt_message

message = "batatinha"
odd_key = 5
even_key = 4
invalid_message = 10
invalid_key = "4"


def test_correct_encrypt_odd():
    encrypt = encrypt_message(message, odd_key)
    assert encrypt == 'tatab_ahni'


def test_correct_encrypt_even():
    encrypt = encrypt_message(message, even_key)
    assert encrypt == 'atab_anhit'


def test_message_error():
    with pytest.raises(TypeError, match="invalid message type"):
        encrypt_message(invalid_message, even_key)


def test_invalid_key():
    with pytest.raises(TypeError, match="invalid key type"):
        encrypt_message(message, invalid_key)