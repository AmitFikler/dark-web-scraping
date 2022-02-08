
def is_paste_equal(paste, flag):
    """
    :return: True if deep equality and else False
    """
    return paste["Title"] == flag["Title"] and paste["Author"] == flag["Author"] and paste["Content"] == flag["Content"] and paste["Date"] == flag["Date"]
