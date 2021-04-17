import Control.Monad

dist x y = sqrt ((fst x - fst y) ** 2 + (snd x - snd y) ** 2)

perimeter points = perimeter' points
  where
    perimeter' [x] = dist x (head points)
    perimeter' (x : xs) = dist x (head xs) + perimeter' xs

readFloats :: IO [Float]
readFloats = fmap (map read . words) getLine

main :: IO ()
main = do
  n <- readLn :: IO Float
  points <-
    forM
      [1 .. n]
      ( \_ -> do
          [x, y] <- readFloats
          return (x, y)
      )
  print (perimeter points)