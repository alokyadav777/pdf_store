from django.shortcuts import render
import base64
from first.models import Resume_class

def home(request):
    return render(request, 'index.html',{'content':"alok"})


def upload_file(request):
    object = Resume_class()
    final_val ="No PDF"
    if request.method == 'POST' and request.FILES['myfile']:
        # myfile = request.FILES['myfile']
        myfile = request.FILES['myfile']

        var = base64.b64encode(myfile.read())
        object.name=request.POST.get("fname")
        object.pdf_file=var.decode("utf-8")
        object.email=request.POST.get("email")
        object.phone=request.POST.get("phone")
        object.whywehire_message = request.POST.get("whywe")
        object.save()
        data=""
        data_instance= Resume_class.objects.all()
        for i in data_instance:
            if(i.name==object.name):
                data=i.pdf_file
                print(i.pdf_file)


        # print(var.decode("utf-8"))

        # final_val = "data:application/pdf;base64,"+data
        # return render(request, 'view.html', {'value': final_val})
        return render(request, 'index.html')
    # return render(request, 'view.html', {'value': final_val})
    return render(request, 'index.html')


def admin_view(request):
    aspirant_list = []
    database_object = Resume_class.objects.all()
    for i in database_object:
        resume_obj = Resume_class()
        resume_obj.name = i.name
        resume_obj.phone = i.phone
        resume_obj.email = i.email
        temp =i.whywehire_message
        resume_obj.whywehire_message = temp[:100]

        resume_obj.pdf_file = i.pdf_file

        aspirant_list.append(resume_obj)

    return render(request, 'home.html', {'aspirant_list': aspirant_list})


def pdf_viewer(request, phone_number):
    print("mobile num is="+ phone_number)
    db_object = Resume_class.objects.all()
    base64_value = ""
    for i in db_object:
        if i.phone == int(phone_number):
            base64_value = i.pdf_file

    
    final_val = "data:application/pdf;base64," + base64_value
    return render(request, 'view.html', {'base64_value': final_val})


def blog_view(request):

    return render(request, 'blog.html')


def candidate_details_view(request, phone_number):
    database_object = Resume_class.objects.filter(phone=phone_number)
    for i in database_object:
        if phone_number == i.phone:
                break

    content = {'name': i.name, 'phone': phone_number, 'email': i.email, 'pdf_file': i.pdf_file, 'whywehire_message': i.whywehire_message}

    return render(request, 'can_details.html', {'content': content})
