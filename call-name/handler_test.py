from .handler import handle

def test_handle():
    assert handle("world") == "안녕 world"
    pass
