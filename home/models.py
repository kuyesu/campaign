from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db import models
from django.db.models.fields.related import ForeignKey

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

from wagtail.core.models import Page


class HomePage(Page):
    template = "home/home_page.html"
    
    site_title = models.CharField(blank=False, null=True, max_length=15)
    
    banner_title = models.CharField(blank=False, null=True, max_length=20)
    banner_subtitle = models.CharField(blank=False, null=True, max_length=100)
    banner_image = ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.CASCADE,
        related_name="+"
    )
    
    banner_cta = ForeignKey(
        'wagtailcore.Page',
        blank=False,
        null=True,
        on_delete=models.CASCADE,
        related_name="+"
    )
    
    
    section_two = StreamField(
        [
            ("jumbo", blocks.JumboBanner())
        ],
        null=True,
        blank=True,
        # min_num=1, 
        max_num=1
    )
    
    section_three = StreamField(
        [
            ("card", blocks.CardBlock()),
        ],
        null=True,
        blank=True,
        # min_num=1, 
    )
    
    partners_section = StreamField(
        [
            ("partner", blocks.Partners())
        ],
        null=True,
        blank=True,
        # min_num=1, 
        max_num=1
    )
