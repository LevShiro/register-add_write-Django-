from django.shortcuts import render

# Create your views here.
def main_content(request):
    data={'title':'Главная страница',
    'text':'Здесь записана основная информация сайта'}

    return render(request,"main/main_content.html",data)

def about_content(request):
    return render(request,"main/about.html")



def contacts_content(request):
    data={'contacts':{'Юрий':'89080231121',
                    'Олег':'89339159375',
                    'Райан Гослинг':'84238175924'}}
    return render(request,"main/contacts.html",data)