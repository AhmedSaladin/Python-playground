from django.shortcuts import render
# Create your views here (The logic).


# Create dummy data to test
posts = [{
    'author': 'CoryMs',
    'title': 'Post 1',
    'content': 'First post content',
    'date_posted': 'August 27,2018'
},
    {
    'author': 'Jane Doe',
    'title': 'Post 2',
    'content': 'Second post content',
    'date_posted': 'August 28,2018'
}]


def home(req):
    # context is passing data to template.
    context = {
        'posts': posts
    }

    return render(req, 'blog/home.html', context)


def about(req):
    return render(req, 'blog/about.html',{'title': 'About'})
