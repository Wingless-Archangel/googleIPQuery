import requests


GOOGLE_IPS_URL = "https://www.gstatic.com/ipranges/goog.json"



def main():
    # call google url to get the latest IP addresses
    res = requests.get(GOOGLE_IPS_URL)
    # extract prefixes from the whole json
    prefixes = res.json()["prefixes"]

    resultv4 = set()
    resultv6 = set()

    for elem in prefixes:
        for k,v in elem.items():
            if k == "ipv4Prefix":
                resultv4.add(v)
            else:
                resultv6.add(v)

    print(f"The IPv4 list is:\n{resultv4}\n")
    print(f"The IPv6 list is:\n{resultv6}")

if __name__ == "__main__":
    main()
