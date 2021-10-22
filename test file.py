
expected_value = [{'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
                          {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
                          {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
                          {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
                          {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}]
for value in (expected_value):
    expected_platform = value.get('platform')
    expected_browser = value.get('browser')
    expected_device = value.get('device')
    print(expected_platform, expected_browser, expected_device)


