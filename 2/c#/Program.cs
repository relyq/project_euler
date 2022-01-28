int limit = 4000000;
int fibonacci = 1;
int last = fibonacci;
int sum = 0;
decimal golden = 0;

while (fibonacci <= limit)
{
  if (fibonacci % 2 == 0)
  {
    sum += fibonacci;
  }
  fibonacci += last;
  last = fibonacci - last;
}

golden = (decimal)fibonacci / last;

Console.WriteLine(sum);
Console.WriteLine(golden);