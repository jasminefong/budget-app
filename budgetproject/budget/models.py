from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    budget = models.IntegerField()

    # override save method to automatically generate slugs
    def save(self, *args, **kwargs):
        # generate slug from the name of the project
        self.slug = slugify(self.name)
        # call the save method from the superclass
        super(Project, self).save(*args, **kwargs)

# every project has user-made categories
class Category(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # name of the type of category
    name = models.CharField(max_length=50)

# store multiple expenses for one project
class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)