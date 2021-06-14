#ifndef ALLOC2_H_
#define ALLOC2_H_

#include <stdlib.h>

void * alloc(size_t size);

int mfree(void * p);

void free_all(void);

#endif  /* ALLOC2_H_ */
