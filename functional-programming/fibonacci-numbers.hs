--Contributed by Ron Watkins
module Main where

fib 1 = 0
fib 2 = 1
fib n = fib' 3 0 1
  where
    fib' i fibMinusTwo fibMinusOne
      | i == n = fibMinusOne + fibMinusTwo
      | otherwise = fib' (i + 1) fibMinusOne (fibMinusOne + fibMinusTwo)

-- This part is related to the Input/Output and can be used as it is
-- Do not modify it
main = do
  input <- getLine
  print . fib . (read :: String -> Int) $ input