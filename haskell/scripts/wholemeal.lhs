Prompt: "Reimplement the following functions in a more idiomatic Haskell
style. Use wholemeal programming practices, breaking each function into
a pipeline of incremental transformations to an entire data structure."

FUNCTION ONE * * * * * * * * * * * * * * * * * * * *

Original:

> fun1 :: [Integer] -> Integer
> fun1 []       = 1
> fun1 (x:xs)
>   | even x    = (x - 2) * fun1 xs
>   | otherwise = fun1 xs

Wholemeal:

> fun1' :: [Integer] -> Integer
> fun1' = foldl1 (*)

fun1' = foldl1 (\prod (x:xs) -> (x - 2) * prod xs)

fun1' = foldl1 (*) worked

Scratchpad:

 Stepping through fun1...
 fun1 [3,4,5] = fun1 [4,5] 
 fun1 [4,5] = (4-2) * fun1 [5]
 fun1 [5] = []

FUNCTION TWO * * * * * * * * * * * * * * * * * * * *

Original:

> fun2 :: Integer -> Integer
> fun2 1             = 0
> fun2 n | even n    = n + fun2 (n `div` 2)
>        | otherwise = fun2 (3 * n + 1)

Wholemeal:

fun2 1 = 0 becomes takewhile (/= 1)
recursive calls to fun2 become iterate()
pipes become if/else statement

> fun2' :: Integer -> Integer
> fun2' = sum
>       . filter even
>       . takeWhile (/= 1)
>       . iterate (\n -> if even n
>                        then n `div` 2
>                        else 3 * n + 1)

Scratchpad:

I edited the wholemeal version to add .filter because...

I'm getting the wrong value for odd ns. 
Ex. fun2' 3 produces sum(3 + 10 + 5 + 16 + 8 + 4 + 2)
While fun2 3 produces sum(10 + 16 + 8 + 4 + 2)

Stepping through fun2...
fun2 10 = 10 + fun2 5
fun2 5  = fun2 16

Stepping through fun2'...
fun2 10 = 10 + fun2' 5
fun2 5 = 5 + fun2' 16

AH...fun2 skips odd numbers in summation.
I need to filter the list iterate returns for evens only.
