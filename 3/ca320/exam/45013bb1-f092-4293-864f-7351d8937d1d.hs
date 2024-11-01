is_zero :: Int -> Bool
is_zero 0 = True
is_zero _ = False

fac :: Int -> Int
fac n = aux n 1
  where
    aux n acc
      | n <= 1 = acc
      | otherwise = aux (n - 1) (n * acc)