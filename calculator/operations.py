def add(lhs, rhs):
    """add the two numbers lhs and rhs"""
    return lhs+rhs

def subtract(lhs, rhs):
    """subtract the two numbers lhs and rhs. In this implementation we use our own add function"""
    return add(lhs, rhs*(-1))

def multiply(lhs, rhs):
    """multiply the two numbers lhs and rhs"""
    return lhs*rhs

def devide(lhs, rhs):
    """devide the numbers lhs by rhs. In this implementation we use our own multiply function"""
    return lhs/rhs