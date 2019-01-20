def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n,max_n,unique_words)


tswift = ((2014,"Katy"),(2014,"Harry"),(2012,"Jake"),(2010,"Taylor"),(2008,"Joe"))

(min,max,numberofpeople) = get_data(tswift)

print(min,max,numberofpeople)