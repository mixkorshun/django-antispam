from django import forms
from django.utils.safestring import mark_safe


class HoneypotInput(forms.TextInput):
    """
    Default honey pot field widget.
    
    Display text input in hidden div.
    """
    @property
    def is_hidden(self):
        return True

    def render(self, *args, **kwargs):
        """
        Returns this widget rendered as HTML.
        """
        return mark_safe(
            '<div style="display: none;">%s</div>' % str(super().render(*args, **kwargs))
        )
