def attribute(kwargs):
    attrs = []
    for key, value in kwargs.items():
        if key in ['klass', 'clazz']:
            key = 'class'
        attrs.append(f'{key}="{value}"')
    return " ".join(attrs)
