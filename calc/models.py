from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='category_subcategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
