# from decouple import config
# from typing import Union
# from assets import sender_private_key, sender_public_key
# from algosdk import mnemonic


from algosdk.future.transaction import AssetTransferTxn
from algosdk.util import algos_to_microalgos
from utility import is_node_connected, wait_for_confirmation


def Transfer_Or_optIn_To_An_Asset(senderPubKey: str, receiverPubKey: str, amount: int, assetId: int, signerPrivateKey: str):
    # Use the AssetTransferTxn class to opt-in to an asset or make a transfer of an asset
    # Opt-in, This means you are giving your consent to receive the asset specified in this transaction
    # to opt-in to an asset, the AssetTransferTxn takes amt=0
    # best to check if an account already has opt-in to an asset before trying to opt-in again
    client = is_node_connected()  # utility function
    params = client[1].suggested_params()
    params.fee = 1000
    params.flat_fee = True
    transaction = AssetTransferTxn(
        sender=senderPubKey,
        sp=params,
        receiver=receiverPubKey,
        amt=algos_to_microalgos(amount),  # assuming the asset has 6 decimal
        index=assetId)
    signed_transaction = transaction.sign(signerPrivateKey)
    transaction_Id = client[1].send_transaction(signed_transaction)
    # submit and Wait for the transaction to be confirm on testnet
    confirmed_transaction = wait_for_confirmation(client[1], transaction_Id)
    # return both transaction confirmed and transaction_id
    return confirmed_transaction, transaction_Id


# receiver = config("TEST_KEY_PAIR")

# pub = mnemonic.to_public_key(receiver)
# private_key = mnemonic.to_private_key(receiver)
# print(f"receiving account {pub}")


# print(Transfer_optIn_Asset(senderPubKey=sender_public_key, receiverPubKey=pub, amount=10, assetId=88469696, signerPrivateKey=sender_private_key))
