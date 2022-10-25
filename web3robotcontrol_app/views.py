from django.shortcuts import redirect, render
from web3 import Web3
import json

infura_url = "https://mainnet.infura.io/v3/45062ae6965241ae891cced9e6a91d12"
web3 = Web3(Web3.HTTPProvider(infura_url))

abi = json.loads("[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "changeOwner",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "oldOwner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnerSet",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "getOwner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]")
address = "0x17F6AD8Ef982297579C203069C1DbfFE4348c372"
contract = web3.eth.contract(address=address, abi=abi)

def addblockView(request):
    print(contract.functions.OwnerSet().send())


def showblockView(request):
    print(contract.functions.changeOwner().call())


def stillExists(request):
    print(contract.functions.changeOwner().call())