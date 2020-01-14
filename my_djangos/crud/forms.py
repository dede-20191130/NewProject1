from django import forms

EMPTY_CHOICES = (
    ('', '-' * 10),
)

TYPE_CHOICES = (
    ('animal', 'animal'),
    ('plant', 'plant'),
    ('mineral', 'hard rock'),
)

FOOD_CHOICES = (
    ('apple', 'りんご'),
    ('beef', '牛肉'),
    ('bread', 'パン'),

)


class MessageForm(forms.Form):
    message = forms.CharField(
        label='メッセージ',
        max_length=255,
        required=True,
        widget=forms.TextInput())
    type = forms.ChoiceField(
        label='種類',
        widget=forms.RadioSelect,
        choices=TYPE_CHOICES,
        required=False,
    )
