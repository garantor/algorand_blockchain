from algosdk.v2client import algod
import json


def is_node_connected():
    endpoint_address = "https://testnet-algorand.api.purestake.io/ps2"
    purestake_key = "rmhNxVQCJT45KFzrrhtHmfs2wiUKGY57sDfT9jf0"
    purestake_header = {'X-Api-key': purestake_key}
    algod_client = algod.AlgodClient(
        purestake_key, endpoint_address, headers=purestake_header)

    status = algod_client.status()
    # Check connection status looking using the catchup-time and transaction comfirmation time
    if status["catchup-time"] == 0 and status["time-since-last-round"] <= 4261519666:
        return True, algod_client
    return False


#   Utility function used to print created asset for account and assetid
def print_created_asset(algodclient, account, assetid):
    # note: if you have an indexer instance available it is easier to just use this
    # response = myindexer.accounts(asset_id = assetid)
    # then use 'account_info['created-assets'][0] to get info on the created asset
    account_info = algodclient.account_info(account)
    idx = 0
    for my_account_info in account_info['created-assets']:
        scrutinized_asset = account_info['created-assets'][idx]
        idx = idx + 1
        if (scrutinized_asset['index'] == assetid):
            asset_id = f"Asset ID: {scrutinized_asset['index']}"
            acct_info = json.dumps(my_account_info['params'], indent=4)
            return asset_id, acct_info
            
            



#   Utility function used to print asset holding for account and assetid
def print_asset_holding(algodclient, account, assetid):
    # note: if you have an indexer instance available it is easier to just use this
    # response = myindexer.accounts(asset_id = assetid)
    # then loop thru the accounts returned and match the account you are looking for
    account_info = algodclient.account_info(account)

    idx = 0
    for my_account_info in account_info['assets']:
        scrutinized_asset = account_info['assets'][idx]
        idx = idx + 1        
        if (scrutinized_asset['asset-id'] == assetid):
            asset_id = f"Asset ID: {scrutinized_asset['asset-id']}"
            # acct_info = json.dumps(my_account_info['params'], indent=4)
            return asset_id, my_account_info
            # print("Asset ID: {}".format(scrutinized_asset['asset-id']))
            # print(json.dumps(scrutinized_asset, indent=4))
            # break
    # account_info = algod_client.account_info(my_address)
#     # print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")
    

def wait_for_confirmation(client, txid):
    last_round = client.status().get('last-round')
    txinfo = client.pending_transaction_info(txid)
    while not (txinfo.get('confirmed-round') and txinfo.get('confirmed-round') > 0):
        print('Waiting for confirmation')
        last_round += 1
        client.status_after_block(last_round)
        txinfo = client.pending_transaction_info(txid)
    print('Transaction confirmed in round', txinfo.get('confirmed-round'))
    return txinfo

# print(is_node_connected())
# My address: Q4H7IINJ7H6NUNERBWCSYDH3T2WXDHLS3YMIUHBYFG6CWXQSQQYGEGBGUY
# My private key: 7St5DPtPsvMRkJGYAw+1oIBtJaF+I88tBA/tER1fAQiHD/Qhqfn82jSRDYUsDPuerXGdct4Yihw4KbwrXhKEMA ==
# My passphrase: laundry tool mail zero goose language letter muscle indoor despair fold anxiety swallow enable vital casino rigid awful maple burst demand fit divorce abandon actor


# print(print_asset_holding(is_node_connected()[
#       1], account="JUH6PM2RXY7BTQ4H6U56UMXWSVQTDGDRZ67QMJKPFBVSOXFCFRSPMW7WM4", assetid=88469696))
