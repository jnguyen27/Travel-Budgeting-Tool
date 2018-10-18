from django.shortcuts import render

posts = [
    {
        'author': 'Duy Nguyen',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'October 17, 2018'
    },
    {
        'author': 'Alice Nguyen',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'October 18, 2018'
    }
]

def home(request):
    # creating a context dictionary for posts
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
