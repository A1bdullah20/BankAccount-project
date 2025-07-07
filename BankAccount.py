# BankAccount project by Abdullah ALnasser
from datetime import datetime

class BankAccount:
    def __init__(self, name):
        self.__balance = 0  # Encapsulation
        self.name = name

    def _get_time(self):
        now = datetime.now()

        days_ar = {
            'Saturday': 'السبت',
            'Sunday': 'الأحد',
            'Monday': 'الإثنين',
            'Tuesday': 'الثلاثاء',
            'Wednesday': 'الأربعاء',
            'Thursday': 'الخميس',
            'Friday': 'الجمعة'
        }

        months_ar = {
            'January': 'يناير',
            'February': 'فبراير',
            'March': 'مارس',
            'April': 'أبريل',
            'May': 'مايو',
            'June': 'يونيو',
            'July': 'يوليو',
            'August': 'أغسطس',
            'September': 'سبتمبر',
            'October': 'أكتوبر',
            'November': 'نوفمبر',
            'December': 'ديسمبر'
        }

        day_en = now.strftime("%A")
        month_en = now.strftime("%B")
        day_ar = days_ar[day_en]
        month_ar = months_ar[month_en]

        time_str = now.strftime("%I:%M%p")
        date_str = f"في يوم {day_ar}، {now.day} {month_ar} {now.year}، الساعة {time_str}"
        return date_str

    def deposit(self, amount):
        self.__balance += amount
        print(f" تم إيداع {amount} ريال لرصيدك البنكي {self._get_time()}.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print(" لا يمكن سحب المبلغ. الرصيد غير كافٍ.")
        else:
            self.__balance -= amount
            print(f" تم خصم {amount} ريال من رصيدك البنكي {self._get_time()}.")

    def check_balance(self):
        print(f" رصيدك الحالي هو: {self.__balance} ريال")


# Use the software
account1 = BankAccount("عبدالله") # Name Account
account1.deposit(8000) # Deposit
account1.withdraw(150) # withdraw
account1.check_balance() # Balance
