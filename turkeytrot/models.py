from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class SponsorBlock(blocks.StructBlock):
    """Block for sponsor information"""
    name = blocks.CharBlock(required=True, help_text="Sponsor name")
    logo = ImageChooserBlock(required=False, help_text="Sponsor logo")
    website_url = blocks.URLBlock(required=False, help_text="Sponsor website")
    description = blocks.TextBlock(required=False, help_text="Brief description")
    
    class Meta:
        template = "blocks/sponsor_block.html"
        icon = "user"
        label = "Sponsor"


class TurkeyTrotPage(Page):
    """Main Turkey Trot page model"""
    
    # Hero section
    title_override = models.CharField(
        max_length=255, 
        blank=True, 
        help_text="Override the page title displayed on the page"
    )
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Hero image for the page"
    )
    event_date = models.DateTimeField(
        blank=True, 
        null=True,
        help_text="Date and time of the event"
    )
    event_location = models.CharField(
        max_length=255,
        blank=True,
        help_text="Event location"
    )
    event_address = models.TextField(
        blank=True,
        help_text="Full event address"
    )
    
    # Navigation buttons
    donate_url = models.URLField(blank=True, help_text="Donation link")
    registration_url = models.URLField(blank=True, help_text="Registration link")
    sponsor_packet_pdf = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Upload sponsor packet PDF"
    )
    volunteer_url = models.URLField(blank=True, help_text="Volunteer signup")
    results_url = models.URLField(blank=True, help_text="Results link")
    photos_url = models.URLField(blank=True, help_text="Photos link")
    
    # Main content sections
    about_event = RichTextField(
        blank=True,
        help_text="About the event description"
    )
    
    # Route section
    route_description = RichTextField(
        blank=True,
        help_text="Description of the race route"
    )
    route_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Route map image"
    )
    parking_info = RichTextField(
        blank=True,
        help_text="Parking information"
    )
    
    # Sponsor section
    sponsor_description = RichTextField(
        blank=True,
        help_text="Description for sponsors section"
    )
    sponsors = StreamField([
        ('sponsor_level', blocks.StructBlock([
            ('level_name', blocks.CharBlock(help_text="e.g., Apple Pie, Pumpkin Pie")),
            ('sponsors', blocks.ListBlock(SponsorBlock(), help_text="Sponsors at this level"))
        ]))
    ], blank=True, use_json_field=True, help_text="Sponsor levels and sponsors")
    
    # About us section
    about_us = RichTextField(
        blank=True,
        help_text="About the organization"
    )
    about_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image for about us section"
    )
    
    # Library carousel
    library_images = StreamField([
        ('library_image', blocks.StructBlock([
            ('image', ImageChooserBlock()),
            ('caption', blocks.TextBlock(required=False))
        ]))
    ], blank=True, use_json_field=True, help_text="Future library images with captions")
    
    # Contact information
    mailing_address = models.TextField(blank=True)
    email_address = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('title_override'),
            FieldPanel('hero_image'),
            FieldPanel('event_date'),
            FieldPanel('event_location'),
            FieldPanel('event_address'),
        ], heading="Hero Section"),
        
        MultiFieldPanel([
            FieldPanel('donate_url'),
            FieldPanel('registration_url'),
            FieldPanel('sponsor_packet_pdf'),
            FieldPanel('volunteer_url'),
            FieldPanel('results_url'),
            FieldPanel('photos_url'),
        ], heading="Navigation Links"),
        
        MultiFieldPanel([
            FieldPanel('about_event'),
        ], heading="About Event"),
        
        MultiFieldPanel([
            FieldPanel('route_description'),
            FieldPanel('route_image'),
            FieldPanel('parking_info'),
        ], heading="Route Information"),
        
        MultiFieldPanel([
            FieldPanel('sponsor_description'),
            FieldPanel('sponsors'),
        ], heading="Sponsors"),
        
        MultiFieldPanel([
            FieldPanel('about_us'),
            FieldPanel('about_image'),
        ], heading="About Us"),
        
        MultiFieldPanel([
            FieldPanel('library_images'),
        ], heading="Future Library"),
        
        MultiFieldPanel([
            FieldPanel('mailing_address'),
            FieldPanel('email_address'),
            FieldPanel('phone_number'),
            FieldPanel('facebook_url'),
            FieldPanel('instagram_url'),
        ], heading="Contact Information"),
    ]
    
    class Meta:
        verbose_name = "Turkey Trot Page"
