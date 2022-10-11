def wallet():
    values = input("Provide cash values for respective wallets (separate the values by space): ")
    wallets = values.split()
    for i in range(len(wallets)):
        wallets[i] = int(wallets[i])
    fattest = max(wallets)
    skinniest = min(wallets)
    total = sum(wallets)
    dimes = total/10
    print("The fattest wallet has", fattest, "in it.")
    print("The skinniest wallet has", skinniest, "in it.")
    print("All together, these wallets have a total of", total, "in them.")
    print("All together, the total value of these wallets is worth", dimes, "dimes.")
