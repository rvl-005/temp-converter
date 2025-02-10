import app.temperature as temp
 
def test_temperature():
    testTemp = temp.Temperature(32, 'F')
    assert str(testTemp) == '32°F'