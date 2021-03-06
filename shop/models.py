from django.db import models
import os


def get_upload_path(instance, filename):
    # ext = filename.split('.')[-1]
    # filename = '{}-{}.{}'.format(instance.product.slug, instance.id,  ext)
    return os.path.join(
    '%s' % instance.product.brand,'%s' % instance.product.model, filename)

def get_upload_path_thumb(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}-{}.{}'.format(instance.slug, instance.id,  ext)
    return os.path.join(
    '%s' % instance.brand,'%s' % instance.model, 'thumb', filename)

class ProductCategory(models.Model):
    title = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'slug')
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Product(models.Model):
    brand = models.CharField(max_length=10)
    model = models.CharField(max_length=20)
    desc = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    sale = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to=get_upload_path_thumb)
    inStock = models.DecimalField(decimal_places=0, max_digits=3, default=100)
    saleToday = models.BooleanField(default=False)
    categories = models.ManyToManyField(ProductCategory)

    def __str__(self):
        return '%s %s' %(self.brand, self.model)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_path)

class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    size = models.DecimalField(decimal_places=0, max_digits=2)
    sizeInStock = models.IntegerField(default=1)




