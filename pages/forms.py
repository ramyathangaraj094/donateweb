from django import forms


class DonationForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        error_messages={"required": "Name is required."}
    )

    email = forms.EmailField(
        required=True,
        error_messages={"required": "Email is required."}
    )

    address = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}),
        required=True,
        error_messages={"required": "Address is required."}
    )

    amount = forms.ChoiceField(
        choices=[
            ("500", "₹500"),
            ("1000", "₹1000"),
            ("2000", "₹2000"),
        ]
    )

    cause = forms.ChoiceField(
        choices=[
            ("Education", "Education"),
            ("Food", "Food"),
            ("Health", "Health"),
        ]
    )


class VolunteerForm(forms.Form):

    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full border rounded-md p-3',
            'placeholder': 'Full Name'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full border rounded-md p-3',
            'placeholder': 'Email Address'
        })
    )

    phone = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'w-full border rounded-md p-3',
            'placeholder': 'Phone Number'
        })
    )

    area = forms.ChoiceField(
        choices=[
            ('', 'Area of Interest'),
            ('Education', 'Education'),
            ('Medical', 'Medical'),
            ('Food', 'Food'),
        ],
        widget=forms.Select(attrs={
            'class': 'w-full border rounded-md p-3'
        })
    )

    availability = forms.ChoiceField(
        choices=[
            ('', 'Availability'),
            ('Weekdays', 'Weekdays'),
            ('Weekends', 'Weekends'),
        ],
        widget=forms.Select(attrs={
            'class': 'w-full border rounded-md p-3'
        })
    )

    def clean_phone(self):
        phone = self.cleaned_data["phone"]

        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")

        if len(phone) != 10:
            raise forms.ValidationError("Phone number must be 10 digits.")

        return phone