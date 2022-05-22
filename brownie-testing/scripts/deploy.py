from brownie import accounts, SimpleStorage


def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage.address)

    simple_storage.setNumber(777, {"from": account})
    print(simple_storage.number())

    return simple_storage


def main():
    deploy_simple_storage()