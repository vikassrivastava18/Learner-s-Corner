from django.shortcuts import render, HttpResponse

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def library(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    if request.method == 'GET':
        new_books=[]
        num_books=Book.objects.all().count()
        num_instances=BookInstance.objects.all().count()
        # Available copies of books
        book_instances=BookInstance.objects.all()
        for book in book_instances:
            new_books.insert(0,book)
        num_instances_available=BookInstance.objects.filter(status__exact='a').count()
        num_authors=Author.objects.count()  # The 'all()' is implied by default.
        genres = Genre.objects.all()
        # Number of visits to this view, as counted in the session variable.
        num_visits=request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits+1
        
        # Render the HTML template index.html with the data in the context variable.
        return render(
            request,
            'lib.html',
            context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
                'num_visits':num_visits,'arrivals':new_books, 'Genres':genres},
        )
    else: 
        bookinfo = request.POST["q"]
        books = Book.objects.filter(title__icontains=bookinfo)
        return render(request,'searched_book.html',context={'books':books})

def book_by_genre(request, genre):
    allitems = {}
    items = []
    books = Book.objects.filter(genre__name=genre)
    return render(request,'genre.html',context={'books':books})

def book_detail(request, isbn):
    bookinstance = BookInstance.objects.filter(book__isbn=isbn)
    book = Book.objects.get(isbn=isbn)
    link = "http://covers.openlibrary.org/b/isbn/" + isbn + "-M.jpg"
    return render(request, 'book_detail.html', context={'bookinstance':bookinstance,'book':book,'link':link})




