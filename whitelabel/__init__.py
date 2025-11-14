# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# import frappe

# __version__ = '0.0.1'

# if frappe.conf and frappe.conf.get("app_logo_url"):
#     __logo__ = frappe.conf.get("app_logo_url") or '/assets/whitelabel/images/whitelabel_logo.jpg'
# else:
#     __logo__ = '/assets/whitelabel/images/whitelabel_logo.jpg'
from __future__ import unicode_literals

__version__ = '0.0.1'

__logo__ = '/assets/whitelabel/images/whitelabel_logo.jpg'

def _safe_import_frappe():
    """Delay frappe import to avoid setup errors during installation."""
    global __logo__
    try:
        import frappe
        if getattr(frappe, "conf", None) and frappe.conf.get("app_logo_url"):
            __logo__ = frappe.conf.get("app_logo_url") or '/assets/whitelabel/images/whitelabel_logo.jpg'
    except ImportError:
        # Frappe not yet available (during bench setup)
        pass

_safe_import_frappe()
