from django import forms
from django.utils.safestring import mark_safe


class HoneypotInput(forms.TextInput):
    @property
    def is_hidden(self):
        return True

    def render(self, *args, **kwargs):
        return mark_safe(
            '<div style="display: none;">%s</div>' % str(super().render(*args, **kwargs))
        )
