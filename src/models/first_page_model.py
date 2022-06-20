import attr
from faker import Faker

fake = Faker()


@attr.s
class FirstPageModel:
    blank_text: str = attr.ib(default=None)

    @classmethod
    def random(cls):
        return FirstPageModel(blank_text="selene")
