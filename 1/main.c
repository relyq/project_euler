#include <errno.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include "../../c_practice/vectors/vector.h"

int main(int argc, char** argv) {
  if (argc != 4) {
    printf("usage: multiples [x] [y] [limit]\n");
    return 1;
  }
  int x, y, limit;
  char* end;

  errno = 0;

  x = strtol(argv[1], &end, 10);
  y = strtol(argv[2], &end, 10);
  limit = strtol(argv[3], &end, 10);

  const bool range_error = errno == ERANGE;
  if (range_error) {
    printf("range error ocurred\n");
    return 2;
  }
  if (!x || !y || !limit) {
    printf("arguments cant be zero / no conversion can be performed\n");
    return 3;
  }

  vector v = vector_create(16);

  for (size_t i = 0; i < limit; i++) {
    if (i % x == 0 || i % y == 0) {
      vector_push(&v, i);
    }
  }

  int sum = 0;
  for (size_t i = 0; i < vector_size(&v); i++) {
    sum += vector_at(&v, i);
  }
  vector_destroy(&v);

  printf("the sum of all multiples of %d or %d below %d is %d\n", x, y, limit,
         sum);
  return 0;
}