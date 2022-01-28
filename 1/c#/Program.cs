List<int> multiples = new();

int limit = 1000;
int x = 3, y = 5;

for (int i = 2; i < limit; i++)
{
  if ((i % x == 0) || (i % y == 0))
  {
    multiples.Add(i);
  }
}

int sum = 0;

multiples.ForEach((int x) => sum += x);

Console.WriteLine(sum);