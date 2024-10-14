from django import forms


class DisableFieldsMixin(forms.Form):
    disabled_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if self.disabled_fields[0] == "__all__" or field_name in self.disabled_fields:
                field.disabled = True


class ExcludeFieldsMixin(forms.Form):
    excluded_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in list(self.fields.keys()):
            if field_name in self.excluded_fields:
                del self.fields[field_name]


