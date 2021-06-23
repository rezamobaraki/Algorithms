"""
    این الگوریتم یک آرایه دریافت می کند و بیشترین مقدار_ارزش را برمی گرداند
    همچنین ، گاهی اوقات ممکن است چندین "بیشترین_تکرر" را داشته باشید ،
    بنابراین این تابع لیستی را برمی گرداند. از این نتیجه می توان برای یافتن a استفاده کرد
    مقدار نماینده در یک آرایه.
    این الگوریتم یک آرایه می گیرد ، از آن یک فرهنگ لغت درست می کند ،
    بیشترین تعداد را پیدا می کند و لیست نتایج را ایجاد می کند.
    ==========================
    this algorithm liked collection.counter
    -----------------------------------------------------------------------------
    This algorithm receives an array and returns most_frequent_value
    Also, sometimes it is possible to have multiple 'most_frequent_value's,
    so this function returns a list. This result can be used to find a
    representative value in an array.
    This algorithm gets an array, makes a dictionary of it,
    finds the most frequent count, and makes the result list.
    ==========================
    this algorithm liked collection.counter
    ---------------------------------------------------------------------------
    For example: top_1([1, 1, 2, 2, 3, 4]) will return [1, 2]
    (TL:DR) Get mathematical Mode
    Complexity: O(n)
"""


def top(arr):
    values = {}
    result = []
    f_val = 0

    for num in arr:
        if num in values:
            values[num] += 1
        else:
            values[num] = 1

    f_val = max(values.values())
    for i in values.keys():
        if values[i] == f_val:
            result.append(i)
        else:
            break
    return result, f_val


print(top([1, 1, 2, 2, 3, 4]))
