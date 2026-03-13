from web3 import Web3

# Connect to Ethereum public node
w3 = Web3(Web3.HTTPProvider("https://cloudflare-eth.com"))

print("=== Ethereum Wallet Balance Checker ===")

address = input("Enter wallet address: ")

balance = w3.eth.get_balance(address)

eth_balance = w3.from_wei(balance, 'ether')

print("Balance:", eth_balance, "ETH")
