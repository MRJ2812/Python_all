# It's like rest and spread
# get's perameter like 'dictionary' 


def xxargs(**pera):
    print(pera)
    print(pera["name"])
    print(pera["id"])

xxargs(name='Joy',id=101)                      ## name and id is like key