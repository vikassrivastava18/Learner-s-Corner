from django.db import models

# Create your models here.

from django.urls import reverse #Used to generate urls by reversing the URL patterns

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    def __str__(self):
        return self.name
        

class Language(models.Model):

    name = models.CharField(max_length=200, help_text="Enter a the book's natural language (e.g. English, French, Japanese etc.), d")
    def __str__(self):
        return self.name
        
        
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    edition = models.DateField(null=True, blank=True)
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
        display_genre.short_description = 'Genre'
    
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return '{0}, {1}'.format(self.title,self.edition)
        
        
import uuid # Required for unique book instances
from datetime import date

from django.contrib.auth.models import User #Required to assign User as a borrower

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    arrival_date = models.DateField(null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
        
    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status= models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Book availability')

    class Meta:
        ordering = ["arrival_date"]
        permissions = (("can_mark_returned", "Set book as returned"),)   

    def __str__(self):
        #return '%s (%s)' % (self.id,self.book.title)
        return '{0} ({1}),{2}'.format(self.id,self.arrival_date,self.book.title)
        

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        ordering = ["last_name","first_name"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.first_name, self.last_name)
