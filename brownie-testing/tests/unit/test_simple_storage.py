from scripts.deploy import deploy_simple_storage
from brownie import accounts


def test_can_set_number():
    #Arrange
    simple_storage = deploy_simple_storage()
    account = accounts[0]
    expected = 777

    #Act
    tx = simple_storage.setNumber(expected, {"from": account})
    tx.wait(1)

    #Assert
    assert simple_storage.number() == expected


def test_dummy():
    some_number = 8
    some_other_number = 8
    assert some_number == some_other_number
