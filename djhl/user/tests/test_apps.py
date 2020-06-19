from djhl.user.apps import UserConfig


def test_core():
    assert UserConfig.name == "djhl.user"
