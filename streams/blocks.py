from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock



class JumboBanner(blocks.StructBlock):
    
    jumbo_content = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title",  blocks.CharBlock(required=True, max_length=45)),
                ("subtitle",  blocks.TextBlock(required=True, max_length=150)),
                ("request_quot", blocks.PageChooserBlock(required=False)),
                ("read_more", blocks.PageChooserBlock(required=True)),
            ]
        )
    )
    
    
    class Meta:
        template = "streams/jumbo.html"
        icon = "placeholder"
        label = "Jumbo Banner"
        
        
class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Cards for more details"
        
        
class Partners(blocks.StructBlock):
    """Cards with image and text and button(s)."""

    Partners_section = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
                
                
            ]
        )
    )
    partners =  blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True))
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"