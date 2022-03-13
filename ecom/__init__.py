__version__ = "0.0.1"
from datetime import date
from urllib import response
import frappe
import requests
from json import loads


def add_item_and_category():
    add_categores()
    add_items()
    add_price()


def add_categores():
    url = "https://fakestoreapi.com/products/categories"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        data = loads(response.text)
        for category in data:
            cat = category.title()
            if not frappe.db.get_value("Item Group", cat, "name"):
                doc = frappe.new_doc("Item Group")
                doc.item_group_name = cat
                doc.parent_item_group = "All Item Groups"
                doc.save(ignore_permissions=True)


def add_items():
    url = "https://fakestoreapi.com/products"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        data = loads(response.text)
        for item in data:
            if not frappe.db.get_value("Item", item["title"].title(), "name"):
                doc = frappe.new_doc("Item")
                doc.item_code = item["title"].title()
                doc.item_name = item["title"].title()
                doc.image = item["image"]
                doc.description = item["description"]
                doc.item_group = item["category"].title()
                doc.is_stock_item = 0
                doc.stock_uom = "Nos"
                doc.save(ignore_permissions=True)


def add_price():
    url = "https://fakestoreapi.com/products"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        data = loads(response.text)
        for item in data:
            if not frappe.db.get_value(
                "Item Price",
                {"item_code": item["title"].title(), "selling": 1},
                "name",
            ):
                doc = frappe.new_doc("Item Price")
                doc.item_code = item["title"].title()
                doc.price_list = "Standard Selling"
                doc.price_list_rate = item["price"]
                doc.save(ignore_permissions=True)
