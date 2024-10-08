from BinarySearchTreeMap import *
def create_chain_bst(n):
    chain_bst = BinarySearchTreeMap()
    for i in range(n):
        chain_bst.insert(i + 1, None)
    return chain_bst


def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst


def add_items(bst, low, high):
    mid = (low + high) // 2
    bst.insert(mid, None)
    if low != high:
        add_items(bst, low, mid - 1)
        add_items(bst, mid + 1, high)