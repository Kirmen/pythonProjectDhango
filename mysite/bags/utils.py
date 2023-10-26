class MyMixin:
    mixin_prop = ''
    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, some_string: str):
        if isinstance(some_string, str):
            return some_string.upper()
        else:
            return some_string.title.upper()
