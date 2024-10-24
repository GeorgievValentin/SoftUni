class PlaceholderMixin:
    def add_placeholders(self):
        for field_name, field in self.fields.items():  # ('first_name': field_obj)
            placeholder = field.label or field_name.replace('_', ' ').capitalize()
            field.widget.attrs['placeholder'] = placeholder

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholders()


class ReadOnlyMixin:
    read_only_fields = []

    def make_fields_readonly(self):
        for field_name in self.read_only_fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['readonly'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly()