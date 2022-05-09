from utility import is_node_connected
import json

#get info of an address, including the assets it opt-in to, their balance, 
#status of those assets, address local state, address schema, etc 
def address_balance_details(address_pub: str) -> dict:
    node_status, algo_client = is_node_connected()
    if node_status == True:
        balance = algo_client.account_info(address_pub)
        return(json.dumps(balance, indent=4))
    




# bal = address_balance_details(
#     "7RQYIUXCHWNX4OJ25SA7NLXU4GQJYXH3S3JHVBLC5SLQRJ7AJ32GYWXJFQ")
# print(bal)


# import json
# import time
# import base64
# from algosdk.v2client import algod
# from algosdk import mnemonic
# from algosdk import transaction
# from decouple import config
# # Function from Algorand Inc.




# # Setup HTTP client w/guest key provided by PureStake
# algod_token = config("NODE_TOKEN")
# algod_address = 'https://testnet-algorand.api.purestake.io/ps2'
# purestake_token = {'X-Api-key': algod_token}

# # Initalize throw-away account for this example - check that is has funds before running script
# mnemonic_phrase = 'laundry tool mail zero goose language letter muscle indoor despair fold anxiety swallow enable vital casino rigid awful maple burst demand fit divorce abandon actor'
# account_private_key = mnemonic.to_private_key(mnemonic_phrase)
# account_public_key = mnemonic.to_public_key(mnemonic_phrase)

# algodclient = algod.AlgodClient(
#     algod_token, algod_address, headers=purestake_token)

# # get suggested parameters from Algod
# params = algodclient.suggested_params()

# gh = params.gh
# first_valid_round = params.first
# last_valid_round = params.last
# fee = params.min_fee
# send_amount = 1

# existing_account = account_public_key
# send_to_address = 'AEC4WDHXCDF4B5LBNXXRTB3IJTVJSWUZ4VJ4THPU2QGRJGTA3MIDFN3CQA'

# # Create and sign transaction
# tx = transaction.PaymentTxn(existing_account, fee, first_valid_round,
#                             last_valid_round, gh, send_to_address, send_amount, flat_fee=True)
# signed_tx = tx.sign(account_private_key)

# try:
#     tx_confirm = algodclient.send_transaction(signed_tx)
#     print('Transaction sent with ID', signed_tx.transaction.get_txid())
#     wait_for_confirmation(algodclient, txid=signed_tx.transaction.get_txid())
# except Exception as e:
#     print(e)




