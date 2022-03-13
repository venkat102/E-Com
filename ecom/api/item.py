import frappe

# Get Item
@frappe.whitelist(allow_guest=True)
def get_item():
    item_data = frappe.db.sql(
        """
        select 
            it.item_name as name,
            it.description as description,
            it.image as image,
            it.rating as rating,
            ip.price_list_rate as price,
            count(cmt.name) as comments,
            it.modified as modified
        from
            `tabItem` it
        left join
            `tabItem Price` ip
        on
            it.item_code = ip.item_code
        left join
            `tabItem Comments` cmt
        on
            it.item_code = cmt.item
        group by
            it.item_code
        order by
            it.item_name
    """,
        as_dict=True,
    )
    return {"length": len(item_data), "item": item_data}
