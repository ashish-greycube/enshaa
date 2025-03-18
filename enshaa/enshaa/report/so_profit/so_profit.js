// Copyright (c) 2025, GreyCube Technologies and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["SO Profit"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label":__("From Date"),
			"fieldtype": "Date",
            "default": frappe.datetime.add_days(frappe.datetime.nowdate(), -30)
		},
		{
			"fieldname": "to_date",
			"label":__("To Date"),
			"fieldtype": "Date",
            "default": frappe.datetime.nowdate()
		},
		{
			"fieldname": "customer",
			"label":__("Customer"),
			"fieldtype": "Link",
			"options": "Customer"
		},
		{
			"fieldname": "sales_partner",
			"label":__("Sales Partner"),
			"fieldtype": "Link",
			"options": "Sales Partner"
		},
	]
};
