def calculate_total(prices):
    count=0
    for i in prices:
        count=count+i
    return count

def apply_tax(amount):
    return (amount+amount*0.05)
