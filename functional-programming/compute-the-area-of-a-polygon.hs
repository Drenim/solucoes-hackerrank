import Control.Monad

area points = abs (sum (area' points)) / 2
  where
    diffOfProd x y = fst x * snd y - snd x * fst y
    area' [x] = [diffOfProd x (head points)]
    area' (x : xs) = diffOfProd x (head xs) : area' xs

readFloats :: IO [Float]
readFloats = fmap (map read . words) getLine

main = do
  n <- readLn :: IO Int
  points <-
    forM
      [1 .. n]
      ( \_ -> do
          [x, y] <- readFloats
          return (x, y)
      )
  print (area points)