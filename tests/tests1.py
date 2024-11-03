from packages.models import Dog

def test_bark():
    dog = Dog("Brutus")
    assert "Brutus" in dog.bark()