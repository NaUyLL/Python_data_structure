# 二叉树
def BinTree(data, left=None, right=None):
    return [data, left, right]

def is_empty_BinTree(btree):
    return btree is None

def root(btree):
    return btree[0]

def left(btree):
    return btree[1]

def right(btree):
    return btree[2]

def self_root(btree, data):
    btree[0] = data

def self_left(btree, left):
    btree[1] = left

def self_right(btree, right):
    btree[2] = right

