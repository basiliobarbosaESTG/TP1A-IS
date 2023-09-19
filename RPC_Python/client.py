import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("3 é par: %s" % str(proxy.is_even(3)))
    print("100 é par: %s" % str(proxy.is_even(100)))
    print("153 é par: %s" % str(proxy.is_even(153)))
    print("160 é par: %s" % str(proxy.is_even(160)))