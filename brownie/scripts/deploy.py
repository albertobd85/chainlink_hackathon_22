from brownie import SimpleStorage, accounts


def main():
    account = accounts[0]
    simple_storage_contract = SimpleStorage.deploy({"from": account})
    print(simple_storage_contract.number())

    simple_storage_contract.setNumber(777, {"from": account})
    print(simple_storage_contract.number())
