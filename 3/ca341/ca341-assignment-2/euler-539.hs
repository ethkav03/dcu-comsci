main :: Int -> IO()
main a = putStrLn (test a 0)

test a b
    | a <= 1 = a
    | b == 0 = 2 * test (a / 2) 1
    | a `mod` 2 ~= 0 = (2 * test (a / 2) 0) - 1
    | otherwise = 2 * test (a / 2) 0