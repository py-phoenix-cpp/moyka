from django.shortcuts import render

def Index(request):
    return render(request, 'dashboard/index.html')

def Account_setting(request):
    return render(request, 'dashboard/account-setting.html')


def test():
    discond = Discond.objects.create(
        all_sum = 200,
        quantity = 2
    )
    client = Cliend.objects.get(id=2)
    cliend.price += discond.all_sum
    cliend.quantiy += discond.quantity
    cliend.save()
