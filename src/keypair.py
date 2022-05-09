from algosdk import account, mnemonic


def generate_algorand_keypair():
    private_key, address = account.generate_account()
    mnemonic_ = mnemonic.from_private_key(private_key)
    return {"public_address":address, "private_key":private_key, "mnemonic phrase":mnemonic_}
    




# accts = generate_algorand_keypair()

# print(accts)


