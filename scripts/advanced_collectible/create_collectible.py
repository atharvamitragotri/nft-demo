from web3 import Web3
from brownie import AdvancedCollectible
from scripts.helpful_scripts import fund_with_link, get_account, get_contract


def main():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address,amount = Web3.toWei(0.1,"ether"))
    create_transaction = advanced_collectible.createCollectible({"from":account})
    create_transaction.wait(1)
    print("Collectible created!")
