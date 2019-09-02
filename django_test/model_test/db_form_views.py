from django.shortcuts import render

from .models import Test


# Create your views here.
def db_operation(request):
    print(request.body)
    submit_type = request.POST.get("type", None)
    if submit_type == 'insert' and 'insert-name' in request.POST and request.POST['insert-name']:
        name = request.POST['insert-name']
        test = Test(name=name)
        test.save()
    elif submit_type == 'delete' and 'delete-name' in request.POST and request.POST['delete-name']:
        name = request.POST['delete-name']
        Test.objects.filter(name=name).delete()
    elif submit_type == 'delete_all':
        Test.objects.filter().delete()

    objs = Test.objects.all()
    data_list = list()
    for t in objs:
        data_list.append(t.name)
    context = {
        "data_list": data_list
    }
    return render(request, 'db_form.html', context)
