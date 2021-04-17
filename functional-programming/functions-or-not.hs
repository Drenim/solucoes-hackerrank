import Control.Monad
import Data.Map (Map)
import qualified Data.Map as Map

isFunction pairs = if isFunction' pairs Map.empty then "YES" else "NO"
  where
    isFunction' [] map' = True
    isFunction' ((x, y) : xs) map' = Map.notMember x map' && isFunction' xs (Map.insert x y map')

readInts :: IO [Int]
readInts = fmap (map read . words) getLine

main :: IO ()
main = do
  t <- readLn :: IO Int
  forM_
    [1 .. t]
    ( \_ -> do
        n <- readLn :: IO Int
        pairs <-
          forM
            [1 .. n]
            ( \_ -> do
                [x, y] <- readInts
                return (x, y)
            )
        putStrLn (isFunction pairs)
    )
