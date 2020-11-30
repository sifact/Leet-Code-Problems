import re


def defangIpAddress(address):
    return address.replace('.', '[.]')


def defangIpAddress2(address):
    return '[.]'.join(address.split('.'))


def defangIpAddress3(address):
    return re.sub('\.', '[.]', address)


def defangIpAddress4(address):
    return ''.join('[.]' if c == '.' else c for c in address)
