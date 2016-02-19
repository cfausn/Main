#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

#include "memory.h"
#include "assert.h"

/*
 * Frame size (in bytes / chars)
 *
 * Frame size must be a multiple of double for proper alignment of anything
 * placed in the allocated area.
 *
 * See MB_MULT below.
 */
#define FRAME_SIZE	(64 * sizeof(double))	// 512 bytes

/*
 * Number of allocatable frames and a frame structure.
 * This is the limit to the number of outstanding allocations at
 * any given time.
 */
#define NUM_FRAMES	(100)
typedef struct {
	bool frame_inuse ;
	short frame_bytes ;
	double frame_area[FRAME_SIZE / sizeof(double)] ;	// really char *
} frame ;

/*
 * Default fill character - used help detect overrun of the allocated
 * space.
 */

#define FILL_CHAR	(0x5a)

/*
 * The arena itself
 */
static frame arena[NUM_FRAMES] ;

/*
 * Local Support Function Declarations.
 *
 * All are at the end of this source file after the
 * global functions declared in memory.h
 */
static frame *ptr_to_frame(char *p) ;
static bool at_frame_start(char *p) ;
static frame *find_free_frame() ;
static void init_frame_area(frame *fp, char fillch) ;
static bool frame_arena_tail_filled_with(frame *fp, char fillch) ;

/*
 * Attempt to allocate space to hold <nbytes>.
 */
void *malloc_impl(size_t nbytes) {

	/*
	 * Fail if request is for more than one frame's capacity.
	 */
	assert_mesg(nbytes <= FRAME_SIZE,
		"malloc: too many bytes requested") ;
	if( nbytes > FRAME_SIZE) {
		return NULL ;
	}

	/*
	 * Fail if we can't find any space.
	 */
	frame *fp = find_free_frame() ;
	assert_mesg( fp != NULL, "malloc: can't find free memory" ) ;
	if( fp == NULL ) {
		return NULL ;
	}

	/*
	 * We found a frame. Mark it as in use and record the number of
	 * bytes actually requested, and fill the allocated space with
	 * junk bytes.
	 */
	fp->frame_inuse = true ;
	fp->frame_bytes = nbytes ;
	init_frame_area(fp, FILL_CHAR) ;

	/*
	 * Return a pointer to the start of the frame's portion of the
	 * overall allocation arena.
	 */
	return (void *)fp->frame_area ;
}

/*
 * Free the space allocated to <p>. This must have previously
 * been allocated by malloc().
 */
void free_impl(void *p) {
	/*
	 * Find the frame corresponding to the pointer.
	 * The pointer must be to the start of the frame's area.
	 */
	frame *fp = ptr_to_frame(p) ;
	bool at_start = fp != NULL && (p == (void *)fp->frame_area) ;

	assert_mesg(at_start, "free: pointer is not to allocated space") ;
	if( ! at_start ) {
		return ;
	}

	/*
	 * We should not free memory twice.
	 */
	int inuse = fp->frame_inuse ;
	assert_mesg(inuse, "free: pointer to space not in use") ;

	/*
	 * If freeing memory, do a simple check for overwriting past the
	 * part of the frame corresponding to the number of bytes
	 * requested in the original malloc call. This is not guaranteed
	 * to detect all such errors.
	 */
	if( inuse ) {
		assert_mesg(frame_arena_tail_filled_with(fp, FILL_CHAR),
			"free: overwrote past allocated space") ;
	}

	/*
	 * Clear the inuse flag and reset the number of bytes allocated
	 * in the frame.
	 */
	fp->frame_inuse = false ;
	fp->frame_bytes = 0 ;

	return ;
}

/*
 * Does pointer <p> refer to properly allocated space?
 *    + Is it in the arena AND
 *    + Does it refer to an arena frame that's in use AND
 *    + Is it within the actually allocated space in the frame.
 */
bool is_ptr_valid(void *p) {
	frame *fp = ptr_to_frame(p) ;

	/*
	 * If there is no frame (because the pointer is outside
	 * the arena) or the frame is not in use, return false.
	 */
	if( fp == NULL || ! fp->frame_inuse ) {
		return false ;
	}

	/*
	 * Return true iff the pointer is in that part of the
	 * frame that was actually allocated by the malloc() call.
	 */
	return ((char *)p - (char *)fp->frame_area) < fp->frame_bytes ;
}

/*
 * What is the allocated size of the frame <p> refers to? Requres that <p>:
 *    + Is in the arena AND
 *    + Refers to an arena frame that's in use.
 * If these conditions are not met then the function returns (-1).
 */
int frame_allocation(void *p) {
	frame *fp = ptr_to_frame(p) ;

	/*
	 * If there is no frame (because the pointer is outside
	 * the arena) or the frame is not in use, return (-1).
	 */
	if( fp == NULL || ! fp->frame_inuse ) {
		return (-1) ;
	}

	/*
	 * Return the number of bytes in the frame that were
	 * allocated by the malloc() call.
	 */
	return fp->frame_bytes ;
}

/*
 * Set the frame size (in bytes) and the number of frames
 * Here for compatibility with the dynamic version of the memory system.
 * Always returns false.
 */
bool set_memory_params(long fs, long nf) {
	return false ;
}

/*
 * Return the number of allocated but not freed memory areas.
 */
int allocated_area_count() {
	int i = 0 ;
	int count = 0 ;

	while( i < NUM_FRAMES ) {
		if( arena[i].frame_inuse ) {
			count++ ;
		}
		i++ ;
	}
	return count ;
}

/*******************
 * Local Support Functions.
 ******************/

/*
 * Given a pointer <p>, return a pointer to the frame information
 * structure corresponding to the frame to which <p> refers.
 * Returns NULL if <p> is not in the arena (allocated by us).
 */
static frame *ptr_to_frame(char *p) {
	int i = 0 ;

	while ( i < NUM_FRAMES ) {
		char *fr_area = (char *)arena[i].frame_area ;

		if( p >= fr_area && p < fr_area + FRAME_SIZE ) {
			return &arena[i] ;
		}
		i++ ;
	}

	return NULL ;
}

/*
 * Find a free frame to satisfy a malloc request. Returns
 * NULL if all frames are in use.
 */
static frame *find_free_frame() {
	int i = 0 ;

	while( i < NUM_FRAMES && arena[i].frame_inuse ) {
		i++ ;
	}
	return (i < NUM_FRAMES) ? &arena[i] : NULL ;
}

/*
 * Initialize all bytes in a frame's portion of the arena to a
 * fill character. Used to (TRY TO):
 * (a) trigger early problems for programs that refer to newly
 *     allocated space before putting something in it and
 * (b) check calls to free to determine whether the client accessed
 *     went past the number of bytes requested at malloc time.
 */
static void init_frame_area(frame *fp, char fillch) {
	char *p_ch = (char *)fp->frame_area ;
	int i ;

	for( i = 0 ; i < FRAME_SIZE ; i++ ) {
		p_ch[i] = fillch ;
	}
}

/*
 * Upon freeing space, see if that portion of the frame beyond what
 * was explicitly requested at malloc time still contains the fill
 * character. See init_frame_arena.
 */
static bool frame_arena_tail_filled_with(frame *fp, char fillch) {
	int unalloc_byte_idx = fp->frame_bytes ;
	char *area = (char *)fp->frame_area ;

	while( unalloc_byte_idx < FRAME_SIZE ) {
		if( area[unalloc_byte_idx] != fillch ) {
			break ;
		}
		unalloc_byte_idx++ ;
	}
	return unalloc_byte_idx >= FRAME_SIZE ;
}
