x = [ 2 * x | x <- [1..10], x < 4]

y s = sum [1 | x <- s, x == 'e']

z s = [x | x <- s, x /= ' ']

between a b l = [x | x <- l, x > a, x < b]

multTwos s = [ if q `mod` 2 == 0 then "Two" else "No" | q <- s]

f y s = [ if p > y then p + 5 else p `div` 2 | p <- s]

twoFour = [(x, y) | x <- [1..2], y <- [1..4]]

multSquared = [(x * y) ^ 2 | x <- [1..3], y <- [1..3]]

array a b = [(x, y) | x <- [1..a], y <- [x..b]]

p m = [(x, y, z) | x <- [1..m], y <- [x..m], z <- [y..m], x ^ 2 + y ^ 2 == z ^ 2]

nestedOdds s = [[ sii | sii <- si, odd sii] | si <- s]

nestedNoSpace s = [[y | y <- x, y /= ' '] | x <- s]

