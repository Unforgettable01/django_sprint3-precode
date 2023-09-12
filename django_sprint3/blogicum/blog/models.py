from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Location(BaseModel):
    name = models.CharField(max_length=256)

    class Meta:
        varbose_name = 'географическая метка'
        varbose_name_plyral = 'Географические метки'


class Category(BaseModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    
    class Meta:
        varbose_name = 'категория'
        varbose_name_plyral = 'Категории'


class Post(BaseModel):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True)
    category = models.ForeignKey(
        Category,        
        on_delete=models.SET_NULL)
        
    class Meta:
        varbose_name = 'публикация'
        varbose_name_plyral = 'Публикации'