def sum(a: int, b: int) -> int:
  """return the sum of two number
  """
  if a is None or b is None:
    print("Invalid numbers")
  return a + b

if __name__ == "__main__":
  sum()
