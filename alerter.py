alert_failure_count = 0


def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    if(celcius <= 200):
    # Return 200 for ok
        return 200
    else:
    # Return 500 for not-ok
        return 500


def network_alert_real(celcius):
    return 200

def ConvertFarenheitToCelcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    return celcius

def alert_in_celcius(farenheit, network_alert_real):
    celcius = ConvertFarenheitToCelcius(farenheit)
    returnCode = network_alert_real(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0 

alert_in_celcius(303.6, network_alert_stub)
alert_in_celcius(400.5, network_alert_stub)

print(f'{alert_failure_count} alerts failed.')
assert(alert_failure_count == 1)
print('All is well (maybe!)')
