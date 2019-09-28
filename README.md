# shoppy-mcshopface
Flask API for fictional grocery store

Shoppy McShopFace 
Flask API

Resources:

	Endpoints:

	GET: 												
	
	/grocery_items 
		-Returns all grocery items currently in store

	/grocery_item/id=<id>
		-Returns specific grocery item in store based on id
		-If id is given which doesn't not correspond to a product in the store, 		
    "Item not found” is returned

	/purchase_log
		-Returns log of all purchases

	POST:												

	/itemlist_price
		-Returns the price of a given list of posted item ids.

		 -Request body accepts list of product ids in the following 							  
     format: 
			{
			  "ids": ["1", "2", “1”]
			}
		
			-If request body contains incorrect fields or an empty list, the message 			  	   	
      "No purchase item ids specified” will be returned

	PUT: 												
				
	/purchase
		-Endpoint to make a purchase of one or more products

		-Request body accepts list of product ids and money sent in the following 				
    format:
			{
			  “ids”: [“1”, “2”, “1”], 
			  “money_sent”: “15”
			}
		
		-If the value of “money_sent” in the request body is less than the total price of 				
    the items, the message "Insufficient funds sent” will be returned. If the amount 				
    equals or exceeds the total price of all items in the “ids” array, the response will 				
    be: 
			{
			  “customer_change”: “AMOUNT”
			}
