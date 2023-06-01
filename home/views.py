from django.shortcuts import render
from home.models import Contact, Blog
from PIL import Image

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    context = {'success': False}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name = name, email = email, subject = subject, message = message)
        contact.save()
        context = {'success': True}
        print("Tha data has been written to the DB")
    return render(request, 'contact.html', context)

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    # for blog in blogs:

        # image = Image.open(blog.image.url)
        # image.thumbnail((650, 400))
        # image.save()
        # print(image.size)
    return render(request, 'blog.html', context)

def blog_post(request, slug):
    blog = Blog.objects.filter(slug = slug).first()
    context = {'blog': blog}
    return render(request, 'blog-post.html', context)

def portfolio(request):
    return render(request, 'portfolio.html')



"""
          Procfile - heroku
web: waitress-serve --port=8000 portfolio.wsgi:application
web: waitress-serve --port=$PORT portfolio.wsgi:application
"""