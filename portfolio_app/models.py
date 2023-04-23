from django.db import models
from django_quill.fields import QuillField

# Create your models here.

STATUS_CHOICES = (
    ('F', 'Featured'),
    ('P', 'Popular'),
)
class Videos(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.CharField(max_length=512)
    thumbnail = models.ImageField(upload_to='thumbnail', null=True, blank=True, default="default.jpg")
    duration = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='F')
    is_published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.title
    

class About(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    phone = models.CharField(default=0, max_length=20)
    heading = models.TextField()
    about_desc1 = models.TextField(null=True, blank=True)
    about_image = models.ImageField(upload_to='aboutImage', default="about.jpg")
    about_desc2 = models.TextField(null=True, blank=True)
    contact_desc = models.TextField(null=True, blank=True)
    contact_image = models.ImageField(upload_to='contactImage', default="contact.jpg")
    social_youtube = models.CharField(max_length=255, null=True, blank=True)
    social_facebook = models.CharField(max_length=255, null=True, blank=True)
    social_twitter = models.CharField(max_length=255, null=True, blank=True)
    social_instagram = models.CharField(max_length=255, null=True, blank=True)
    social_pinterest = models.CharField(max_length=255, null=True, blank=True)
    main_banner = models.ImageField(upload_to='mainBanner', default="main-banner.jpg")

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About Detail"


    def __str__(self):
        return self.name
    

class Articles(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    posted_on = models.DateTimeField(auto_now_add=True)
    description = QuillField()
    thumbnail = models.ImageField(upload_to='articleThumbnail', null=True, blank=True, default="article_default.jpg")
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Snap Shot"
        verbose_name_plural = "Snap Shots"


    def __str__(self):
        return self.title
