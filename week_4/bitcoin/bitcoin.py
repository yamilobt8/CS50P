import requests, sys

if len(sys.argv) == 1:
    print('Missing command-line argument')
    sys.exit(1)


try:
    if not sys.argv[1].replace('.', '', 1).isdigit():
        print('Command-line argument is not a number ')
        sys.exit(1)
    else:
        n = float(sys.argv[1])
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        result = response.json() 
        amount = (result['bpi']['USD']['rate_float']) * n
        print(f'${amount:,.4f}')
except requests.RequestException:
    sys.exit(1)
        