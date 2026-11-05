from cashback import cashback

def test_cashback_completo():
    assert cashback([50, 100, 200]) == 15.0
    assert cashback([]) == 0.0
    assert cashback([99.99]) == 0.0
    assert cashback([100.0]) == 5.0
