from django.db import models
import uuid

from django.utils.translation import activate
# Create your models here.
from users.models import Profile, User
from django.conf import settings

class Recipe(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # null mean we are allowed to make a record (if I don't have a description yet.)
    intro = models.CharField(max_length=300)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) # Whenever it created, just set the time automatically
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    views = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ## -creacted == asc
        ordering = ['-views', '-vote_total','-created']
    
    @property
    def commenters(self):
        queryset = self.comment_set.all().values_list('owner__id', flat=True)
        return queryset

    @property
    def getLikesCount(self):
        comments = self.comment_set.all()
        totalVotes = comments.count()

        self.vote_total = totalVotes
        self.save()

    @property
    def getViews(self):
        self.views = self.views + 1
        self.save()

class Comment(models.Model):
    VOTE_TYPE = ( ('up', 'אהבתי'), ('down', 'לא אהבתי') )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE) #on_delete = if the recipe is deleted what do we wanna do with its children?
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together = [['owner', 'recipe']]

    def __str__(self) -> str:
        return self.value + "-" + str(self.id)

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    quanity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    direction = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class RecipeMethod(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    direction = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.description