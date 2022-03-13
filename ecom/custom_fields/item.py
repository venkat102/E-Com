from pydoc import doc
import frappe


def create_rating_field():
    if not frappe.db.get_value(
        "Custom Field",
        {
            "dt": "Item",
            "fieldname": "rating",
        },
        "name",
    ):
        try:
            doc = frappe.new_doc("Custom Field")
            doc.dt = "Item"
            doc.module = "Ecom"
            doc.label = "Rating"
            doc.fieldtype = "Float"
            doc.insert_after = "is_fixed_asset"
            doc.default = 0
            doc.save()
        except:
            pass
