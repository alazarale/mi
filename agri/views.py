from django.shortcuts import render
from .models import Post, Product
from .forms import ContactForm, CommentForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def home(request):
    posts = Post.objects.filter(active=True)[:3]
    products = Product.objects.filter(status='publish')[:2]
    if request.POST:
        form_contact = ContactForm(data=request.POST)
        if form_contact.is_valid():
            cd = form_contact.cleaned_data
            form_contact.save()

    else:
        form_contact = ContactForm()
    return render(request, 'contents/home.html', {'posts':posts, 'status':'home', 'form_contact':form_contact, 'products': products})

def news(request):
    object_list = Post.objects.filter(active=True)
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'contents/news.html', {'posts': posts, 'status':'news', 'page':page})

def detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             created__year=year,
                             created__month=month,
                             created__day=day,
                             slug=post,
                             )
    posts = Post.objects.filter(active=True)[:3]
    comments = post.post_commented.all()


    if request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_form = comment_form.save(commit=False)
            new_form.post = post
            new_form.save()
    else:
        comment_form = CommentForm()

    return render(request, 'contents/detail.html', {'post': post, 'posts':posts, 'comment_form': comment_form, 'comments': comments})

def product(request):
    products = Product.objects.filter(status='publish')
    return render(request, 'contents/product.html', {'products':products, 'status':'product'})

def description(request, month, day, name):
    product = get_object_or_404(Product,
                                created__month=month,
                                created__day = day,
                                slug=name,
    )

    return render(request, 'contents/description.html', {'product':product})

def contact(request):
    if request.POST:
        form_contact = ContactForm(data=request.POST)
        if form_contact.is_valid():
            cd = form_contact.cleaned_data
            form_contact.save()
            subject = 'Message from the site'
            message = "hello there"
            from_email = 'fordjangouse@gmail.com'
            to = ('fordjangouse@gmail.com',)
            send_mail(subject, message, from_email, to, fail_silently=False)
    else:
        form_contact = ContactForm()
    return render(request, 'contents/contact.html', {'status':'contact', 'form_contact': form_contact})

def service(request):
    return render(request, 'contents/service.html', {'status': 'service'})