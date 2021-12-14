#include <errno.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
  if (argc != 2) {
    printf("usage: fibonacci [limit]\n");
    return 1;
  }
  unsigned long limit;
  char* end;

  errno = 0;

  limit = strtol(argv[1], &end, 10);

  const bool range_error = errno == ERANGE;
  if (range_error) {
    printf("range error ocurred\n");
    return 2;
  }
  if (!limit) {
    printf("arguments cant be zero / no conversion can be performed\n");
    return 3;
  }

  unsigned long fibonacci = 1;
  unsigned long last = fibonacci;
  unsigned long sum = 0;

  while (fibonacci <= limit) {
    if (fibonacci % 2 == 0) {
      sum += fibonacci;
    }
    fibonacci += last;
    last = fibonacci - last;
  }

  printf("the sum of all even fibonacci numbers below %ld is %ld\n", limit,
         sum);
  return 0;
}