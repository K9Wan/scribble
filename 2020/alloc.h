#ifndef ALLOC_H_
#define ALLOC_H_

#include <stdlib.h>

void init(int max);

void terminate(void);

void * alloc(size_t size);

int mfree(void * p);

int my_free2(void ** p);

void free_all(void);

#endif  /* ALLOC_H_ */
