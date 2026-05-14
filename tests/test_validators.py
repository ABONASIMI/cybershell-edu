from cybershell.validators import is_valid_ip, is_valid_port

def test_valid_ip():
    assert is_valid_ip("127.0.0.1") == True
    assert is_valid_ip("not-an-ip") == False

def test_valid_port():
    assert is_valid_port("80") == True
    assert is_valid_port("99999") == False
