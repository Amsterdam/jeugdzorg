from django.forms.widgets import *


class ProfielCheckboxSelectMultiple(CheckboxSelectMultiple):
    option_template_name = 'form/checkbox_option.html'