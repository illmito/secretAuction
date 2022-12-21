import os
import art as gfx

logo = gfx.logo
winnerBanner = gfx.winner
noMoreBids = gfx.finish
bids_taken = {}

def highest_bidder(bidding_record):
    print(noMoreBids)
    input("--- All Bidding has ceased! ---\n\n\nPress 'ENTER' to reveal winner")
    os.system('cls')

    top_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > top_bid:
            top_bid = bid_amount
            winner = bidder
    print(winnerBanner)
    print(f"Congratulation to {winner}, with a bid of ${top_bid}")

# initial text
print(logo)
print("Welcome to the secret Auction Program!\n")

active_bid = True
while active_bid:
    name = input("Please input your name: ")
    bid = int(input(f"\nThank you {name}, Please place your Bid: $"))
    bids_taken[name] = bid

    add_bid = input("\nAre there anymore bids?, 'yes' or 'no' :")
    if add_bid == 'no':
        active_bid = False
        os.system('cls')
        highest_bidder(bids_taken)
    elif add_bid == 'yes':
        os.system('cls')
    else:
        input(f"'{add_bid}' INVALID INPUT...\nAre there anymore bids?, 'yes' or 'no'")



