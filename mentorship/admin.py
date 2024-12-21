from django.contrib import admin
from  django.urls import reverse
from django.utils.html import format_html
from .models import ContactMessage
from .models import Testimonial
from .models import UserProfile
from django.contrib import admin
from .models import Course, Lecturer
from .models import Trainer

# Register your models here.
@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_display_links = ('email', 'name')
    list_filter = ('created_at',)
    
def edit_button(self, obj):
        # Generate the Edit button with a link to the edit page
        return format_html(
            '<a class="btn btn-primary btn-sm" href="{}">Edit</a>',
            reverse('admin:mentorship_contact_change', args=[obj.id])
        )
edit_button.short_description = 'Edit'  # Column title

def delete_button(self, obj):
        # Generate the Delete button with a link to the delete page
        return format_html(
            '<a class="btn btn-danger btn-sm" href="{}">Delete</a>',
            reverse('admin:mentorship_contact_delete', args=[obj.id])
        )
delete_button.short_description = 'Delete'  # Column title    



@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'image','created_at')
    search_fields = ('name', 'message')
    def image(self,obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 50px; height: auto;">'
        return 'No Image'
    
    image.allow_tags=True
    image.short_description='image'
    


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')
 
 
 # admin.py
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'lecturer', 'price')  
    search_fields = ('title', 'lecturer__name')  


admin.site.register(Course)
admin.site.register(Lecturer)


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')


    


