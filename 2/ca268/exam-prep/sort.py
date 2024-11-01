#!/usr/bin/env python3#

def select_sort(a):
    for i in range(0, len(a)):
        p = i
        for j in range(i + 1, len(a)):
            if a[p] > a[j]:
                p = j
        tmp = a[i]
        a[i] = a[p]
        a[p] = tmp
    return a

def bubble_sort(a):
    changes = 1
    while changes > 0:
        changes = 0
        for i in range(0, len(a) - 1):
            if a[i] > a[i + 1]:
                tmp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = tmp
                changes += 1

    return a

def merge_sort(a):
    if len(a) < 2:
        return a

    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    b = []
    i = 0
    j = 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            b.append(left[i])
            i += 1
        else:
            b.append(right[j])
            j += 1

    while len(left) > i:
        b.append(left[i])
        i += 1

    while len(right) > j:
        b.append(right[j])
        j +=1

    return b

def quick_sort(a):
    if len(a) < 2:
        return a

    x = a[-1]

    l = []
    e = []
    g = []

    for n in a:
        if n > x:
            g.append(n)
        elif n < x:
            l.append(n)
        else:
            e.append(n)

    l = quick_sort(l)
    for n in e:
        l.append(n)
    for n in quick_sort(g):
        l.append(n)

    return l

def bucket_sort(a):
    b = []
    bucketCount = 10
    buckets = []

    for i in range(0, bucketCount):
        buckets.append([])

    for n in a:
        index = n // bucketCount
        buckets[index].append(n)
    
    for bucket in buckets:
        bucket = quick_sort(bucket)
        for num in bucket:
            b.append(num)
    return b

def count_sort(a):
    counts = []
    b = []
    for n in a:
        b.append(n)

    for i in range(0, max(a) + 1):
        counts.append(0)
    
    for n in a:
        counts[n] += 1

    i = 0
    while i < len(counts) - 1:
        counts[i + 1] += counts[i]
        i += 1
    
    for n in a:
        b[counts[n] - 1] = n
        counts[n] -= 1

    return b

def radix_sort(a):
    m = max(a)
    x = 0
    while m > 0:
        m = m // 10
        x += 1
    
    for i in range(0, x):
        a = count_sort(a, i)

    return a

def main():
    nums = [27, 801, 95, 4, 0, 98, 68, 189, 981, 24, 24, 56, 53, 12, 450, 128, 87, 78, 11, 49, 304, 201, 31]
    print("Numbers:", nums)

    #print("Selection:", select_sort(nums))
    #print("Bubble:", bubble_sort(nums))
    #print("Merge:", merge_sort(nums))
    #print("Quick:", quick_sort(nums))
    #print("Bucket:", bucket_sort(nums))
    print("Counting:", count_sort(nums))
    #print("Radix:", radix_sort(nums))


if __name__ == "__main__":
    main()