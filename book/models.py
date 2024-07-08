from django.db import models
from django.contrib.auth.models import User
from book.helpers import SaveMedia


class Author(models.Model):
    first_name = models.CharField(verbose_name="姓名", max_length=50)
    last_name = models.CharField(verbose_name="姓", max_length=50)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=SaveMedia.save_book_image_path, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    book = models.ManyToManyField(Book)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


