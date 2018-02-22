#coding=utf-8

# 从序列中移除重复项且保持元素间顺序不变

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == "__main__":
    # test hashable data
    l = [1,5,2,6,2,5,7]
    print(list(dedupe(l)))
    # test unhashable data
    d = [{'x':1, 'y':2},
         {'x':1, 'y':3},
         {'x':1, 'y':2},
         {'x':2, 'y':4}]
    print(list(dedupe(d, key=lambda arg: (arg['x'], arg['y']))))
    print(list(dedupe(d, key=lambda arg: arg['x'])))

