/*
 * Inteface to our simple memory management library.
 * Primarily useful for unit testing.
 */

#ifndef MEMORY_H
#define MEMORY_H

#include <stdlib.h>
#include <stdbool.h>

/*
 * Allocate enough space to hold <nbytes> bytes.
 * Return NULL if space cannot be found.
 * Macro malloc(n) invokes our version.
 */
extern void *malloc_impl(size_t nbytes) ;
#define malloc(n) (malloc_impl(n))

/*
 * Free the space referenced by <p>; this must have been
 * previously allocated by malloc().
 * Macro free(p) invokes our version.
 */
extern void free_impl(void *p) ;
#define free(p) (free_impl(p))

/*
 * Does pointer <p> refer to properly allocated space?
 * (Useful for unit tests).
 */
extern bool is_ptr_valid(void *p) ;

/*
 * What is the size of the area actually associated with <p>?
 * Returns (-1) if <p> does not refer to dynamically allocated space.
 */
extern int frame_allocation(void *p) ;

/*
 * Set the minimum frame size and the number of allocation
 * frames. This must be done prior to the first call on malloc().
 * Returns true iff the parameters were actually set.
 *
 * If either argument is <= 0 then the corresponding default is used.
 */
extern bool set_memory_params(long frame_size, long num_frames) ;

/*
 * Return the number of allocated but not freed memory areas.
 */
extern int allocated_area_count() ;

#endif
