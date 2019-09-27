from flask import Flask, jsonify, request
from grocery_data import grocery_items, purchase_log
import datetime

app = Flask(__name__)

# class Log:
#     def __init__(self,ids = 0,time = 0):
#         self.ids = ids
#         self.timestamp = time

# GET all grocery items
@app.route("/grocery_items", methods=['GET'])
def get_groceryitems():
    return jsonify({'grocery_items': grocery_items})


# GET individual grocery item by id
@app.route("/grocery_item/id=<int:id>", methods=['GET'])
def get_groceryitem(id):
    # TODO: check if num is in range of ids in grocery_items, otherwise it borks
    item = [item for item in grocery_items if item['id'] == id]
    return jsonify({'grocery_items': item})


# POST computes and returns total price of list of items
# body accepts list of product ids: {"ids": ["1", "2", "1"]}
@app.route("/itemlist_price", methods=['POST'])
def itemlist_price():
    # 'ids' is list of id numbers
    ids = request.json['ids']

    if len(ids) > 0:
        total = 0

        for num in ids:
            # TODO: check if num is in range of ids in grocery_items, otherwise it borks
            item = [item for item in grocery_items if item['id'] == int(num)]
            total += int(item[0]['price'])
        return(jsonify({'purchase_total': total}))
    else:
        return "No purchase item ids specified"


# POST body accepts list of product ids and money sent:
#  {"ids": ["1", "2", "1"], "money_sent": "15"}
@app.route("/purchase_total", methods=['POST'])
def purchase_items():
    # 'ids' is list of id numbers
    ids = request.json['ids']
    monies = int(request.json['money_sent'])

    if len(ids) > 0:
        total = 0
        changeToReturn = 0
        shoppinglist = []

        for num in ids:
            # TODO: check if num is in range of ids in grocery_list, otherwise it borks
            item = [item for item in grocery_items if item['id'] == int(num)]
            shoppinglist.append(item)
            total += int(item[0]['price'])

        if total <= monies:
            changeToReturn = monies - total
            return(jsonify({'customer_change': changeToReturn}))
        else:
            return "Insufficient funds sent"
    else:
        return "No purchase item ids specified"


# POST to purchase_log
@app.route("/put_test", methods=['POST'])
def update_log():
    ids = request.json['ids']
    created = datetime.datetime.now().timestamp()

    # log = Log(ids, created)

    # purchase_log.append(log)
    purchase_log.append(jsonify({"ids" : ids, "purchase_time": created}))
# jsonify({"purchase_time": created, "ids_in_purchase": ids})
    return  'ok!' # jsonify({"purchase_log": purchase_log})

        
# GET log of purchase history 
@app.route("/purchase_log", methods=['GET'])
def get_purchase_log():
    return jsonify({'purchase_log': purchase_log})


if __name__ == '__main__':
    app.run(debug=True)