from rest_framework import serializers


class LinkOnVideoValidator:

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        tmp_value = dict(value).get(self.fields)
        if tmp_value is None or tmp_value == "":
            return value
        elif tmp_value:
            if "youtube" not in tmp_value:
                raise serializers.ValidationError("Вы прикрепили ссылку не на видео с ютуба")
