module Main where

gcd' :: Integral a => a -> a -> a
gcd' n m
  | n == m = n
  | n > m = gcd' (n - m) m
  | otherwise = gcd' n (m - n)

main = do
  input <- getLine
  print . uncurry gcd' . listToTuple . convertToInt . words $ input
  where
    listToTuple (x : xs : _) = (x, xs)
    convertToInt = map (read :: String -> Int)