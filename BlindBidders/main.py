def highest_amount(bid_details):
    high_bid = 0
    winner = ""
    for item in bid_details:
        if details[item] > high_bid:
            high_bid = details[item]
            winner = item
    print(f"The winner is {winner} with a bid of ${high_bid}")

keep_bidding = True
details = {}
while keep_bidding:

    name = input("What is your name?\n ")
    bid = int(input("What's your bid?\n$"))
    details[name] = bid

    other_user = input("Are there any bidders? Type 'yes' or 'no' ")
    if other_user == "no":
        highest_amount(bid_details= details)
        keep_bidding = False



