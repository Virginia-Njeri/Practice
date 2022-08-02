






from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notifications, Receipt, Reward, Third_Party, Wallet,Transaction


# # class CustomerAdmin(admin.ModelAdmin):
    
#     list_display=("firstname","lastname","address",)
#     search_fields=("firstname","lastname",)

admin.site.register(Customer)
admin.site.register(Wallet)    
admin.site.register(Account)     
admin .site.register(Transaction)
admin.site.register(Card)
admin.site.register(Third_Party) 
admin.site.register(Notifications) 
admin.site.register(Receipt) 
admin.site.register(Loan) 
admin.site.register(Reward)

