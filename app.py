from sys import argv
from os import getenv
from requests import get

# get API key from environment variables
API_KEY = getenv('API_KEY')

# API endpoint to get data
URL = f'https://api.macaddress.io/v1?apiKey={API_KEY}&output=json&search='


def search(mac_addr):
    """
        Function to accept mac address,
        make request to the endpoint,
        return company name and MAC address.

        If the MAC address is not correct,
        response won't contain `vendorDetails`,
        then the function will return the function will error message.

        ::mac_addr: string. MAC address to search
        ::return: string.
    """

    # create URL
    url = URL + mac_addr

    # make request
    response = get(url)

    # get json response as dict
    data = response.json()

    try:
        # get company name from response
        company_name = data['vendorDetails']['companyName']
        return f"Company name: {company_name} \nMac address: {mac_addr}"
    except KeyError:
        return "Something went wrong!"


if __name__ == '__main__':

    # if command has 0 or more than 1 argument, it's invalid command
    if len(argv) != 2:
        print('Invalid command!')

    else:
        # get MAC address from command arguments
        addr = argv[1]

        # run function to get data from API
        result = search(addr)

        # print result to the command line
        print(result)
