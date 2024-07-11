from flask import request, jsonify, render_template
from app import app
from app.linkedlist import LinkedList

linked_list = LinkedList()

# class Node:
#     def __init__(self, val, next = None):
#         self.val = val
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.numItems = 0

#     def insert(self, val):
#         newNode = Node(val)
#         if (not self.head):
#             self.head = newNode
#         else:
#             curr = self.head
#             while (curr.next):
#                 curr = curr.next
#             curr.next = newNode
#         return val
    
#     def printList(self):
#         curr = self.head
#         while (curr):
#             print(curr.val)
#             curr = curr.next

# LL = LinkedList()
# j = LL.insert(1)
# g = str(j)
# LL.printList()

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/api/linkedlist/add', methods=["POST"])
def add_node():
    value = request.args.get('value', type=int)
    if value is not None:
        linked_list.add_node(value)
    return jsonify(linked_list.print_list())


@app.route('/api/linkedlist/remove', methods=["POST"])
def remove_node():
    value = request.args.get('value', type=int)
    if value is not None:
        linked_list.remove_node(value)
    return jsonify(linked_list.print_list())


@app.route('/api/linkedlist/reverse', methods=['POST'])
def reverse_list():
    linked_list.reverse()
    return jsonify(linked_list.print_list())


@app.route('/api/linkedlist/print', methods=['GET'])
def print_list():
    return jsonify(linked_list.print_list())


@app.route('/')
def index():
    return render_template('index.html')