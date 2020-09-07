
# A block of publicly traded stock has a variety of attributes. Let's look at a few of them. A stock has a ticker symbol and a company name. Create a simple dictionary with ticker symbols and company names.

stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "GE": "General Electric"
}

# Create a simple list of blocks of stock. Make them tuples with ticker symbols, number of shares, dates and price.

purchases = [
    ( 'GM', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GM', 200, '1-jul-1998', 56 )
]

# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

# Example output for one block: I purchased General Electric stock for $4800

for purchase in purchases:

    # print(f"I purchased {stockDict[purchase[0]]} stock for ${purchase[1] * purchase[3]}.")
    print(f'I bought {stockDict[purchase[0]]} stocks for ${purchase[1] * purchase[3]}')