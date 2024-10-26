from django import forms


class PlaceholderMixin:
    def add_placeholders(self):
        for field_name, field in self.fields.items():
            placeholder = (field.label or field_name.replace("_", " "))
            placeholder = " ".join(word.capitalize() for word in placeholder.split())
            placeholder = placeholder.replace("Url", "URL")
            field.widget.attrs["placeholder"] = placeholder

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholders()


class CapitalizeLabelsMixin:
    def add_labels(self):
        for field_name, field in self.fields.items():
            if field.label:
                capitalized_label = ' '.join(word.capitalize() for word in field.label.split())
                capitalized_label = capitalized_label.replace("Url", "URL")
                field.label = capitalized_label

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_labels()


class DisableFieldsMixin(forms.Form):
    disabled_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if self.disabled_fields[0] == "__all__" or field_name in self.disabled_fields:
                field.disabled = True
