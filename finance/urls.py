from finance import views
from django.urls import path

urlpatterns = [
    path('bankreg',views.bank_forms,name="bankreg"),
    path('home',views.home,name="home"),
    path('supplierreg',views.supplier_form,name="supplier register"),
    path('customerreg',views.customer_form,name="customer register"),
    path('banklogin',views.bank_login,name='bank login'),
    path('supplierlogin',views.supplier_login,name='supplier login'),
    path('customerlogin',views.customer_login,name='customer login'),
    path('bankmain',views.bankmain,name="bank main"),
    path('requestinvoice',views.req_invoice,name='request invoice'),
    path('approveinvoice',views.approveinvoice,name='approve invoice'),
    path('suppliermain',views.suppliermain,name="supplier main"),
    path('customermain',views.customermain,name="customer main"),
    path('A_viewinvoice',views.A_viewinvoice,name=' approved view invoice'),
    path('D_viewinvoice',views.D_viewinvoice,name="deny view invoices"),
    path('viewinvoice',views.viewinvoice,name="view invoices"),
    path('oursuppliers',views.our_supplier,name="our suppliers"),
    path('ourcustomer',views.our_customer,name="our customer"),
    path('uploadin',views.up_invoice,name="upload invoice"),
    path('appstartinvoice',views.app_invoice,name="approve start page"),
    
]
