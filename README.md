# log-analyser

## FIX 4.4
- Stock Code - 55
- Transaction Quantity - 14
- Transaction Price - 6
- Transaction Side (Buy/Sell) - 54 val
  - 1 buy, 2 sell
- Account - 1
- Transaction Reference ID - 11 Buyer ID, 37 Seller ID
- Transaction Time - 60



#### 2) a. What were the orders that the account sent? b. And what are the account’s positions now?
```
Orders that were sent were buy orders for Tencent, Semiconductor Manufacturing International Corp, Lenovo Group, and Meitu.
Positions:
- 698 shares of Tencent, bought at 17450 total cost, avg price of 25/share
- 9999 shares of Semiconductor and Meitu, both bought at 249975 total cost, both avg price of 25/share
- 21999 shares of Lenovo Group, bought at 549975 total cost, avg price of 25/share 
```


#### 3) The client has left you a message that “something seems wrong” and she is in meeting for therest of the day. Could you investigate and see what might be wrong in her eyes? How would you proceed the investigation?
```
I would proceed by having a rough look at the CSV/logs to see if anything looks strange.
Investigation Results:
The system always sends a buy order for 0 shares at 0 dollars before it starts transactions, wasting 1 to 3 seconds in transaction time, 
which is precious in the finance world.
```

### References:
- https://www.onixs.biz/fix-dictionary/4.4/fields_by_tag.html
- https://btobits.com/fixopaedia/fixdic44/fields_by_tag_.html
