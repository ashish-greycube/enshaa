import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def after_migrate():
    custom_fields = {
        "Purchase Invoice": [
            dict(
                fieldname="custom_so_reference",
                label="SO Reference",
                fieldtype="Link",
                options="Sales Order",
                insert_after="tax_withholding_category",
                translatable=0,
                is_system_generated=0,
                is_custom_field=1,
		    ),
        ],

        "Journal Entry": [
            dict(
                fieldname="custom_so_reference",
                label="SO Reference",
                fieldtype="Link",
                options="Sales Order",
                insert_after="apply_tds",
                translatable=0,
                is_system_generated=0,
                is_custom_field=1,
            ),
        ],

        "Stock Entry Detail": [
            dict(
                fieldname="custom_references",
                label="References",
                fieldtype="Section Break",
                insert_after="sample_quantity",
                translatable=0,
                is_system_generated=0,
                is_custom_field=1,
            ),
            dict(
                fieldname="custom_sales_order",
                label="Sales Order",
                fieldtype="Link",
                options="Sales Order",
                insert_after="custom_references",
                translatable=0,
                is_system_generated=0,
                is_custom_field=1,
            ),
        ],
        
    }
    print("Creating custom fields for app Enshaa")
    for dt, fields in custom_fields.items():
        print("*******\n %s: " % dt, [d.get("fieldname") for d in fields])
    create_custom_fields(custom_fields)