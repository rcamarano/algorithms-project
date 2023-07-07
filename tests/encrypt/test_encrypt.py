# from challenges.challenge_encrypt_message import encrypt_message

import pytest
from challenges.challenge_encrypt_message import encrypt_message

def test_encrypt_message():
    # Testes com chave ímpar
    assert encrypt_message("batatinha", 5) == "tatab_ahni"
    assert encrypt_message("batatinha", 3) == "tab_ahnita"
    assert encrypt_message("batatinha", 1) == "b_ahnitata"

    # Testes com chave par
    assert encrypt_message("batatinha", 4) == "ahnit_atab"
    assert encrypt_message("batatinha", 2) == "ahnitat_ab"
    assert encrypt_message("batatinha", 6) == "ahn_itatab"

    # Testes com chave fora dos limites
    assert encrypt_message("batatinha", 0) == "ahnitatab"
    assert encrypt_message("batatinha", 10) == "ahnitatab"

    # Testes com tipos inválidos
    with pytest.raises(TypeError):
        encrypt_message(10, 4)
        encrypt_message("batatinha", "4")
        encrypt_message("batatinha", 4.5)
        encrypt_message("batatinha", True)
        encrypt_message("batatinha", False)

    # Teste com string vazia
    assert encrypt_message("", 4) == ""
