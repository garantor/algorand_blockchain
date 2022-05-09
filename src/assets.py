
from decouple import config
from algosdk import mnemonic
from algosdk.future.transaction import AssetConfigTxn
from algosdk.future.transaction import *
from algosdk.util import algos_to_microalgos
from utility import is_node_connected, wait_for_confirmation
import json



def create_an_Asset(creatorPub_key: str, total_supply: int, asset_name:str, asset_unit_name:str,
                manager_acct: str, reserve_acct: str, freeze_acct: str, clawback_acct: str, 
                signerKey: str, url_path="https://path/to/my/asset/details"):
    #Create an Asset, with a default of 6 decimal
    algo_client = is_node_connected()[1] # utility function
    params = algo_client.suggested_params()  # params for token configuration
        
    CreateAssetTx = AssetConfigTxn(
        sender=creatorPub_key,
        sp=params,
        total=algos_to_microalgos(total_supply),
        default_frozen=False,
        unit_name=asset_unit_name,
        asset_name=asset_name,
        manager=manager_acct,
        reserve=reserve_acct,
        freeze=freeze_acct,
        clawback=clawback_acct,
        url=url_path,
        decimals=6)

    # Sign with secret key of creator
    signed_tx = CreateAssetTx.sign(signerKey)
    # submit transaction to the network.
    try:
        sub_transaction = algo_client.send_transaction(signed_tx)
        # Wait for the transaction confirmation
        confirmed_txn = wait_for_confirmation(algo_client, sub_transaction)
    except Exception as err:
        print(err)

    #returning newly created asset details
    return json.dumps(confirmed_txn, indent=4)
























mnemonic_phrase = config("MNEMONIC_PHRASE")


sender_private_key = mnemonic.to_private_key(mnemonic_phrase)
sender_public_key = mnemonic.to_public_key(mnemonic_phrase)


# algod_token = config("NODE_TOKEN") #purestake node api key
# algod_address = 'https://testnet-algorand.api.purestake.io/ps2' #testnet purestake url
# purestake_header = {'X-Api-key': algod_token} #purestake header

# algo_client = algod.AlgodClient(
#     algod_token, algod_address, headers=purestake_header)


manager_account = config("MANAGER_MNEMONIC")

# print(create_an_Asset(sender_public_key, 1000, "Test2", "TST2", mnemonic.to_public_key(manager_account),mnemonic.to_public_key(manager_account), mnemonic.to_public_key(manager_account), mnemonic.to_public_key(manager_account), sender_private_key))
