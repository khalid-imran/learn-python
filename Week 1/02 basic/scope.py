balance = 5000
def deduct(sell):
    # balance can be access in local scope but not update the value
    # to update the value we need to add global kwyword
    global balance
    newBalance = sell + balance
    print(f"balance after cell: {newBalance}")

deduct(1000)